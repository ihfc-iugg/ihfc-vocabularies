IHFC Controlled Vocabularies
============================

The IHFC Controlled Vocabularies are the controlled terms the International Heat Flow
Commission (IHFC) maintains for the Global Heat Flow Database (GHFDB) and related heat-flow
data products. They set the permitted values for the metadata fields used when heat-flow data
are submitted, validated, assessed for quality and published: the method used to calculate a
heat-flow value, the probe and exploration context, the geographic setting, the type of
temperature measurement and its corrections, and the thermal conductivity parameters.

Each vocabulary is a SKOS concept scheme. Every vocabulary, concept and collection has a URI
under ``https://w3id.org/ihfc-iugg/vocabularies/`` and a page on this site, with its RDF in
Turtle, JSON-LD, RDF/XML and N-Triples beside it. The vocabularies are released under the
`Creative Commons Attribution 4.0 International licence
<https://creativecommons.org/licenses/by/4.0/>`_.

The source files, the release downloads and the changelog are in the `GitHub repository
<https://github.com/ihfc-iugg/controlled-vocabularies>`_.

How to cite
-----------
Cite the vocabularies when your data, software or paper uses their terms. The licence,
CC BY 4.0, asks for credit wherever the vocabularies are reused.

1. Find the version you used. Versions are the `releases
   <https://github.com/ihfc-iugg/controlled-vocabularies/releases>`_ of the repository, numbered
   ``<year>.<release>``, such as ``2026.1``.

2. Cite the data publication, and give the version you used:

   .. code-block:: text

      Jennings, S., Neumann, F., Norden, B., Balkan-Pazvantoğlu, E., Elbarbary, S.,
      Petrunin, A. G., Elger, K., and Fuchs, S. (2026). IHFC Controlled Vocabularies for the
      Global Heat Flow Database, version 2026.1. GFZ Data Services.
      https://doi.org/10.5880/fidgeo.2026.065

3. To point at one vocabulary or one concept, give its URI as well. The URI never changes,
   and a withdrawn concept keeps its page, so the reference keeps resolving:

   .. code-block:: text

      https://w3id.org/ihfc-iugg/vocabularies/heat-flow-method
      https://w3id.org/ihfc-iugg/vocabularies/heat-flow-method/bullard

.. toctree::
   :hidden:

   Home <self>
   catalogue/index
