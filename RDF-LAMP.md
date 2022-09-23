# RDF-LAMP

This page is for curating a list of free and open source tools and libraries -- analogous to the [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29) -- that a new RDF user can easily download and use to build a "typical" RDF application.  It addresses [issue #2](https://github.com/w3c/EasierRDF/issues/2).  This list is not intended to be exhaustive.  (See [Awesome Semantic Web](https://github.com/semantalytics/awesome-semantic-web) for a more comprehensive list.)  Rather it is intended to be a starting point: to include only those tools and libraries that would be needed by _most_ RDF applications.  The hope is to eventually bundle them into a single, common download, analogous to Red Hat or Ubuntu.

_**PRs are invited!**_

## Target applications
Three "typical" RDF applications are targeted:

* **Data integration.** The application must integrate data from multiple data sources having different formats and data models, including a relational database and a (plain) JSON data source.
* **Catalog metadata.** The application must use RDF metadata to categorize items in multiple ways, such as products in a catalog.
* **OWL for smarter querying.** The application must use OWL reasoning (or other inference rules) to enable smarter queries, such as queries of biomedical data.

One or more of these applications should involve the following challenges:

* Alignment of multiple data models / vocabularies / ontologies. 
* Use of user-defined inference, either using an RDF rules language or whatever programming language is used to build the application.
* Conversion of relational data to RDF.
* Conversion of plain JSON data -- not already JSON-LD -- to RDF.
* Using public RDF data.
* Understanding and visualizing RDF data.
* SPARQL queries.
* Use of SKOS for metadata.
* Metadata vocabulary that originates in a spreadsheet.
* Conversion of RDF data:
  * from RDF/XML or Turtle to Turtle or N-Triples; 
  * from JSON-LD or TriG to N-Quads;
  * from N-Quads to human-friendly TriG, using common RDF namespace prefixes.
* (What else?)

**TO DO:** _Find or create specific examples for the above three kinds of application, with example data, and turn them into tutorials based on the below set of tools.   (Can someone suggest some, complete with example data?  Or suggest others, perhaps some existing tutorials?)_

## Criteria for inclusion
To be considered for inclusion, a candidate tool or library:
* must be [OSI-compliant free and open source software (FOSS)](https://opensource.org/), though the software may be maintained by a commercial company and it may also be offered under a non-FOSS license;
* must be compliant with W3C standards, especially RDF 1.1, SPARQL 1.1 and JSON-LD 1.1;
* must be necessary (or normally recommended) to implement at least one of the three "typical" applications listed above;
* must be powerful enough to be used for real world applications (in its FOSS version);
* must be actively supported and used in the RDF community;
* should run on Linux, Windows and Mac OS; and
* should represent the easiest and most popular community choice in its category.
* should represent the easiest within its tool category, to get started and use (i.e., usability, documentation, active community forum, stability, etc.)

## Candidate Tools and Libraries

### Generic tools
Tools in this section are not specific to the programming language that is used to build your RDF application.

* One of:
  * [Virtuoso Open Source](https://github.com/openlink/virtuoso-opensource/) -- RDF database
  * [RDF4J](https://www.rdf4j.org/)-- RDF database
  * [Apache Jena](https://jena.apache.org/)-- RDF database
  * [Oxigraph](https://github.com/oxigraph/oxigraph)-- RDF database
* [Protege](https://protege.stanford.edu) -- Ontology editor
* [rapper -- Raptor RDF parsing and serializing utility](https://librdf.org/raptor/rapper.html) -- Validates and converts different RDF serialization formats
* [SKOS Play](https://skos-play.sparna.fr/play/about)? -- Converts a spreadsheet taxonomy to SKOS data
* [YASGUI](https://triply.cc/docs/yasgui) -- SPARQL editor 
* [OpenRefine](https://openrefine.org/) -- Clean data and convert to RDF
* One of:
  * [OpenLink Structured Data Sniffer](https://github.com/OpenLinkSoftware/OSDS_extension) -- View RDF in web pages
  * [RDF Browser](https://addons.mozilla.org/en-US/firefox/addon/rdf-browser/) -- View RDF in web pages
* (What for RDF authoring?)
* (What for visualizing RDF data?)
* One of:
  * [Tarql](http://tarql.github.io/) -- convert CSV files to RDF
  * [R2RML Parser](https://github.com/nkons/r2rml-parser) -- export relational database contents as RDF
* (What for converting from JSON data to triples (assuming it is not already JSON-LD)?)
* (What for writing and applying simple inference rules)
* (list others here ... )

### Java libraries
Libraries in this section are for those using Java to build RDF applications.

* [Apache Jena](https://jena.apache.org/download/index.cgi) -- Java framework and library for building RDF applications
* (list others here ... )

### JavaScript libraries
Libraries in this section are for those using JavaScript to build RDF applications.

* [RDF JS](https://rdf.js.org/) -- JavaScript library for building RDF applications.
* (list others here ... )

### Python libraries
Libraries in this section are for those using Python to build RDF applications.

* [RDFLib](https://pypi.org/project/rdflib/) -- Python library for RDF applications.
* (list others here ... )

For a curated list of additional projects specifically for Python, see [semantic-python-overview](https://github.com/pysemtec/semantic-python-overview).

### Ruby libraries
Libraries in this section are for those using Ruby to build RDF applications.

* [Ruby-RDF](https://github.com/ruby-rdf/linkeddata)

### Rust libraries
Libraries in this section are for those using Rust to build RDF applications.

* [Sophia](https://github.com/pchampin/sophia_rs) -- "Linked Data and Semantic Web toolkit", provides in-memory graphs for efficient triple pattern queries.
* [Oxigraph](https://github.com/oxigraph/oxigraph)-- On-disk graph database library.
* [Rio](https://crates.io/crates/rio_turtle/0.6.2) --  Low level Turtle, Trig, N-Triples and N-Quads parsers and serializers.

