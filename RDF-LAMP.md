# RDF-LAMP

This page is for curating a list of free and open source tools --
analogous to the [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29) --
that a new RDF user can easily download and use to build a "typical" RDF
application.  The list is not intended to be exhaustive.  (See [Awesome Semantic Web]() for a broader list.)  Rather it is intended to be a starting point: to include only those tools that would be needed by _most_ RDF applications.
The hope is to eventually bundle these tools into a single, common download, analogous to Red Hat or Ubuntu.

## Target applications
Three "typical" RDF applications are targeted:

* **Data integration.** The application must integrate data from multiple data sources having different formats and data models, including a relational database and a (plain) JSON data source.  Challenges should include:
** Data model and vocabulary alignment, using inference rules or some other mechanism.
** Conversion of relational data to RDF
** Conversion of plain JSON data -- not already JSON-LD -- to RDF
** SPARQL queries
** (What else?)
* **Catalog metadata.** The application must use RDF metadata to categorize items in multiple ways, such as products in a catalog.  Challenges should include:
** Use of SKOS for metadata
** Metadata originates in a spreadsheet
** SPARQL queries
** (What else?)
* **OWL for smarter queries.** The application must use OWL reasoning or other inference rules to enable smarter queries, such as queries of biomedical data.  Challenges should include:
** Ontology authoring
** SPARQL queries
** (What else?)

**TO DO:** _Get specific examples for the above three kinds of application, with example data, and turn them into tutorials based on the below set of tools.   (Can someone suggest some, complete with example data?  Or suggest others?)_

## Criteria for inclusion
A candidate for inclusion in this list:
* must be [OSI-compliant free and open source software (FOSS)](https://opensource.org/), though the software may be maintained by a commercial company and other versions may not be FOSS;
* must be necessary to implement at least one of the three "typical" applications listed above;
* must be powerful enough to be used for real world applications;
* must be actively supported and used in the RDF community;
* should run on Linux, Windows and Mac OS; and
* should represent the most popular choice of tools for what it does, without unnecessarily duplicating functionality that is provided by other tools on this list.

## Generic tools
Tools in this section are not specific to the programming language that is used to build
your RDF application.

* [BlazeGraph](https://github.com/blazegraph/database)? -- Graph database 
* [Protégé](https://protege.stanford.edu/) -- Ontology editor
* [SKOS Play](https://skos-play.sparna.fr/play/about)? -- Converts a spreadsheet taxonomy to SKOS data
* (What for RDF authoring?)
* (What for converting from relational data to triples?)
* (What for converting from JSON data to triples (assuming it is not already JSON-LD)?)
* (What for writing and applying simple inference rules)
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

## Ruby tools
Tools in this section are for those using Ruby to build RDF applications.

* [Ruby-RDF](https://github.com/ruby-rdf/linkeddata)

