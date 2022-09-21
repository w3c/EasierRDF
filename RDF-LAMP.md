# RDF-LAMP

This page is for curating a list of free and open source tools --
analogous to the [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29) --
that a new RDF user can easily download and use to build a "typical" RDF
application.  The list is not intended to be exhaustive.  (See [Awesome Semantic Web]() for a broader list.)  Rather it is intended to be a starting point: to include only those tools that would be needed by _most_ RDF applications.
The hope is to eventually bundle these tools into a single, common download, analogous to Red Hat or Ubuntu.

Three "typical" RDF applications are targeted:

* an application that integrates data from multiple data sources having different formats and data models, including a relational database and a JSON data source;
* an application that uses RDF metadata to categorize items in multiple ways, such as products in a catalog; or
* an application that uses inference rules or OWL reasoning to support smarter queries, such as queries of biomedical data.

## Criteria for inclusion
A candidate for inclusion in this list:
* must be [OSI-compliant free and open source software (FOSS)](https://opensource.org/), though the software may be maintained by a commercial company and other versions may not be FOSS;
* must be necessary to implement at least one of the three "typical" applications listed above;
* must be powerful enough to be used for real world applications;
* must be actively supported and used in the RDF community;
* should run on Linux, Windows and Mac OS; and
* should provide the best FOSS choice of tools for what it does, without unnecessarily duplicating functionality that is provided by other tools on this list.

## Generic tools
Tools in this section are not specific to the programming language that is used to build
your RDF application.

* [BlazeGraph](https://github.com/blazegraph/database) -- High performance graph database 
* [Protégé](https://protege.stanford.edu/) -- Ontology editor
* (list others here ... )

## Java tools
Tools in this section are for those using Java to build RDF applications.

* [Apache Jena](https://jena.apache.org/download/index.cgi) -- Java framework and library for building RDF applications
* (list others here ... )

## JavaScript tools
Tools in this section are for those using JavaScript to build RDF applications.

* [RDF JS](https://rdf.js.org/) -- JavaScript library for building RDF applications.
* (list others here ... )

## Python tools
Tools in this section are for those using Python to build RDF applications.

* [RDFLib](https://pypi.org/project/rdflib/) -- Python library for RDF applications.
* (list others here ... )

