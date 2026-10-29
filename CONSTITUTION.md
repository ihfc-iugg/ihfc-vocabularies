# IHFC Vocabularies Constitution

The rules every change to this repository follows. The words in it are defined in
[`CONTEXT.md`](CONTEXT.md).

## Core articles

### Article I — Testing
Every change follows [`docs/contributing/standards/testing.md`](docs/contributing/standards/testing.md): what gets a test
and what does not, the test-first cycle, and test structure.

### Article II — Simplicity
Start with the simplest change that does the job. A new dependency, script or piece of
infrastructure needs a stated reason in the pull request.

### Article III — Anti-Abstraction
No wrapper layers, base classes or indirection without a present, concrete second use. Prefer
duplication over the wrong abstraction.

### Article IV — Integration-First
The vocabularies are an interface other systems import. A change is judged by what those
systems will read: an address, an identifier, a label. The tests check the files the way an
importer reads them.

### Article V — Security & data-safety
Secrets live in runtime configuration, never in the repository. No change removes or renames
something an importer may already have stored (Article XII).

### Article VI — Documentation
A change to what the vocabularies contain is recorded in `CHANGELOG.md` in the same pull
request. A change to how they are edited, checked or exported updates the README in the same
pull request. Docstrings and comments follow
[`docs/contributing/standards/code-documentation.md`](docs/contributing/standards/code-documentation.md), and any page under `docs/`
follows [`docs/contributing/standards/documentation.md`](docs/contributing/standards/documentation.md).

### Article VII — Dependency discipline
A new dependency needs a stated reason. The vocabularies depend on rdflib and nothing else.
Development uses pytest and pre-commit, and the documentation site uses sphinx-skos, which
brings Sphinx and the furo theme, in the `docs` dependency group.

## Project articles

### Article VIII — The source files are the vocabularies
The Turtle files in `vocabularies/` are the only place a vocabulary is defined and the only
files anyone edits. Each is kept in the fixed layout. Copies in other RDF formats are generated
from them by `scripts/build_vocabularies.py` when a release is published, and are never committed.

### Article IX — One vocabulary per file
Each source file holds exactly one concept scheme, whose address is
`https://w3id.org/ihfc/vocabularies/` followed by the file name. The concept scheme has an
English `skos:prefLabel` and an English `dcterms:description`, and names its creator and
publisher (`dcterms:creator`, `dcterms:publisher`), its licence (`dcterms:license`) and the
publications its values come from (`dcterms:source`) and the data publication it is part of
(`dcterms:isPartOf`), each with a citation. Every concept and collection in
the file has an address under it, and every concept is `skos:inScheme` it.

### Article X — Every text has a language
Every label and definition carries a language tag. English is required for every label. A
translation is a further language-tagged value on the same concept, never a separate file.
No text is empty.

### Article XI — References resolve
Every concept a collection names, and every concept a `skos:broader`, `skos:narrower` or
`skos:related` points at, exists in the same vocabulary.

### Article XII — Addresses are permanent
Once a concept is published, its address and identifier never change and are never reused for a
different meaning. A concept that is withdrawn stays in its file, marked `owl:deprecated true`,
with `dcterms:isReplacedBy` when a successor exists. Labels and definitions may be corrected;
what the concept means may not.

### Article XIII — Stack
Python 3.12 or later, managed with uv. rdflib reads and writes every file. pytest runs the
checks, and pre-commit runs the linters. sphinx-skos builds the documentation site with
Sphinx and the furo theme, from its settings in `pyproject.toml`. CI is this repository's own
workflow.

## Quality bar

Read at review; applies to every change.

- Every check in `tests/` passes for every vocabulary.
- Every vocabulary exports to every format without losing anything.
- pre-commit passes.
- `CHANGELOG.md` records every change to what a vocabulary contains.

## Non-negotiables

- Tests and lint pass before a change merges. Nobody overrides a red check.
- The default branch requires one approval, and the author of a change never approves it.

---

**Version**: 4.0.0 | **Ratified**: 2026-10-27 | **Last Amended**: 2026-10-29
