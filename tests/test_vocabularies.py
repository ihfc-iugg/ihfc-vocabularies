"""Checks every vocabulary source and its exports.

Each test runs once per file in ``vocabularies/``, so a failure names the vocabulary
it concerns.
"""

from collections import Counter

import pytest
from build_vocabularies import (
    EXPORT_FORMATS,
    canonical_turtle,
    export_path,
    load,
    source_files,
)
from rdflib import RDF, Literal, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import DCTERMS, SKOS

SOURCES = source_files()
BASE_URL = "https://portal.heatflow.world/vocabularies/"
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
        expected = canonical_turtle(graph)
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
            if isinstance(value, Literal) and (not value.language or not value.strip())
        ]
        assert not wrong

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


@pytest.mark.parametrize("folder", EXPORT_FORMATS)
def test_export_matches_its_source(source, graph, folder):
    target = export_path(source, folder)
    assert target.exists(), f"{target.name} is missing"
    assert isomorphic(graph, load(target, EXPORT_FORMATS[folder][0])), (
        "run `uv run python scripts/build_vocabularies.py` to regenerate it"
    )


def test_every_export_has_a_source():
    stems = {path.stem for path in SOURCES}
    orphans = [
        path
        for folder in EXPORT_FORMATS
        for path in export_path(SOURCES[0], folder).parent.iterdir()
        if path.stem not in stems
    ]
    assert not orphans
