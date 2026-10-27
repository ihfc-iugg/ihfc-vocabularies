"""Rewrite the vocabulary sources in their fixed form, or export them.

The Turtle files in ``vocabularies/`` are the source. Run with no arguments after
editing a vocabulary, to rewrite each file exactly as rdflib serialises it, so every
file has one layout and a diff shows only what changed::

    uv run python scripts/build_vocabularies.py

Run with ``--export`` to write every vocabulary in every format into one directory,
where the files differ only by extension. The release workflow does this::

    uv run python scripts/build_vocabularies.py --export dist/ihfc-vocabularies
"""

import argparse
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import DCTERMS, OWL, RDF, SKOS

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "vocabularies"
SOURCE_FORMAT = "longturtle"
BASE_URL = "https://portal.heatflow.world/vocabularies/"

# File extension -> rdflib format.
EXPORT_FORMATS = {
    ".ttl": SOURCE_FORMAT,
    ".rdf": "xml",
    ".jsonld": "json-ld",
    ".nt": "nt",
}


def source_files():
    """Return the vocabulary source files, sorted by name."""
    return sorted(SOURCE_DIR.glob("*.ttl"))


def load(path):
    """Parse an RDF file into a graph, in the format its extension names."""
    return Graph().parse(path)


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


def serialize(graph, name, extension):
    """Return the vocabulary called ``name`` in the format for ``extension``."""
    return with_prefixes(graph, name).serialize(format=EXPORT_FORMATS[extension])


def canonical_turtle(graph, name):
    """Return the vocabulary called ``name`` serialised in the fixed source layout."""
    return serialize(graph, name, ".ttl")


def rewrite_sources():
    """Rewrite every source file in its fixed layout."""
    for source in source_files():
        text = canonical_turtle(load(source), source.stem)
        source.write_text(text, encoding="utf-8")


def export(directory):
    """Write every vocabulary in every format into ``directory``."""
    directory.mkdir(parents=True, exist_ok=True)
    for source in source_files():
        graph = load(source)
        for extension in EXPORT_FORMATS:
            target = directory / f"{source.stem}{extension}"
            target.write_text(serialize(graph, source.stem, extension), "utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--export",
        type=Path,
        metavar="DIR",
        help="write every vocabulary in every format into DIR",
    )
    arguments = parser.parse_args()
    if arguments.export:
        export(arguments.export)
    else:
        rewrite_sources()
