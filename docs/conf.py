"""Sphinx configuration for the IHFC Controlled Vocabularies site.

Every vocabulary in ``vocabularies/`` gets a page, and so does each of its concepts and
collections, at its URI with ``skos_base_uri`` removed. Build with the ``dirhtml``
builder so each page sits at that address as a directory.
"""

project = "IHFC Controlled Vocabularies"
author = "International Heat Flow Commission"
copyright = (
    "International Heat Flow Commission. The vocabularies are licensed under CC BY 4.0"
)
language = "en"

extensions = ["sphinx_skos"]
skos_vocabularies = ["../vocabularies/*.ttl"]
skos_base_uri = "https://w3id.org/ihfc/vocabularies/"

exclude_patterns = ["_build", "agents", "contributing"]

html_theme = "furo"
html_title = project
