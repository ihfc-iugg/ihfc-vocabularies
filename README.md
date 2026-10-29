# IHFC Controlled Vocabularies

[![DOI](https://img.shields.io/badge/DOI-10.5880%2Ffidgeo.2026.065-blue.svg)](https://doi.org/10.5880/fidgeo.2026.065)
[![Latest release](https://img.shields.io/github/v/release/ihfc-iugg/ihfc-vocabularies)](https://github.com/ihfc-iugg/ihfc-vocabularies/releases/latest)
[![Checks](https://github.com/ihfc-iugg/ihfc-vocabularies/actions/workflows/checks.yml/badge.svg)](https://github.com/ihfc-iugg/ihfc-vocabularies/actions/workflows/checks.yml)
[![Vocabularies: CC BY 4.0](https://img.shields.io/badge/vocabularies-CC%20BY%204.0-lightgrey.svg)](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/LICENSE-CC-BY-4.0)

The IHFC Controlled Vocabularies are the controlled terms the International Heat Flow Commission
(IHFC) maintains for the Global Heat Flow Database (GHFDB) and related heat-flow data products.
They set the permitted values for the metadata fields used when heat-flow data are submitted,
validated, assessed for quality and published.

The GHFDB is the primary international repository for terrestrial and marine heat-flow
measurements. Comparing and reusing those measurements depends on consistent metadata: how a
measurement was made, which corrections were applied, and the geological and environmental
setting of the site. Shared terminology makes that metadata consistent across datasets, makes
automated quality checks possible, and supports the FAIR data principles.

The vocabularies were developed during the restructuring of the GHFDB. They cover the method used
to calculate a heat-flow value, the probe and exploration context, the geographic setting, the
type of temperature measurement and its corrections, and the thermal conductivity parameters:
source, location, measurement method, saturation state, measurement conditions, pressure and
temperature correction, and averaging strategy.

There are fifteen vocabularies, each a SKOS (Simple Knowledge Organization System) concept scheme
written in RDF Turtle. Every vocabulary and concept has a persistent URI under
`https://w3id.org/ihfc/vocabularies/` and an English label and definition. Translations
are further language-tagged labels on the same concepts, so they never change a URI. The Turtle
files are edited directly and checked automatically on every change. Each versioned release
publishes them, with copies in RDF/XML, JSON-LD and N-Triples, as a citable snapshot.

The repository is maintained by the [GFZ Helmholtz Centre for Geosciences](https://www.gfz.de/en/)
through the [World Heat Flow Database Project](https://heatflow.world), funded by the Deutsche
Forschungsgemeinschaft (DFG), project number 491795283. The vocabularies are released under the
Creative Commons Attribution 4.0 International licence (CC BY 4.0).

## Vocabularies

### Thermal conductivity measurement conditions

- **Name:** `conductivity-conditions`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-conditions>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-conditions.ttl>

The pressure and temperature conditions under which thermal conductivity was measured, and whether they were recorded, replicated or corrected to in-situ conditions.

### Thermal conductivity location

- **Name:** `conductivity-location`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-location>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-location.ttl>

Where the thermal conductivity used for a heat-flow value was measured, relative to the heat-flow site.

### Thermal conductivity methods

- **Name:** `conductivity-methods`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-methods>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-methods.ttl>

Methods used to determine thermal conductivity, by laboratory measurement, in-situ probe, well-log interpretation or estimation.

### Thermal conductivity pressure and temperature functions

- **Name:** `conductivity-pt-function`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-pt-function>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-pt-function.ttl>

Functions used to correct measured thermal conductivity for the effects of pressure (p), temperature (T) or both (pT).

### Thermal conductivity saturation states

- **Name:** `conductivity-saturation`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-saturation>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-saturation.ttl>

The saturation state of the rock when its thermal conductivity was measured.

### Thermal conductivity sources

- **Name:** `conductivity-sources`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-sources>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-sources.ttl>

The material or data the thermal conductivity values were obtained from, such as core samples, well logs or the literature.

### Thermal conductivity strategies

- **Name:** `conductivity-strategy`
- **URI:** <https://w3id.org/ihfc/vocabularies/conductivity-strategy>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/conductivity-strategy.ttl>

The strategy used to obtain thermal conductivity values for the depth interval of a heat-flow determination.

### Exploration methods

- **Name:** `exploration-methods`
- **URI:** <https://w3id.org/ihfc/vocabularies/exploration-methods>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/exploration-methods.ttl>

The general means by which temperature sensors gained access to the rock, such as drilling, probing, mining or tunnelling.

### Exploration purposes

- **Name:** `exploration-purpose`
- **URI:** <https://w3id.org/ihfc/vocabularies/exploration-purpose>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/exploration-purpose.ttl>

The main purpose of the original excavation that gave temperature sensors access to the rock.

### Geographic environments

- **Name:** `geographic-environments`
- **URI:** <https://w3id.org/ihfc/vocabularies/geographic-environments>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/geographic-environments.ttl>

The basic geographic environment in which a heat-flow measurement was made, onshore or offshore.

### Correction flags

- **Name:** `heat-flow-corrections`
- **URI:** <https://w3id.org/ihfc/vocabularies/heat-flow-corrections>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/heat-flow-corrections.ttl>

Flags recording whether an effect that can bias heat-flow data was present, and whether it was considered or corrected.

### Heat-flow methods

- **Name:** `heat-flow-method`
- **URI:** <https://w3id.org/ihfc/vocabularies/heat-flow-method>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/heat-flow-method.ttl>

Methods used to determine a heat-flow value from temperature and thermal conductivity data.

### Heat-flow probe types

- **Name:** `heat-flow-probes`
- **URI:** <https://w3id.org/ihfc/vocabularies/heat-flow-probes>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/heat-flow-probes.ttl>

Types of probe used to measure heat flow, mainly in marine settings.

### Temperature correction methods

- **Name:** `temperature-corrections`
- **URI:** <https://w3id.org/ihfc/vocabularies/temperature-corrections>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/temperature-corrections.ttl>

Methods used to correct measured temperatures for disturbances, such as those caused by drilling, before heat flow is derived.

### Temperature methods

- **Name:** `temperature-method`
- **URI:** <https://w3id.org/ihfc/vocabularies/temperature-method>
- **Source:** <https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/vocabularies/temperature-method.ttl>

Methods used to measure or estimate the temperatures from which heat flow is derived.

## Using the vocabularies

Each [release](https://github.com/ihfc-iugg/ihfc-vocabularies/releases) carries every vocabulary
in four formats, as separate files that differ only by extension:

| Format | Extension |
| --- | --- |
| Turtle | `.ttl` |
| RDF/XML | `.rdf` |
| JSON-LD | `.jsonld` |
| N-Triples | `.nt` |

A link with a version always returns that release's file:

```text
https://github.com/ihfc-iugg/ihfc-vocabularies/releases/download/v2026.1/heat-flow-method.jsonld
```

A link with `latest` always returns the file from the newest release:

```text
https://github.com/ihfc-iugg/ihfc-vocabularies/releases/latest/download/heat-flow-method.jsonld
```

Each release also carries `vocabularies-full.zip`: every vocabulary in every format, with this
README, the list of contributors, the changelog and the licence, in a folder named after the
version. The newest one is always at
<https://github.com/ihfc-iugg/ihfc-vocabularies/releases/latest/download/vocabularies-full.zip>.

With the [GitHub CLI](https://cli.github.com), `gh release download v2026.1 --repo ihfc-iugg/ihfc-vocabularies`
downloads every file of a release.

Any RDF library can read the files. For example, with [rdflib](https://rdflib.readthedocs.io):

```python
from rdflib import Graph

url = "https://github.com/ihfc-iugg/ihfc-vocabularies/releases/latest/download/heat-flow-method.ttl"
graph = Graph().parse(url, format="turtle")
```

A concept's URI never changes once it is published. A concept that is withdrawn stays in its
vocabulary, marked as deprecated, so data that refers to it keeps resolving.

## Repository structure

```text
vocabularies/          the fifteen vocabularies, one Turtle file each: the only files edited
scripts/
  build_vocabularies.py  rewrites the Turtle files in their fixed layout, and exports them
tests/                 the checks every vocabulary must pass
docs/                  the documentation site: its settings and its own pages
.github/workflows/
  checks.yml           runs the checks on every pull request
  publish.yml          creates a release and attaches its files
CONTRIBUTORS.md        everyone who has contributed to the vocabularies
CHANGELOG.md           what changed in each release
CONSTITUTION.md        the rules every change follows
CONTEXT.md             the words used for the parts of a vocabulary
```

### How the vocabularies are maintained

The Turtle files in `vocabularies/` are the vocabularies. There is no other source and no
generated copy in the repository. A change is made by editing a file directly, in a pull request:

```bash
uv sync
uv run python scripts/build_vocabularies.py
uv run pytest
```

The build script rewrites every file in one fixed layout, so a diff shows only what changed in
meaning. The checks run on every pull request and confirm that every file parses and that:

- each file holds one vocabulary, named after the file, with an English label and description
- each vocabulary names its creator, publisher, licence and sources, and the data publication it is part of, and cites each
- every concept belongs to its vocabulary, has one English label, and has a URI under the vocabulary's URI
- no two concepts in a vocabulary share a label
- every label and definition has a language tag and is not empty
- every concept a collection or relationship names exists
- `skos:broader`, `skos:narrower` and `skos:related` are stated in both directions, and the top concepts are exactly those with no broader concept
- codes in `skos:notation` are unique within a vocabulary
- every vocabulary can be written in every release format without losing anything
- the documentation site builds without warnings and its front page lists every vocabulary

The rules behind these checks are in
[`CONSTITUTION.md`](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/CONSTITUTION.md), and
the words used for the parts of a vocabulary are in
[`CONTEXT.md`](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/CONTEXT.md).

### How the documentation site is built

The site in `docs/` is built with [Sphinx](https://www.sphinx-doc.org/) and
[sphinx-skos](https://github.com/FAIR-DM/sphinx-skos), which writes a page for every
vocabulary, concept and collection, at its URI with `https://w3id.org/ihfc/vocabularies/`
removed, and its RDF beside it. Those pages are written on every build and are not committed.
The front page and the how-to guides are the only pages kept in `docs/`. A new vocabulary is
added to the list on the front page, `docs/index.rst`, and its two generated paths to
`.gitignore`.

```bash
uv run sphinx-build -W -b dirhtml docs docs/_build/dirhtml
```

### How releases are made

A maintainer runs the **Publish** workflow from the repository's Actions tab, on `main`. It runs
the checks, works out the next version from the current year and the last release (`v2026.1`,
`v2026.2`, then `v2027.1` in a new year), and creates the release with the `[Unreleased]` notes
from `CHANGELOG.md`. It then exports every vocabulary into every format and attaches the files and
the release archive.

What changed in each release is recorded in
[`CHANGELOG.md`](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/CHANGELOG.md).
Changes waiting for the next release are listed under `[Unreleased]`.

## Contributing

Suggestions and corrections are welcome. Please open an
[issue](https://github.com/ihfc-iugg/ihfc-vocabularies/issues) to discuss a change before opening
a pull request.

## Scope & philosophy

**What this is.** The single published source of the heat-flow vocabularies. Applications that
need them, such as the Global Heat Flow Database portal, import these files rather than keeping
their own copies.

**What this is not.** It is not software. There is no package to install, and the only code is
the script that checks and exports the files. Its URIs resolve through
[w3id.org](https://w3id.org) to the documentation site built from these files, with a page for
every vocabulary and concept.

**When in doubt:**

- The Turtle file is the truth. Every other format is derived from it.
- Data that already refers to a concept matters more than tidiness. Correct a label or a
  definition, but never change what a published URI means.
- A translation is another language-tagged label on the same concept, never a separate file.

## How to cite

Jennings, Samuel; Neumann, Florian; Norden, Ben; Balkan-Pazvantoğlu, Elif; Elbarbary, Samah;
Petrunin, Alexey G.; Elger, Kirsten; Fuchs, Sven (2026): IHFC Controlled Vocabularies for the
Global Heat Flow Database. GFZ Data Services. https://doi.org/10.5880/fidgeo.2026.065

Everyone who has contributed to the vocabularies is listed in
[`CONTRIBUTORS.md`](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/CONTRIBUTORS.md).

## License

The vocabularies, in `vocabularies/` and in every release archive, are licensed under the
[Creative Commons Attribution 4.0 International License](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/LICENSE-CC-BY-4.0).
The script and tests are licensed under the
[MIT License](https://github.com/ihfc-iugg/ihfc-vocabularies/blob/main/LICENSE).
