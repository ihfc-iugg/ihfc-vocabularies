"""Rewrite the vocabulary sources in their fixed form and regenerate the exports.

The Turtle files in ``vocabularies/`` are the source. This script rewrites each one
exactly as rdflib serialises it, so every file has one layout and a diff shows only
what changed. It then writes each vocabulary to ``data/`` in every export format.

An export is rewritten only when the graph it holds differs from its source. RDF/XML
and JSON-LD come out of rdflib in a different order on every run, so rewriting them
unconditionally would change every file on every build.

Run it after editing a vocabulary::

    uv run python scripts/build_vocabularies.py
"""

from pathlib import Path

from rdflib import Graph
from rdflib.compare import isomorphic
from rdflib.namespace import DCTERMS, OWL, RDF, SKOS

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "vocabularies"
EXPORT_DIR = ROOT / "data"
SOURCE_FORMAT = "longturtle"
BASE_URL = "https://portal.heatflow.world/vocabularies/"

# Export folder name -> (rdflib format, file extension).
EXPORT_FORMATS = {
    "rdf-xml": ("xml", ".rdf"),
    "json-ld": ("json-ld", ".jsonld"),
    "n-triples": ("nt", ".nt"),
}


def source_files():
    """Return the vocabulary source files, sorted by name."""
    return sorted(SOURCE_DIR.glob("*.ttl"))


def load(path, rdf_format="turtle"):
    """Parse an RDF file into a graph."""
    return Graph().parse(path, format=rdf_format)


def with_prefixes(graph, name):
    """Return a copy of the graph bound to the fixed set of prefixes.

    ``ihfc:`` is the base address, so a vocabulary reads ``ihfc:heat-flow-method``.
    The empty prefix is the vocabulary's own namespace, so its concepts read
    ``:bullard``. Any prefix the file was written with is dropped.
    """
    prefixed = Graph(bind_namespaces="none")
    for triple in graph:
        prefixed.add(triple)
    prefixed.bind("", f"{BASE_URL}{name}/")
    prefixed.bind("ihfc", BASE_URL)
    prefixed.bind("rdf", RDF)
    prefixed.bind("skos", SKOS)
    prefixed.bind("dcterms", DCTERMS)
    prefixed.bind("owl", OWL)
    return prefixed


def canonical_turtle(graph, name):
    """Return the vocabulary called ``name`` serialised in the fixed source layout."""
    return with_prefixes(graph, name).serialize(format=SOURCE_FORMAT)


def export_path(source, folder):
    """Return where the export of ``source`` in the given format is written."""
    extension = EXPORT_FORMATS[folder][1]
    return EXPORT_DIR / folder / f"{source.stem}{extension}"


def serialize_export(graph, folder):
    """Return the graph serialised in an export format.

    N-Triples is sorted line by line so that the file is the same on every run.
    """
    text = graph.serialize(format=EXPORT_FORMATS[folder][0])
    if folder == "n-triples":
        lines = sorted(line for line in text.splitlines() if line.strip())
        text = "\n".join(lines) + "\n"
    return text


def build():
    """Rewrite every source in its fixed form and bring every export up to date."""
    for source in source_files():
        graph = load(source)
        source.write_text(canonical_turtle(graph, source.stem), encoding="utf-8")
        for folder, (rdf_format, _extension) in EXPORT_FORMATS.items():
            target = export_path(source, folder)
            if target.exists() and isomorphic(graph, load(target, rdf_format)):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            text = serialize_export(with_prefixes(graph, source.stem), folder)
            target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    build()
