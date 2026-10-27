# Glossary

The words this repository uses for its own concepts. Issues, pull requests, tests and
documentation use these terms as defined here.

| Term | Definition | Avoid |
| --- | --- | --- |
| **Vocabulary** | One SKOS concept scheme, held in one file under `vocabularies/`. The file name is the last part of the vocabulary's address (`heat-flow-method.ttl` is `https://portal.heatflow.world/vocabularies/heat-flow-method`). | "list", "choices" |
| **Concept** | One entry in a vocabulary (`skos:Concept`). It has a label and, eventually, a definition. | "term", "option", "value" |
| **Collection** | A named group of concepts within one vocabulary (`skos:Collection`), such as the onshore and offshore geographic environments. A collection groups concepts and is not itself one. | "category" |
| **Address** | The URI that identifies a vocabulary, concept or collection. A concept's address is its vocabulary's address, a slash, and its identifier. Once published, an address is permanent. | "URL", "ID" |
| **Identifier** | The last part of a concept's address (`bullard` in `…/heat-flow-method/bullard`). Databases that use these vocabularies store it, so it never changes. | "key", "slug" |
| **Label** | The name of a concept as people read it (`skos:prefLabel`). One per language. | "name", "title" |
| **Description** | The sentence that says what a vocabulary covers (`dcterms:description` on the concept scheme). | "definition", for a vocabulary |
| **Definition** | The sentence that says what a concept means (`skos:definition`). One per language. | "description" |
| **Translation** | A label or definition in a language other than English, stored on the same concept with its language tag (`"Bullard-Methode"@de`). | — |
| **Source file** | A Turtle file in `vocabularies/`. Source files are the only files anyone edits. | "input" |
| **Export** | A copy of a vocabulary in another RDF format, under `data/`. Exports are generated from the source files and never edited by hand. | "build", "output" |
| **Fixed layout** | The exact Turtle text rdflib writes for a vocabulary (its `longturtle` format), with two prefixes: `ihfc:` for `https://portal.heatflow.world/vocabularies/`, so a vocabulary reads `ihfc:heat-flow-method`, and the empty prefix for the vocabulary's own namespace, so its concepts read `:bullard`. Every source file is kept in it, so a diff shows only what changed in meaning. | "formatting" |
