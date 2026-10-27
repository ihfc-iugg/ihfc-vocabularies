# IHFC Heat Flow Vocabularies

[![Checks](https://github.com/ihfc-iugg/ihfc-vocabularies/actions/workflows/checks.yml/badge.svg)](https://github.com/ihfc-iugg/ihfc-vocabularies/actions/workflows/checks.yml)
[![Vocabularies: CC BY 4.0](https://img.shields.io/badge/vocabularies-CC%20BY%204.0-lightgrey.svg)](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/LICENSE-CC-BY-4.0)

Controlled vocabularies for the scientific study of Earth's heat flow, published as
[SKOS](https://www.w3.org/2004/02/skos/) concept schemes. They define the values used to describe
heat-flow measurements in the [Global Heat Flow Database](https://heatflow.world): how heat flow,
temperature and thermal conductivity were determined, what was corrected, and where and why the
measurement was made.

The vocabularies were developed with the international heat flow community during the
restructuring of the Global Heat Flow Database, and are used to assess the quality of heat-flow
data and metadata.

## Vocabularies

Each vocabulary is one file in `vocabularies/`, and its address is
`https://heatflow.world/vocabularies/<name>`.

| Name | Label |
| --- | --- |
| `conductivity-conditions` | Conductivity measurement conditions |
| `conductivity-location` | Conductivity location |
| `conductivity-methods` | Conductivity methods |
| `conductivity-pt-function` | Thermal conductivity PT function |
| `conductivity-saturation` | Heat-flow specific conductivity saturation states |
| `conductivity-sources` | conductivity sources |
| `conductivity-strategy` | Thermal conductivity strategy |
| `exploration-methods` | exploration methods |
| `exploration-purpose` | Exploration purposes |
| `geographic-environments` | geographic environments |
| `heat-flow-corrections` | Generic flag choices |
| `heat-flow-method` | Heat flow methods |
| `heat-flow-probes` | Heat flow probe types |
| `temperature-corrections` | Temperature correction methods |
| `temperature-method` | Temperature determination method |

## Using the vocabularies

The Turtle files in `vocabularies/` are the source. The same vocabularies are under `data/` in
three more RDF formats:

| Format | Folder |
| --- | --- |
| RDF/XML | `data/rdf-xml/*.rdf` |
| JSON-LD | `data/json-ld/*.jsonld` |
| N-Triples | `data/n-triples/*.nt` |

Any RDF library can read them. For example, with [rdflib](https://rdflib.readthedocs.io):

```python
from rdflib import Graph

url = "https://raw.githubusercontent.com/ihfc-iugg/ihfc-vocabularies/main/vocabularies/heat-flow-method.ttl"
graph = Graph().parse(url)
```

A concept's address never changes once it is published. A concept that is withdrawn stays in its
vocabulary, marked as deprecated, so data that refers to it keeps resolving.

## Scope & philosophy

**What this is.** The single published source of the heat-flow vocabularies. Applications that
need them, such as the Global Heat Flow Database portal, import these files rather than keeping
their own copies.

**What this is not.** It is not software. There is no package to install and no code that builds
the vocabularies. The only code is a script that checks and exports the files. It does not host
the vocabularies at their addresses either: that is the job of whatever serves
`heatflow.world`.

**When in doubt:**

- The Turtle file is the truth. Everything under `data/` is derived from it.
- Data that already refers to a concept matters more than tidiness. Correct a label or a
  definition, but never change what a published address means.
- A translation is another language-tagged label on the same concept, never a separate file.

## Contributing

Suggestions and corrections are welcome. Please open an issue to discuss a change before opening a
pull request.

To change a vocabulary, edit its file in `vocabularies/`, then rewrite it in its fixed layout and
regenerate the exports:

```bash
uv sync
uv run python scripts/build_vocabularies.py
uv run pytest
```

The checks confirm that every file parses and that:

- each file holds one vocabulary, named after the file
- every concept belongs to its vocabulary, has one English label, and has an address under the vocabulary's address
- no two concepts in a vocabulary share a label
- every label and definition has a language tag and is not empty
- every concept a collection or relationship names exists
- every export matches its source file

The rules behind these checks are in [`CONSTITUTION.md`](CONSTITUTION.md), and the words used for
the parts of a vocabulary are in [`CONTEXT.md`](CONTEXT.md).

## Attribution

Maintained by the [GFZ Helmholtz Centre for Geosciences](https://www.gfz.de/en/) through the
[World Heat Flow Database Project](https://heatflow.world), funded by the Deutsche
Forschungsgemeinschaft (DFG), project number 491795283.

## License

The vocabularies, in `vocabularies/` and `data/`, are licensed under the
[Creative Commons Attribution 4.0 International License](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/LICENSE-CC-BY-4.0).
The script and tests are licensed under the
[MIT License](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/LICENSE).
