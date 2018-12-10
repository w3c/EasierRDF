# EasierRDF

_This repository is for experimental/exploratory work on making RDF easier to use, with the goal of making it easy enough for *average* developers (middle 33% of ability).  By "RDF" we mean the whole RDF ecosystem -- including SPARQL, OWL, tools, standards, educational materials, etc. -- everything that a developer touches when using RDF.  Our plan:_
* _focus and coordinate community efforts;_
* _collect and review ideas for discussion at the [W3C Graph Data Workshop](https://www.w3.org/Data/events/data-ws-2019/cfp.html) in March 2019, and prepare the path for launching new standards work at W3C; and_
* _launch additional W3C Community Groups to tackle specific areas of need, including:_
  * _[n3-dev Community Group](https://www.w3.org/community/n3-dev/), for standardizing N3 rules._

## Introduction

Businesses have used relational databases for many years, but it is costly to adapt database schema and applications in response to evolving application needs. We've seen the emergence of NoSQL databases, e.g. CouchDB for keyed access to JSON. There is a need for fine grained links between data, and this is driving rapid growth of interest in graph data.  Unfortunately, there is a lack of interoperability across existing graph data solutions, motivating interest in open standards for an interchange framework. 

RDF is an appealing vendor neutral framework for graph data, and is well positioned to take on the role of an interchange framework as well as being a flexible data/metadata framework in its own right.  The value of RDF has been well proven, in many applications, over the 20+ years since it was first created.  However, difficulty of use has caused RDF to be categorized as a niche technology. This is unfortunate because it limits uptake and prevents RDF from being a viable choice for many use cases that would otherwise be an excellent fit.

This work seeks to build upon our experience with RDF to examine how we can make it easier to use.  What aspects or gaps have caused difficulty?  How can we make RDF -- or a successor -- easy enough for *average* developers?  For more background, see the [email thread](https://lists.w3.org/Archives/Public/semantic-web/2018Nov/0036.html) that led to this effort.

## Guiding principles

**1. The goal is to make RDF -- or some RDF-based successor -- easy enough for *average* developers (middle 33%), who are new to RDF, to be consistently successful.**

**2. Solutions may involve anything in the RDF ecosystem: standards, tools, guidance, etc.  All options are on the table.**

**3. Backward compatibility is highly desirable, but *less* important than ease of use.**

## How to contribute?

We welcome contributions. A good place to start is to review the [issues list](https://github.com/w3c/EasierRDF/issues), categorized below. Please feel free to start a new issue if none of the existing ones are a good match. We also welcome longer position papers and analyses, preferably in the GitHub markdown format.  You can also send comments to the mailing list: [semantic-web@w3.org](https://lists.w3.org/Archives/Public/semantic-web/).

## Intellectual property rights

This work is being performed under the [W3C rdf-dev Community Group](https://www.w3.org/community/rdf-dev/) and is subject to the [W3C Community Contributor License Agreement (CLA)](https://www.w3.org/community/about/agreements/cla/).

# Issue topics

Issues and ideas are recorded in our [issues list](https://github.com/w3c/EasierRDF/issues) and divided into the categories below using [issue labels](https://github.com/w3c/EasierRDF/labels).  The lists below are *not* auto-populated, so click on the category name below to see the latest list.

## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories
<!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->
* [Issue 34: Idea: Higher-level RDF language](https://github.com/w3c/EasierRDF/issues/34)
* [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)
* [Issue 32: Idea: Build JavaScript libraries that work in the browser](https://github.com/w3c/EasierRDF/issues/32)
* [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)
* [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)
<!-- END_DO_NOT_EDIT! Category: big ideas -->

## [Category: tools](https://github.com/w3c/EasierRDF/labels/Category%3A%20tools): For RDF tools
<!-- BEGIN_DO_NOT_EDIT! Category: tools -->
* [Issue 5: Moribundity of Tools](https://github.com/w3c/EasierRDF/issues/5)
* [Issue 4: Overview of an RDF triple store](https://github.com/w3c/EasierRDF/issues/4)
* [Issue 3: Lack of automated feedback / validation](https://github.com/w3c/EasierRDF/issues/3)
* [Issue 2: Tools are scattered](https://github.com/w3c/EasierRDF/issues/2)
<!-- END_DO_NOT_EDIT! Category: tools -->

## [Category: education](https://github.com/w3c/EasierRDF/labels/Category%3A%20education): For documentation and education
<!-- BEGIN_DO_NOT_EDIT! Category: education -->
* [Issue 11: Rejection of SQL and OO as Metaphors](https://github.com/w3c/EasierRDF/issues/11)
* [Issue 10: Lack of a Canonical Example](https://github.com/w3c/EasierRDF/issues/10)
* [Issue 9: Lack of Technology Framing](https://github.com/w3c/EasierRDF/issues/9)
* [Issue 8: Beginner friendly support](https://github.com/w3c/EasierRDF/issues/8)
* [Issue 7: Beginner friendly tutorials / documentation](https://github.com/w3c/EasierRDF/issues/7)
* [Issue 6: No clear entry point](https://github.com/w3c/EasierRDF/issues/6)
<!-- END_DO_NOT_EDIT! Category: education -->

## [Category: usage](https://github.com/w3c/EasierRDF/labels/Category%3A%20usage): For issues around RDF usage in practice
<!-- BEGIN_DO_NOT_EDIT! Category: usage -->
* [Issue 16: Easier-to-use competitors](https://github.com/w3c/EasierRDF/issues/16)
* [Issue 15: Define an easier profile of RDF](https://github.com/w3c/EasierRDF/issues/15)
* [Issue 14: Namespaces are lost in the RDF model](https://github.com/w3c/EasierRDF/issues/14)
* [Issue 13: Namespace proliferation](https://github.com/w3c/EasierRDF/issues/13)
* [Issue 12: IRI allocation](https://github.com/w3c/EasierRDF/issues/12)
<!-- END_DO_NOT_EDIT! Category: usage -->

## [Category: language features](https://github.com/w3c/EasierRDF/labels/Category%3A%20language%20features): For language features of RDF itself -- model and syntax
<!-- BEGIN_DO_NOT_EDIT! Category: language features -->
* [Issue 25: Vocabulary for new semantic extensions](https://github.com/w3c/EasierRDF/issues/25)
* [Issue 24: Decouple semantics from data model](https://github.com/w3c/EasierRDF/issues/24)
* [Issue 23: Working with named graphs gets complicated fast](https://github.com/w3c/EasierRDF/issues/23)
* [Issue 22: Language-tagged strings](https://github.com/w3c/EasierRDF/issues/22)
* [Issue 21: Literals as subjects](https://github.com/w3c/EasierRDF/issues/21)
* [Issue 20: Standardized n-ary relations (and property graphs)](https://github.com/w3c/EasierRDF/issues/20)
* [Issue 19: Blank nodes](https://github.com/w3c/EasierRDF/issues/19)
* [Issue 18: SPARQL-friendly lists](https://github.com/w3c/EasierRDF/issues/18)
* [Issue 17: IRI reuse and synonyms](https://github.com/w3c/EasierRDF/issues/17)
<!-- END_DO_NOT_EDIT! Category: language features -->

## [Category: related standards](https://github.com/w3c/EasierRDF/labels/Category%3A%20related%20standards): For RDF-related standards
<!-- BEGIN_DO_NOT_EDIT! Category: related standards -->
* [Issue 29: No standard way to map a JSON predicate to a URI](https://github.com/w3c/EasierRDF/issues/29)
* [Issue 28: Named solution sets in SPARQL](https://github.com/w3c/EasierRDF/issues/28)
* [Issue 27: Lack of a standard rules language](https://github.com/w3c/EasierRDF/issues/27)
* [Issue 26: Lack of standard RDF canonicalization](https://github.com/w3c/EasierRDF/issues/26)
<!-- END_DO_NOT_EDIT! Category: related standards -->

## Uncategorized
[Search](https://github.com/w3c/EasierRDF/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+no%3Alabel) for issues with no category label.





