"""Checks every vocabulary source and its exports.

Each test runs once per file in ``vocabularies/``, so a failure names the vocabulary
it concerns.
"""

from collections import Counter

import pytest
from build_vocabularies import (
    BASE_URL,
    EXPORT_FORMATS,
    canonical_turtle,
    export,
    load,
    source_files,
)
from rdflib import RDF, Literal, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import DCTERMS, FOAF, SKOS

SOURCES = source_files()
LABELLED_TYPES = (SKOS.ConceptScheme, SKOS.Concept, SKOS.Collection)


@pytest.fixture(params=SOURCES, ids=[path.stem for path in SOURCES])
def source(request):
    return request.param


@pytest.fixture
def graph(source):
    return load(source)


@pytest.fixture
def scheme(graph):
    schemes = list(graph.subjects(RDF.type, SKOS.ConceptScheme))
    assert len(schemes) == 1, f"expected one concept scheme, found {len(schemes)}"
    return schemes[0]


class TestSource:
    def test_there_are_vocabularies(self):
        assert SOURCES

    def test_is_in_the_fixed_layout(self, source, graph):
        expected = canonical_turtle(graph, source.stem)
        assert source.read_text(encoding="utf-8") == expected, (
            "run `uv run python scripts/build_vocabularies.py` to rewrite it"
        )


class TestScheme:
    def test_address_matches_the_file_name(self, source, scheme):
        assert scheme == URIRef(BASE_URL + source.stem)

    def test_has_an_english_label_and_description(self, graph, scheme):
        for predicate in (SKOS.prefLabel, DCTERMS.description):
            values = [value.language for value in graph.objects(scheme, predicate)]
            assert "en" in values, f"scheme has no English {predicate}"

    @pytest.mark.parametrize(
        "predicate",
        [DCTERMS.creator, DCTERMS.publisher, DCTERMS.license, DCTERMS.source],
        ids=lambda predicate: predicate.split("/")[-1],
    )
    def test_states_its_provenance(self, graph, scheme, predicate):
        assert (scheme, predicate, None) in graph

    def test_names_its_creator_and_publisher(self, graph, scheme):
        for predicate in (DCTERMS.creator, DCTERMS.publisher):
            for agent in graph.objects(scheme, predicate):
                assert (agent, FOAF.name, None) in graph, f"{agent} has no name"

    def test_cites_its_sources(self, graph, scheme):
        for source in graph.objects(scheme, DCTERMS.source):
            assert (source, DCTERMS.bibliographicCitation, None) in graph, (
                f"{source} has no citation"
            )


class TestConcepts:
    def test_scheme_has_concepts(self, graph):
        assert list(graph.subjects(RDF.type, SKOS.Concept))

    def test_every_concept_is_in_the_scheme(self, graph, scheme):
        outside = [
            concept
            for concept in graph.subjects(RDF.type, SKOS.Concept)
            if (concept, SKOS.inScheme, scheme) not in graph
        ]
        assert not outside

    def test_every_address_is_under_the_scheme(self, graph, scheme):
        namespace = str(scheme) + "/"
        outside = [
            subject
            for kind in (SKOS.Concept, SKOS.Collection)
            for subject in graph.subjects(RDF.type, kind)
            if not str(subject).startswith(namespace)
        ]
        assert not outside

    def test_everything_has_one_english_label(self, graph):
        def english_labels(subject):
            labels = graph.objects(subject, SKOS.prefLabel)
            return [label for label in labels if label.language == "en"]

        wrong = [
            subject
            for kind in LABELLED_TYPES
            for subject in graph.subjects(RDF.type, kind)
            if len(english_labels(subject)) != 1
        ]
        assert not wrong

    def test_no_two_concepts_share_a_label(self, graph):
        labels = Counter(
            (str(label).casefold(), label.language)
            for concept in graph.subjects(RDF.type, SKOS.Concept)
            for label in graph.objects(concept, SKOS.prefLabel)
        )
        assert not [label for label, count in labels.items() if count > 1]

    def test_every_text_has_a_language_and_content(self, graph):
        wrong = [
            (subject, predicate)
            for subject, predicate, value in graph
            if isinstance(value, Literal)
            and predicate != SKOS.notation
            and (not value.language or not value.strip())
        ]
        assert not wrong

    def test_notations_have_no_language_and_are_unique(self, graph):
        notations = [value for value in graph.objects(None, SKOS.notation)]
        assert not [value for value in notations if value.language]
        assert len(notations) == len(set(notations))

    def test_collection_members_exist(self, graph):
        missing = [
            member
            for collection in graph.subjects(RDF.type, SKOS.Collection)
            for member in graph.objects(collection, SKOS.member)
            if (member, RDF.type, SKOS.Concept) not in graph
        ]
        assert not missing

    def test_related_concepts_exist(self, graph):
        missing = [
            target
            for predicate in (SKOS.broader, SKOS.narrower, SKOS.related)
            for target in graph.objects(None, predicate)
            if (target, RDF.type, SKOS.Concept) not in graph
        ]
        assert not missing

    @pytest.mark.parametrize(
        ("predicate", "inverse"),
        [
            (SKOS.broader, SKOS.narrower),
            (SKOS.narrower, SKOS.broader),
            (SKOS.related, SKOS.related),
        ],
        ids=["broader", "narrower", "related"],
    )
    def test_relationships_are_stated_both_ways(self, graph, predicate, inverse):
        one_way = [
            (subject, target)
            for subject, target in graph.subject_objects(predicate)
            if (target, inverse, subject) not in graph
        ]
        assert not one_way

    def test_top_concepts_are_exactly_those_without_a_broader_concept(
        self, graph, scheme
    ):
        concepts = set(graph.subjects(RDF.type, SKOS.Concept))
        without_broader = {c for c in concepts if (c, SKOS.broader, None) not in graph}
        top = set(graph.objects(scheme, SKOS.hasTopConcept))
        top_of = set(graph.subjects(SKOS.topConceptOf, scheme))
        assert top == without_broader
        assert top_of == without_broader

    def test_related_concepts_are_not_also_in_a_hierarchy(self, graph):
        clashes = [
            (subject, target)
            for subject, target in graph.subject_objects(SKOS.related)
            if (subject, SKOS.broader, target) in graph
            or (subject, SKOS.narrower, target) in graph
        ]
        assert not clashes


@pytest.fixture(scope="module")
def exported(tmp_path_factory):
    directory = tmp_path_factory.mktemp("export")
    export(directory)
    return directory


class TestExport:
    @pytest.mark.parametrize("extension", EXPORT_FORMATS)
    def test_holds_the_same_graph_as_its_source(
        self, exported, source, graph, extension
    ):
        target = exported / f"{source.stem}{extension}"
        assert isomorphic(graph, load(target))

    def test_writes_one_file_per_vocabulary_and_format(self, exported):
        written = sorted(path.name for path in exported.iterdir())
        expected = sorted(
            f"{path.stem}{extension}"
            for path in SOURCES
            for extension in EXPORT_FORMATS
        )
        assert written == expected
