# RDF-LAMP

This page is for curating a list of free and open source tools -- analogous to the [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29) -- that a new RDF user can easily download and use to build a "typical" RDF application.  The list is not intended to be exhaustive.  (See [Awesome Semantic Web](https://github.com/semantalytics/awesome-semantic-web) for a more comprehensive list.)  Rather it is intended to be a starting point: to include only those tools that would be needed by _most_ RDF applications.  The hope is to eventually bundle these tools into a single, common download, analogous to Red Hat or Ubuntu.

_**PRs are invited!**_

## Target applications
Three "typical" RDF applications are targeted:

* **Data integration.** The application must integrate data from multiple data sources having different formats and data models, including a relational database and a (plain) JSON data source.
* **Catalog metadata.** The application must use RDF metadata to categorize items in multiple ways, such as products in a catalog.
* **OWL for smarter quering.** The application must use OWL reasoning (or other inference rules) to enable smarter queries, such as queries of biomedical data.

One or more of these applications should involve the following challenges:

* Alignment of multiple data models / vocabularies / ontologies. 
* Use of user-defined inference, either using an RDF rules language or whatever programming language is used to build the application.
* Conversion of relational data to RDF.
* Conversion of plain JSON data -- not already JSON-LD -- to RDF.
* Locating, understanding and visualizing public RDF data.
* SPARQL queries.
* Use of SKOS for metadata.
* Metadata vocabulary that originates in a spreadsheet.
* Conversion of RDF data:
 * from RDF/XML or Turtle to Turtle or N-Triples; 
 * from JSON-LD or TriG to N-Quads;
 * from N-Quads to human-friendly TriG, using common RDF namespace prefixes.
* SPARQL queries.
* (What else?)

**TO DO:** _Get specific examples for the above three kinds of application, with example data, and turn them into tutorials based on the below set of tools.   (Can someone suggest some, complete with example data?  Or suggest others?)_

## Criteria for tool inclusion
To be considered for inclusion, a candidate tool:
* must be [OSI-compliant free and open source software (FOSS)](https://opensource.org/), though the software may be maintained by a commercial company and it may also be offered under a non-FOSS license;
* must be necessary to implement at least one of the three "typical" applications listed above;
* must be powerful enough to be used for real world applications (in its FOSS version);
* must be actively supported and used in the RDF community;
* should run on Linux, Windows and Mac OS; and
* should represent the most popular choice of tools for what it does, without unnecessarily duplicating functionality that is provided by other tools on this list.

## Candidate Tools

### Generic tools
Tools in this section are not specific to the programming language that is used to build your RDF application.

* RDF database (supporting SPARQL 1.1 and named graphs), one of:
 * [Virtuoso Open Source](https://github.com/openlink/virtuoso-opensource/)
 * [RDF4J](https://www.rdf4j.org/)
 * [Apache Jena](https://jena.apache.org/)
* [Protégéhthttps://protege.stanford.edu -- Ontology editor

 * [SKOS Play](https://skos-play.sparna.fr/play/about)? -- Converts a spreadsheet taxonomy to SKOS data
* (What for RDF authoring?)
* (What for converting from relational data to triples?)
* (What for converting from JSON data to triples (assuming it is not already JSON-LD)?)
* (What for writing and applying simple inference rules)
* (list others here ... )

### Java tools
Tools in this section are for those using Java to build RDF applications.

* [Apache Jena](https://jena.apache.org/download/index.cgi) -- Java framework and library for building RDF applications
* (list others here ... )

### JavaScript tools
Tools in this section are for those using JavaScript to build RDF applications.

* [RDF JS](https://rdf.js.org/) -- JavaScript library for building RDF applications.
* (list others here ... )

### Python tools
Tools in this section are for those using Python to build RDF applications.

* [RDFLib](https://pypi.org/project/rdflib/) -- Python library for RDF applications.
* (list others here ... )

For a curated list of additional tools specifically for Python, see [semantic-python-overview](https://github.com/pysemtec/semantic-python-overview).

## Ruby tools
Tools in this section are for those using Ruby to build RDF applications.

* [Ruby-RDF](https://github.com/ruby-rdf/linkeddata)

