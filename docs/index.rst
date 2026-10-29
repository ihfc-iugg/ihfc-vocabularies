IHFC Controlled Vocabularies
============================

The IHFC Controlled Vocabularies are the controlled terms the International Heat Flow
Commission (IHFC) maintains for the Global Heat Flow Database (GHFDB) and related heat-flow
data products. They set the permitted values for the metadata fields used when heat-flow data
are submitted, validated, assessed for quality and published: the method used to calculate a
heat-flow value, the probe and exploration context, the geographic setting, the type of
temperature measurement and its corrections, and the thermal conductivity parameters.

Each vocabulary is a SKOS concept scheme. Every vocabulary, concept and collection has a URI
under ``https://w3id.org/ihfc/vocabularies/`` and a page on this site, with its RDF in
Turtle, JSON-LD, RDF/XML and N-Triples beside it. The vocabularies are released under the
`Creative Commons Attribution 4.0 International licence
<https://creativecommons.org/licenses/by/4.0/>`_.

The source files, the release downloads and the changelog are in the `GitHub repository
<https://github.com/ihfc-iugg/ihfc-vocabularies>`_.

.. toctree::
   :caption: Vocabularies
   :maxdepth: 1

   conductivity-conditions
   conductivity-location
   conductivity-methods
   conductivity-pt-function
   conductivity-saturation
   conductivity-sources
   conductivity-strategy
   exploration-methods
   exploration-purpose
   geographic-environments
   heat-flow-corrections
   heat-flow-method
   heat-flow-probes
   temperature-corrections
   temperature-method

.. toctree::
   :caption: How-to guides
   :maxdepth: 1

   how-to/index
