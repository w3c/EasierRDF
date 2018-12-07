# EasierRDF

_This repository is for work on making RDF easier to use.  By "RDF" we mean the whole RDF ecosystem -- including SPARQL, OWL, tools, standards, educational materials, etc. -- everything that a developer touches when using RDF.  Approach:_
 - _Focus and coordinate community efforts._
 - _Collect and review ideas for discussion at the [W3C Graph Data Workshop](https://www.w3.org/Data/events/data-ws-2019/cfp.html) in March 2019, and prepare the path for launching new standards work at W3C._
 - _Launch additional W3C Community Groups to tackle specific areas of need.  For example, see the [n3-dev Community Group](https://www.w3.org/community/n3-dev/), which seeks to standardize N3 rules._

## Introduction

The value of RDF has been well proven, in many applications, over the 20+ years since it was first created.  At the same time, a painful reality has emerged: RDF is too hard for
*average* developers.  By "average developers" I mean those
in the middle 33 percent of ability. And by "RDF", I mean the
whole RDF ecosystem -- including SPARQL, OWL, tools, standards,
etc. -- everything that a developer touches when using RDF.

Businesses have used relational databases for many years, but it is costly to adapt database schema and applications in response to evolving application needs. We've seen the emergence of NoSQL databases, e.g. CouchDB for keyed access to JSON. There is a need for fine grained links between data, and this is driving rapid growth of interest in graph data.

Unfortunately, there is a lack of interoperability across existing graph data solutions, motivating interest in open standards for an interchange framework. RDF is an appealing vendor neutral framework for graph data and well positioned to take on the role of an interchange framework as well as being a flexible data/metadata framework in its own right.

It is now timely to build upon two decades of experience with RDF to examine how we can make RDF easier to use, especially as businesses are under pressure to find effective agile solutions for managing information across large numbers of heterogeneous data silos distributed throughout the enterprise. What has worked well? What features have caused friction? How can we best address the needs of different communities?

## Guiding principles

1. The goal is to make RDF -- or some RDF-based successor -- easy enough for *average* developers (middle 33% of ability), who are new to RDF, to be consistently successful.

2. Solutions may involve anything in the RDF ecosystem: standards, tools, guidance, etc.  All options are on the table.

3. Backward compatibility is highly desirable, but **less** important than ease of use.

## How to contribute?

We welcome contributions. A good place to start is to review the collection of issues, see below. Please feel free to start a new issue if none of the existing ones are a good match. We also welcome longer position papers and analyses, preferably in the GitHub markdown format.  You can also send comments to the mailing list: [semantic-web@w3.org](https://lists.w3.org/Archives/Public/semantic-web/).

# Topics

This provides a convient way to group the large number of GitHub issues we're discussing. Note that these provide a means for describing use cases, challenges and proposed solutions.

## Some Big Ideas

* Attracting JavaScript front-end developers
* Basing Linked Data on a JavaScript API
* Build JavaScript libraries that work in the browser
* Build powerful query engines
* Higher-level RDF languages
* RDF Templates
* Accessible and scalable developer tools

## RDF Tools

* Tools are scattered
* LAMP for RDF: establishing a standard bundle available for all common operating systems
* Semantic Web client in a box
* Lack of automated feedback/validation
* Overview of an RDF triple store
* Obvious moribundity of tools

## Documentation and Education

* No clear entry point
* Canonical documentation
* Beginner friendly tutorials/documentation
* Building things
* An integrated primer that spans specifications and tools
* Beginner friendly support
* Lack of technology framing
* Lack of a canonical example
* Rejection of SQL and Object-Orientation as metaphors

## RDF Usage

* IRI allocation - need for clear guidance
* Namespace proliferation
* Define an easier profile of RDF

## RDF Language features

* Making it easier to express property graphs
* IRI reuse and synonyms
* SPARQL friendly lists
* Blank nodes
* Allow expressions as first class entities
* Separate existential quantifier (blank node) logic from RDF
* Add explicit scope mechanism for blank nodes
* Define equality and hash functions on types
* Standardized n-ary relations (and property graphs)
* Nested triples
* Auto-generate a predictable IRI from the object's primary key
* Extend RDF from binary to n-ary
* Literals as subjects
* Graphs as subjects and objects
* Allow literals and blank nodes as predicates too
* Allow blank nodes and literals as graph names
* Language-tagged strings
* Eliminate the special status of language-tagged strings
* Use W3C OntoLex/Lemony as a basis for language tagging
* Use URIs to identify language
* Working with named graphs gets complicated fast
* Nesting and composition of named graphs
* Decouple semantics from data model
* Vocabulary for new semantic extensions

## RDF Related standards

* Lack of standard RDF canonicalization
* JSON-LD canonicalization
* RDF canonicalization
* Lack of a standard rules language
* Embed RDF in a programming language
* Standardize N3 Logic
* Bind custom inference rules to functions
* Update RIF
* SPARQL-Generate extensions
* Named solution sets in SPARQL
* No standard way to map a JSON predicate to a URI

## Original References

To simplify editing, please DO NOT add more references to this list.  These are references from the message that started the discussion about making RDF easier to use:
https://lists.w3.org/Archives/Public/semantic-web/2018Nov/0036.html 

Please add any new references (links) inline with the topics above.  This will make it easier to move text around as we are organizing these topics.

1. "Toward Easier RDF", David Booth, slides from 2018 US
Semantic Technology Symposium:
https://goo.gl/H2vBYi
2. US Semantic Technology Symposium (US2TS):
http://www.us2ts.org/
3. "What happened to the Semantic
Web?" (general comments), Sean Palmer:
https://lists.w3.org/Archives/Public/semantic-web/2017Oct/0024.html
4. "Semantic Web Interest Group now closed",
"RDF(-DEV), back to the future", Dan Brickley:
https://lists.w3.org/Archives/Public/semantic-web/2018Oct/0086.html
https://lists.w3.org/Archives/Public/semantic-web/2018Oct/0052.html
5. "A More Decentralized Vision for Linked Data", Axel Polleres,
Maulik R. Kamdar, Javier D. Fernandez, Tania Tudorache, and
Mark A. Musen: https://openreview.net/pdf?id=H1lS_g81gX
6. "Signing RDF Graphs", Jeremy Carroll
http://www.hpl.hp.com/techreports/2003/HPL-2003-142.pdf
7. "Is it possible to get the position of an element
in an RDF Collection in SPARQL?", see Joshua
Taylor's answer, "A Pure SPARQL 1.1 Solution":
https://stackoverflow.com/questions/17523804/is-it-possible-to-get-the-position-of-an-element-in-an-rdf-collection-in-sparql
8. "An Ordered RDF List", David Wood and James Leigh:
https://www.w3.org/2009/12/rdf-ws/papers/ws14
9. "Defining N-ary Relations on the Semantic Web", W3C Working Group:
https://www.w3.org/TR/swbp-n-aryRelations/
10. Property Graph, Wikipedia:
https://en.wikipedia.org/wiki/Graph_database#Labeled-Property_Graph
11. DB-Engines Ranking of Graph DBMS:
https://db-engines.com/en/ranking/graph+dbms
12. "Standards for storing RDF/OWL in a property graph?", Olaf Hartig:
https://lists.w3.org/Archives/Public/semantic-web/2018Apr/0030.html
13. "SPARQL 1.1 Query Language: CONSTRUCT":
https://www.w3.org/TR/sparql11-query/#construct

1. "What happened to the Semantic
Web?" (SPARQL comments), Sean Palmer:
https://lists.w3.org/Archives/Public/semantic-web/2017Oct/0045.htmlhttps://lists.w3.org/Archives/Public/semantic-web/2017Oct/0059.html
2. "Debunking some 'RDF vs. Property Graph' Alternative Facts",
Jesus Barras, slides 34 and 35:
https://www.slideshare.net/neo4j/graphconnect-europe-2017-debunking-some-rdf-vs-property-graph-alternative-facts-neo4j
3.  "Universal Resource Identifiers: The Opacity Axiom", Tim
Berners-Lee:
https://www.w3.org/DesignIssues/Axioms.html#opaque
4. "Notation3 (N3): A readable RDF syntax", W3C Team Submission,
Tim Berners-Lee and Dan Connolly:
https://www.w3.org/TeamSubmission/n3/

