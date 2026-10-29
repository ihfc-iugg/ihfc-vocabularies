# Changelog

All notable changes to the vocabularies are recorded here. Versions are calendar versions,
`<year>.<release>`.

## [Unreleased]

### Changed

- Addresses start with `https://w3id.org/ihfc/vocabularies/`, a permanent address that does
  not depend on where the vocabularies are hosted
  (`https://w3id.org/ihfc/vocabularies/heat-flow-method/bullard`). The identifiers after it
  are unchanged.

### Added

- A documentation site, with a page for every vocabulary, concept and collection, and its
  RDF in every format beside it.

- `CONTRIBUTORS.md`, listing everyone who has contributed to the vocabularies with their
  affiliation and ORCID iD.
- A release archive, `vocabularies-full.zip`, with every vocabulary in every format,
  the README, contributors, changelog and licence.

## [2026.1] - 2026-10-27

### Changed

- The vocabularies now match the ones the Global Heat Flow Database portal uses, and the files
  in `vocabularies/` are edited directly. The Python code that generated them is gone.
- Addresses start with `https://portal.heatflow.world/vocabularies/`, where the portal serves
  the vocabularies, and use a slash before the identifier
  (`https://portal.heatflow.world/vocabularies/heat-flow-method/bullard`). Several vocabularies take
  the names the portal uses (`heat-flow-probes`, `geographic-environments`,
  `conductivity-sources`, `conductivity-methods`, `conductivity-conditions`,
  `heat-flow-corrections`, `exploration-methods`, `temperature-corrections`).
- Every vocabulary has an English label and a `dcterms:description`. The descriptions taken
  from the portal were corrected for grammar and checked against the concepts they cover.
- Every vocabulary names its creator (the International Heat Flow Commission), its publisher
  (GFZ Helmholtz Centre for Geosciences), its licence, its language, the publications its values
  come from, the data publication it belongs to
  (https://doi.org/10.5880/fidgeo.2026.065), and the Global Heat Flow Database fields that use it.
- Every concept now names its vocabulary (`skos:inScheme`), and every vocabulary lists its top
  concepts.
- The onshore geographic environments and the correction flags each named a concept that
  does not exist. They now name `onshore_marine` and `not_recognized`.

### Added

- Definitions for every concept in the thermal conductivity vocabularies, citations and DOIs for the published pressure and temperature corrections, and the missing members of their collections.
- Definitions, codes, readable labels and links between corrected and uncorrected measurements for every concept in the temperature method and temperature correction vocabularies, and the drill stem test values the 2023 structure lists.
- Definitions, alternative labels and corrected labels for every concept in the heat-flow method, probe type, geographic environment, exploration method, exploration purpose and correction flag vocabularies.
- Each release carries every vocabulary in Turtle, RDF/XML, JSON-LD and N-Triples, each as its
  own file with its own download link.
- Checks that run on every pull request.

### Removed

- The transfer mechanism vocabulary, which the portal no longer uses.
- Empty definitions. 149 concepts have no definition yet.
