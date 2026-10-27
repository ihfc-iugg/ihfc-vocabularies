# Domain Docs

Which of this repository's domain documents to read before working in it, and in what order.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root — the glossary.
- **`CONSTITUTION.md`** — the rules every change follows.
- **`docs/adr/`** — architectural decisions, when there are any.

This is a single-context repo. There is no `CONTEXT-MAP.md`.

## File structure

```
/
├── vocabularies/           ← the source files, one vocabulary each, edited by hand
├── data/                   ← exports in RDF/XML, JSON-LD and N-Triples, generated
├── scripts/                ← build_vocabularies.py
├── tests/                  ← the checks every vocabulary must pass
├── CONTEXT.md              ← glossary
└── CONSTITUTION.md         ← rules and quality bar
```

## The meaning of a concept is scientific

What a heat-flow concept means is defined by the published structure of the Global Heat Flow
Database (Fuchs et al., 2021, *A new database structure for the IHFC Global Heat Flow Database*,
Earth System Science Data; Fuchs et al., 2023, *The Global Heat Flow Database: Update 2023*), not
by this repository. Never write or reword a definition from inference. Take it from that
literature or from the maintainers in an issue.

## Use the glossary's vocabulary

When your output names a concept from this repository — in an issue title, a pull request or a
test name — use the term as defined in `CONTEXT.md`. If the term you need is not there, either
you are inventing language the project does not use, or there is a gap worth recording.
