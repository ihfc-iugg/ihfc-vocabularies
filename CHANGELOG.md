# Changelog

All notable changes to the vocabularies are recorded here. Versions are calendar versions,
`<year>.<release>`.

## [Unreleased]

### Changed

- The vocabularies now match the ones the Global Heat Flow Database portal uses, and the files
  in `vocabularies/` are edited directly. The Python code that generated them is gone.
- Concept addresses use a slash before the identifier
  (`https://heatflow.world/vocabularies/heat-flow-method/bullard`), and several vocabularies take
  the names the portal uses (`heat-flow-probes`, `geographic-environments`,
  `conductivity-sources`, `conductivity-methods`, `conductivity-conditions`,
  `heat-flow-corrections`, `exploration-methods`, `temperature-corrections`).
- Every concept now names its vocabulary (`skos:inScheme`), and every vocabulary lists its top
  concepts.
- The onshore geographic environments and the generic correction flags each named a concept that
  does not exist. They now name `onshore_marine` and `not_recognized`.

### Added

- Exports in RDF/XML, JSON-LD and N-Triples under `data/`.
- Checks that run on every pull request.

### Removed

- The transfer mechanism vocabulary, which the portal no longer uses.
- Empty definitions. 149 concepts have no definition yet.
