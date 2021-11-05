# EasierRDF

_This repository is for experimental/exploratory work on making RDF easier to use, with the goal of making it easy enough for most developers.  By "RDF" we mean the whole RDF ecosystem -- including SPARQL, OWL, tools, standards, educational materials, etc. -- everything that a developer touches when using RDF.  Our plan:_
* _focus and coordinate community efforts;_
* _build on existing standards whenever possible;_
* _launch additional W3C Community Groups to tackle specific areas of need, including_
  * _[n3-dev Community Group](https://www.w3.org/community/n3-dev/), for standardizing N3 rules; and_
* _contribute to (and benefit from) related efforts, such as the [W3C Graph Data Workshop](https://www.w3.org/Data/events/data-ws-2019/cfp.html) in March 2019, which prepare the path for launching new standards work at W3C._

## Introduction

The value of RDF for graph data has been well proven, in many applications, over the 20+ years since it was first created.  However, difficulty of use has caused RDF to be categorized as a niche technology. This is unfortunate because it limits uptake and prevents RDF from being viewed as a viable choice for many use cases that would otherwise be an excellent fit.

This work seeks to build upon our experience with RDF to examine how we can make it easier to use.  What aspects or gaps have caused difficulty?    How can RDF better support features that users commonly need and other graph databases offer?  How can we make RDF -- or a successor -- easy enough for most developers?

At the same time, businesses are now showing a rapidly growing interest in graph data.  Businesses have used relational databases for many years, but it is costly to adapt database schema and applications in response to evolving application needs.  Other graph and NoSQL databases have emerged to help meet this need.  Unfortunately, there is a lack of interoperability across existing graph data solutions, motivating [interest in open standards for an interchange framework](https://www.w3.org/Data/events/data-ws-2019/cfp.html).  RDF is an appealing vendor neutral framework for graph data, and is well positioned to take on the role of an interchange framework.  Although this interest in RDF as a graph interchange framework arose independently from the effort to make RDF easier, and has different goals, there is a natural overlap in motivation, and both efforts can benefit each other.

## Guiding principles

**1. The goal is to make RDF -- or some RDF-based successor -- easy enough for most developers, who are new to RDF, to be consistently successful.**

**2. Solutions may involve anything in the RDF ecosystem: standards, tools, guidance, etc.  All options are on the table.**

**3. Backward compatibility is highly desirable, but *less* important than ease of use.**

## How to contribute?

We welcome contributions. A good place to start is to review the [issues list](https://github.com/w3c/EasierRDF/issues), categorized below. Please feel free to start a new issue if none of the existing ones are a good match. You can also send comments to the mailing list: [semantic-web@w3.org](https://lists.w3.org/Archives/Public/semantic-web/).

## Intellectual property rights

This work is being performed under the [W3C rdf-dev Community Group](https://www.w3.org/community/rdf-dev/) and is subject to the [W3C Community Contributor License Agreement (CLA)](https://www.w3.org/community/about/agreements/cla/).

# Issue topics

Issues and ideas are recorded in our [issues list](https://github.com/w3c/EasierRDF/issues) and divided into the categories below using [issue labels](https://github.com/w3c/EasierRDF/labels).  The lists below are *not* auto-populated, so click on the category name below to see the latest list.  A [script is available](https://github.com/w3c/EasierRDF/blob/master/src/GetEasierRdfIssuesByCategory.py) for regenerating this list, but it currently must be run manually.

## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories
<!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->
* [Issue 68: Idea: Record stronger alternative definitions of ease](https://github.com/w3c/EasierRDF/issues/68)
* [Issue 34: Idea: Higher-level RDF language](https://github.com/w3c/EasierRDF/issues/34)
* [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)
* [Issue 32: Idea: Build JavaScript libraries that work in the browser](https://github.com/w3c/EasierRDF/issues/32)
* [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)
* [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)
<!-- END_DO_NOT_EDIT! Category: big ideas -->

## [Category: tools](https://github.com/w3c/EasierRDF/labels/Category%3A%20tools): For RDF tools
<!-- BEGIN_DO_NOT_EDIT! Category: tools -->
* [Issue 53: Lack of good forms-based end-user editor](https://github.com/w3c/EasierRDF/issues/53)
* [Issue 52: Transparently merge rdf: and rdfs: namespaces](https://github.com/w3c/EasierRDF/issues/52)
* [Issue 43: Nobody knows who does what with what](https://github.com/w3c/EasierRDF/issues/43)
* [Issue 40: Spoggy easy create & read graphs](https://github.com/w3c/EasierRDF/issues/40)
* [Issue 39: SPARQL Triplestore and Reasoning Performance](https://github.com/w3c/EasierRDF/issues/39)
* [Issue 38: Lack of Full OWL2 Support in Triplestores](https://github.com/w3c/EasierRDF/issues/38)
* [Issue 37: Lack of RDF Visualisation Software](https://github.com/w3c/EasierRDF/issues/37)
* [Issue 35: Lack of a Good Editor](https://github.com/w3c/EasierRDF/issues/35)
* [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)
* [Issue 5: Moribundity of Tools](https://github.com/w3c/EasierRDF/issues/5)
* [Issue 4: Overview of an RDF triple store](https://github.com/w3c/EasierRDF/issues/4)
* [Issue 3: Lack of automated feedback / validation](https://github.com/w3c/EasierRDF/issues/3)
* [Issue 2: Tools are scattered](https://github.com/w3c/EasierRDF/issues/2)
<!-- END_DO_NOT_EDIT! Category: tools -->

## [Category: education](https://github.com/w3c/EasierRDF/labels/Category%3A%20education): For documentation and education
<!-- BEGIN_DO_NOT_EDIT! Category: education -->
* [Issue 59: Reduce the jargon](https://github.com/w3c/EasierRDF/issues/59)
* [Issue 58: Confusion between RDF and Linked Data](https://github.com/w3c/EasierRDF/issues/58)
* [Issue 49: Popular use cases for graph data](https://github.com/w3c/EasierRDF/issues/49)
* [Issue 41: Idea: Material to be put in an undergraduate DB or WebDev unit](https://github.com/w3c/EasierRDF/issues/41)
* [Issue 11: Rejection of SQL and OO as Metaphors](https://github.com/w3c/EasierRDF/issues/11)
* [Issue 10: Lack of a Canonical Example](https://github.com/w3c/EasierRDF/issues/10)
* [Issue 9: Lack of Technology Framing](https://github.com/w3c/EasierRDF/issues/9)
* [Issue 8: Beginner friendly support](https://github.com/w3c/EasierRDF/issues/8)
* [Issue 7: Beginner friendly tutorials / documentation](https://github.com/w3c/EasierRDF/issues/7)
* [Issue 6: No clear entry point](https://github.com/w3c/EasierRDF/issues/6)
<!-- END_DO_NOT_EDIT! Category: education -->

## [Category: usage](https://github.com/w3c/EasierRDF/labels/Category%3A%20usage): For issues around RDF usage in practice
<!-- BEGIN_DO_NOT_EDIT! Category: usage -->
* [Issue 66: Dereferencing RDF, RDFS & OWL in a browser should return human-friendly versions](https://github.com/w3c/EasierRDF/issues/66)
* [Issue 65: Do not use anonymous classes](https://github.com/w3c/EasierRDF/issues/65)
* [Issue 43: Nobody knows who does what with what](https://github.com/w3c/EasierRDF/issues/43)
* [Issue 16: Easier-to-use competitors](https://github.com/w3c/EasierRDF/issues/16)
* [Issue 15: Define an easier profile of RDF](https://github.com/w3c/EasierRDF/issues/15)
* [Issue 14: Namespaces are lost in the RDF model](https://github.com/w3c/EasierRDF/issues/14)
* [Issue 13: Namespace proliferation](https://github.com/w3c/EasierRDF/issues/13)
* [Issue 12: IRI allocation](https://github.com/w3c/EasierRDF/issues/12)
<!-- END_DO_NOT_EDIT! Category: usage -->

## [Category: language features](https://github.com/w3c/EasierRDF/labels/Category%3A%20language%20features): For language features of RDF itself -- model and syntax
<!-- BEGIN_DO_NOT_EDIT! Category: language features -->
* [Issue 62: Retain relative URIs at the RDF model level](https://github.com/w3c/EasierRDF/issues/62)
* [Issue 61: Simplified Reification](https://github.com/w3c/EasierRDF/issues/61)
* [Issue 57: Composition of named graphs](https://github.com/w3c/EasierRDF/issues/57)
* [Issue 52: Transparently merge rdf: and rdfs: namespaces](https://github.com/w3c/EasierRDF/issues/52)
* [Issue 51: Relationship to the Web of Things](https://github.com/w3c/EasierRDF/issues/51)
* [Issue 48: Different kinds of identifiers](https://github.com/w3c/EasierRDF/issues/48)
* [Issue 45: Property Graphs](https://github.com/w3c/EasierRDF/issues/45)
* [Issue 42: Maybe "datatype" should be in the RDF Graph explicitly](https://github.com/w3c/EasierRDF/issues/42)
* [Issue 25: Vocabulary for new semantic extensions](https://github.com/w3c/EasierRDF/issues/25)
* [Issue 24: Decouple semantics from data model](https://github.com/w3c/EasierRDF/issues/24)
* [Issue 22: Language-tagged strings](https://github.com/w3c/EasierRDF/issues/22)
* [Issue 21: Literals as subjects](https://github.com/w3c/EasierRDF/issues/21)
* [Issue 20: Standardized n-ary relations (and property graphs)](https://github.com/w3c/EasierRDF/issues/20)
* [Issue 19: Blank nodes](https://github.com/w3c/EasierRDF/issues/19)
* [Issue 17: IRI reuse and synonyms](https://github.com/w3c/EasierRDF/issues/17)
<!-- END_DO_NOT_EDIT! Category: language features -->

## [Category: related standards](https://github.com/w3c/EasierRDF/labels/Category%3A%20related%20standards): For RDF-related standards
<!-- BEGIN_DO_NOT_EDIT! Category: related standards -->
* [Issue 64: Mappings between shape languages](https://github.com/w3c/EasierRDF/issues/64)
* [Issue 60: transparently switch between CWA and OWA](https://github.com/w3c/EasierRDF/issues/60)
* [Issue 29: No standard way to map a JSON predicate to a URI](https://github.com/w3c/EasierRDF/issues/29)
* [Issue 27: Lack of a standard rules language](https://github.com/w3c/EasierRDF/issues/27)
* [Issue 26: Lack of standard RDF canonicalization](https://github.com/w3c/EasierRDF/issues/26)
<!-- END_DO_NOT_EDIT! Category: related standards -->


## [Category: easier profile](https://github.com/w3c/EasierRDF/labels/Category%3A%20easier%20profile): For candidate features of an easier profile of RDF
<!-- BEGIN_DO_NOT_EDIT! Category: easier profile -->
* [Issue 56: OWL is too hard](https://github.com/w3c/EasierRDF/issues/56)
* [Issue 50: Profile: Exactly one type per representation of a resource](https://github.com/w3c/EasierRDF/issues/50)
<!-- END_DO_NOT_EDIT! Category: easier profile -->


## [Category: experiments](https://github.com/w3c/EasierRDF/labels/Category%3A%20experiments): For demonstrations exploring the design space
<!-- BEGIN_DO_NOT_EDIT! Category: experiments -->
* [Issue 71: Chunks and Chunk Rules](https://github.com/w3c/EasierRDF/issues/71)
* [Issue 70: Graph traversal automata for RDF queries](https://github.com/w3c/EasierRDF/issues/70)
* [Issue 69: Pattern based queries](https://github.com/w3c/EasierRDF/issues/69)
<!-- END_DO_NOT_EDIT! Category: experiments -->

## Uncategorized
[Search](https://github.com/w3c/EasierRDF/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+no%3Alabel) for issues with no category label.

