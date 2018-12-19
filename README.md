
Jupyter Notebook
GetEasierRdfIssuesByCategory Last Checkpoint: 12/11/2018 (unsaved changes) Current Kernel Logo

Python 3

    File
    Edit
    View
    Insert
    Cell
    Kernel
    Widgets
    Help

1

'''This is for updating the issues lists in the EasierRDF github repo at https://github.com/w3c/EasierRDF .'''

2

​

3

import urllib.request

4

import urllib.parse

5

import json

6

import re

7

​

8

issuesUrl='https://github.com/w3c/EasierRDF/issues'

9

readmeUrl = 'https://raw.githubusercontent.com/w3c/EasierRDF/master/README.md'

10

​

11

categoryNames = ['Category: big ideas',

12

                'Category: tools',

13

                'Category: education',

14

                'Category: usage',

15

                'Category: language features',

16

                'Category: related standards']

17

​

18

def GetIssuesByLabel(label='Category: big ideas', issuesUrl='https://github.com/w3c/EasierRDF/issues'):

19

    '''See https://stackoverflow.com/questions/41753769/get-all-github-issues-from-repo-with-specific-label'''

20

    url = issuesUrl + "?labels=" + urllib.parse.quote(label)

21

    url = re.sub(r'^https://github\.com/', 'https://api.github.com/repos/', url)

22

    # print(url)

23

    header={'Accept': 'application/json'}

24

    req = urllib.request.Request(url=url, headers=header, method='GET')

25

    issuesJson = urllib.request.urlopen(req).read()

26

    issuesObjects = json.loads(issuesJson.decode("utf-8"))

27

    return issuesObjects

28

​

29

def ObjectToMarkdown(issuesObjects):

30

    issuesMdList = [ '* [Issue {}: {}]({})\n'.format(i['number'], i['title'], i['html_url']) for i in issuesObjects]

31

    issuesMd = "".join(issuesMdList)

32

    return issuesMd

33

​

34

GetIssuesByLabel()

35

​

[{'url': 'https://api.github.com/repos/w3c/EasierRDF/issues/34',
  'repository_url': 'https://api.github.com/repos/w3c/EasierRDF',
  'labels_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/34/labels{/name}',
  'comments_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/34/comments',
  'events_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/34/events',
  'html_url': 'https://github.com/w3c/EasierRDF/issues/34',
  'id': 388876081,
  'node_id': 'MDU6SXNzdWUzODg4NzYwODE=',
  'number': 34,
  'title': 'Idea: Higher-level RDF language',
  'user': {'login': 'dbooth-boston',
   'id': 5123226,
   'node_id': 'MDQ6VXNlcjUxMjMyMjY=',
   'avatar_url': 'https://avatars0.githubusercontent.com/u/5123226?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/dbooth-boston',
   'html_url': 'https://github.com/dbooth-boston',
   'followers_url': 'https://api.github.com/users/dbooth-boston/followers',
   'following_url': 'https://api.github.com/users/dbooth-boston/following{/other_user}',
   'gists_url': 'https://api.github.com/users/dbooth-boston/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/dbooth-boston/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/dbooth-boston/subscriptions',
   'organizations_url': 'https://api.github.com/users/dbooth-boston/orgs',
   'repos_url': 'https://api.github.com/users/dbooth-boston/repos',
   'events_url': 'https://api.github.com/users/dbooth-boston/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/dbooth-boston/received_events',
   'type': 'User',
   'site_admin': False},
  'labels': [{'id': 1154330445,
    'node_id': 'MDU6TGFiZWwxMTU0MzMwNDQ1',
    'url': 'https://api.github.com/repos/w3c/EasierRDF/labels/Category:%20big%20ideas',
    'name': 'Category: big ideas',
    'color': 'efacdc',
    'default': False}],
  'state': 'open',
  'locked': False,
  'assignee': None,
  'assignees': [],
  'milestone': None,
  'comments': 1,
  'created_at': '2018-12-08T02:34:25Z',
  'updated_at': '2018-12-10T13:45:56Z',
  'closed_at': None,
  'author_association': 'COLLABORATOR',
  'body': '"Using RDF is like programming in assembly language.\r\nIt is tedious, frustrating and error prone. Somehow, we\r\nneed to move up to a higher, easier, more productive level."\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Nov/0036.html\r\n\r\n"RDF is deceptively simple. You start with a simple idea and end up with a complex mess."\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Nov/0094.html\r\n\r\n"it may be that it is not so much easier RDF that is needed as time working out how these\r\nparadigms -- [RDF\'s logical , FP\'s algebraic and OOs state based architecture] -- fit together, as we need people from these paradigms to work together"\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Dec/0006.html\r\n\r\n## Ideas for addressing this issue\r\n\r\n### Higher-level RDF language\r\n"What I\'d most like to see is a higher-level RDF language that\r\ngets compiled into triples/quads, just as python gets compiled into byte\r\ncode, such that RDF users never need to actually see or deal with the\r\nunderlying triples."\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Nov/0082.html\r\n\r\n### IDEA: RDF templates\r\n"While you wait for the easier RDF, please try out Reasonable Ontology\r\nTemplates (OTTR). OTTR templates are like macros for RDF."\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Nov/0091.html\r\n\r\n"On my wish list are . . . specific templates for certain types like addresses"\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Nov/0170.html'},
 {'url': 'https://api.github.com/repos/w3c/EasierRDF/issues/33',
  'repository_url': 'https://api.github.com/repos/w3c/EasierRDF',
  'labels_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/33/labels{/name}',
  'comments_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/33/comments',
  'events_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/33/events',
  'html_url': 'https://github.com/w3c/EasierRDF/issues/33',
  'id': 388876006,
  'node_id': 'MDU6SXNzdWUzODg4NzYwMDY=',
  'number': 33,
  'title': 'Idea: Build powerful query engines',
  'user': {'login': 'dbooth-boston',
   'id': 5123226,
   'node_id': 'MDQ6VXNlcjUxMjMyMjY=',
   'avatar_url': 'https://avatars0.githubusercontent.com/u/5123226?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/dbooth-boston',
   'html_url': 'https://github.com/dbooth-boston',
   'followers_url': 'https://api.github.com/users/dbooth-boston/followers',
   'following_url': 'https://api.github.com/users/dbooth-boston/following{/other_user}',
   'gists_url': 'https://api.github.com/users/dbooth-boston/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/dbooth-boston/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/dbooth-boston/subscriptions',
   'organizations_url': 'https://api.github.com/users/dbooth-boston/orgs',
   'repos_url': 'https://api.github.com/users/dbooth-boston/repos',
   'events_url': 'https://api.github.com/users/dbooth-boston/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/dbooth-boston/received_events',
   'type': 'User',
   'site_admin': False},
  'labels': [{'id': 1154330445,
    'node_id': 'MDU6TGFiZWwxMTU0MzMwNDQ1',
    'url': 'https://api.github.com/repos/w3c/EasierRDF/labels/Category:%20big%20ideas',
    'name': 'Category: big ideas',
    'color': 'efacdc',
    'default': False}],
  'state': 'open',
  'locked': False,
  'assignee': None,
  'assignees': [],
  'milestone': None,
  'comments': 0,
  'created_at': '2018-12-08T02:33:42Z',
  'updated_at': '2018-12-08T02:41:27Z',
  'closed_at': None,
  'author_association': 'COLLABORATOR',
  'body': '"build powerful query engines such that app developers do not need to write HTTP requests\r\n(every data access should be a query, read or write)"\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Dec/0009.html'},
 {'url': 'https://api.github.com/repos/w3c/EasierRDF/issues/32',
  'repository_url': 'https://api.github.com/repos/w3c/EasierRDF',
  'labels_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/32/labels{/name}',
  'comments_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/32/comments',
  'events_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/32/events',
  'html_url': 'https://github.com/w3c/EasierRDF/issues/32',
  'id': 388875948,
  'node_id': 'MDU6SXNzdWUzODg4NzU5NDg=',
  'number': 32,
  'title': 'Idea: Build JavaScript libraries that work in the browser',
  'user': {'login': 'dbooth-boston',
   'id': 5123226,
   'node_id': 'MDQ6VXNlcjUxMjMyMjY=',
   'avatar_url': 'https://avatars0.githubusercontent.com/u/5123226?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/dbooth-boston',
   'html_url': 'https://github.com/dbooth-boston',
   'followers_url': 'https://api.github.com/users/dbooth-boston/followers',
   'following_url': 'https://api.github.com/users/dbooth-boston/following{/other_user}',
   'gists_url': 'https://api.github.com/users/dbooth-boston/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/dbooth-boston/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/dbooth-boston/subscriptions',
   'organizations_url': 'https://api.github.com/users/dbooth-boston/orgs',
   'repos_url': 'https://api.github.com/users/dbooth-boston/repos',
   'events_url': 'https://api.github.com/users/dbooth-boston/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/dbooth-boston/received_events',
   'type': 'User',
   'site_admin': False},
  'labels': [{'id': 1154330445,
    'node_id': 'MDU6TGFiZWwxMTU0MzMwNDQ1',
    'url': 'https://api.github.com/repos/w3c/EasierRDF/labels/Category:%20big%20ideas',
    'name': 'Category: big ideas',
    'color': 'efacdc',
    'default': False}],
  'state': 'open',
  'locked': False,
  'assignee': None,
  'assignees': [],
  'milestone': None,
  'comments': 0,
  'created_at': '2018-12-08T02:33:06Z',
  'updated_at': '2018-12-08T02:41:27Z',
  'closed_at': None,
  'author_association': 'COLLABORATOR',
  'body': '"build JavaScript libraries and things that work in the browser"\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Dec/0009.html'},
 {'url': 'https://api.github.com/repos/w3c/EasierRDF/issues/31',
  'repository_url': 'https://api.github.com/repos/w3c/EasierRDF',
  'labels_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/31/labels{/name}',
  'comments_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/31/comments',
  'events_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/31/events',
  'html_url': 'https://github.com/w3c/EasierRDF/issues/31',
  'id': 388875903,
  'node_id': 'MDU6SXNzdWUzODg4NzU5MDM=',
  'number': 31,
  'title': 'Idea: Base Linked Data on a JavaScript API',
  'user': {'login': 'dbooth-boston',
   'id': 5123226,
   'node_id': 'MDQ6VXNlcjUxMjMyMjY=',
   'avatar_url': 'https://avatars0.githubusercontent.com/u/5123226?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/dbooth-boston',
   'html_url': 'https://github.com/dbooth-boston',
   'followers_url': 'https://api.github.com/users/dbooth-boston/followers',
   'following_url': 'https://api.github.com/users/dbooth-boston/following{/other_user}',
   'gists_url': 'https://api.github.com/users/dbooth-boston/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/dbooth-boston/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/dbooth-boston/subscriptions',
   'organizations_url': 'https://api.github.com/users/dbooth-boston/orgs',
   'repos_url': 'https://api.github.com/users/dbooth-boston/repos',
   'events_url': 'https://api.github.com/users/dbooth-boston/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/dbooth-boston/received_events',
   'type': 'User',
   'site_admin': False},
  'labels': [{'id': 1154330445,
    'node_id': 'MDU6TGFiZWwxMTU0MzMwNDQ1',
    'url': 'https://api.github.com/repos/w3c/EasierRDF/labels/Category:%20big%20ideas',
    'name': 'Category: big ideas',
    'color': 'efacdc',
    'default': False}],
  'state': 'open',
  'locked': False,
  'assignee': None,
  'assignees': [],
  'milestone': None,
  'comments': 0,
  'created_at': '2018-12-08T02:32:37Z',
  'updated_at': '2018-12-08T02:41:27Z',
  'closed_at': None,
  'author_association': 'COLLABORATOR',
  'body': '"The interface definitions at https://rdf.js.org/ look promising, and enable literals and blank nodes as the subject of quads. It would be a simple change to define quad as deriving from term so that we can then have quads as the subject or object of other quads, as a basis for property graphs without needing reification. . . . This is incredibly important.\r\nFront-end devs I talked to did not want to work with triples.\r\nBy giving them tools, we enabled them to be enthusiastic about Linked Data."\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Dec/0003.html'},
 {'url': 'https://api.github.com/repos/w3c/EasierRDF/issues/30',
  'repository_url': 'https://api.github.com/repos/w3c/EasierRDF',
  'labels_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/30/labels{/name}',
  'comments_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/30/comments',
  'events_url': 'https://api.github.com/repos/w3c/EasierRDF/issues/30/events',
  'html_url': 'https://github.com/w3c/EasierRDF/issues/30',
  'id': 388875832,
  'node_id': 'MDU6SXNzdWUzODg4NzU4MzI=',
  'number': 30,
  'title': 'Idea: Attract JavaScript front-end developers',
  'user': {'login': 'dbooth-boston',
   'id': 5123226,
   'node_id': 'MDQ6VXNlcjUxMjMyMjY=',
   'avatar_url': 'https://avatars0.githubusercontent.com/u/5123226?v=4',
   'gravatar_id': '',
   'url': 'https://api.github.com/users/dbooth-boston',
   'html_url': 'https://github.com/dbooth-boston',
   'followers_url': 'https://api.github.com/users/dbooth-boston/followers',
   'following_url': 'https://api.github.com/users/dbooth-boston/following{/other_user}',
   'gists_url': 'https://api.github.com/users/dbooth-boston/gists{/gist_id}',
   'starred_url': 'https://api.github.com/users/dbooth-boston/starred{/owner}{/repo}',
   'subscriptions_url': 'https://api.github.com/users/dbooth-boston/subscriptions',
   'organizations_url': 'https://api.github.com/users/dbooth-boston/orgs',
   'repos_url': 'https://api.github.com/users/dbooth-boston/repos',
   'events_url': 'https://api.github.com/users/dbooth-boston/events{/privacy}',
   'received_events_url': 'https://api.github.com/users/dbooth-boston/received_events',
   'type': 'User',
   'site_admin': False},
  'labels': [{'id': 1154330445,
    'node_id': 'MDU6TGFiZWwxMTU0MzMwNDQ1',
    'url': 'https://api.github.com/repos/w3c/EasierRDF/labels/Category:%20big%20ideas',
    'name': 'Category: big ideas',
    'color': 'efacdc',
    'default': False}],
  'state': 'open',
  'locked': False,
  'assignee': None,
  'assignees': [],
  'milestone': None,
  'comments': 0,
  'created_at': '2018-12-08T02:31:47Z',
  'updated_at': '2018-12-08T02:31:47Z',
  'closed_at': None,
  'author_association': 'COLLABORATOR',
  'body': '"front-end developers are a new generation.\r\nThey did not exist back when RDF was conceived. . . .\r\nThey’re using JavaScript, TypeScript, React, etc."\r\nhttps://lists.w3.org/Archives/Public/semantic-web/2018Nov/0050.html'}]

1

def UpdateIssuesList(categoryName, page, issuesUrl='https://github.com/w3c/EasierRDF/issues'):

2

    '''Update the issue list in the given category in the page.  

3

    The rest of the page is unchanged.

4

    The issue list in each category is marked like this:

5

    

6

    ## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories

7

    <!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->

8

    * [Issue 34: Idea: Higher-level RDF language](https://github.com/w3c/EasierRDF/issues/34)

9

    * [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)

10

    * [Issue 32: Idea: Build JavaScript libraries that work in the browser](https://github.com/w3c/EasierRDF/issues/32)

11

    * [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)

12

    * [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)

13

    <!-- END_DO_NOT_EDIT! Category: big ideas -->'''

14

    categoryEncoded = urllib.parse.quote_plus(categoryName)

15

    beginMarker = '<!-- BEGIN_DO_NOT_EDIT! ' + categoryName + ' -->'

16

    endMarker   = '<!-- END_DO_NOT_EDIT! ' + categoryName + ' -->'

17

    beforeMiddleAfter = page.split(beginMarker)

18

    if len(beforeMiddleAfter) != 2:

19

        raise Exception('ERROR: Did not find beginMarker in page: '+beginMarker)

20

    before = beforeMiddleAfter[0]

21

    middleAfter = beforeMiddleAfter[1].split(endMarker)

22

    if len(middleAfter) != 2:

23

        raise Exception('ERROR: Did not find endMarker in page: '+endMarker)

24

    middle = middleAfter[0]

25

    after = middleAfter[1]

26

    issuesList = ObjectToMarkdown(GetIssuesByLabel(categoryName))

27

    page = before + beginMarker + '\n' + issuesList + endMarker + after

28

    return page

29

​

30

​

31

print(ObjectToMarkdown(GetIssuesByLabel('Category: big ideas')))

32

​

33

​

34

​

* [Issue 34: Idea: Higher-level RDF language](https://github.com/w3c/EasierRDF/issues/34)
* [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)
* [Issue 32: Idea: Build JavaScript libraries that work in the browser](https://github.com/w3c/EasierRDF/issues/32)
* [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)
* [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)

1

page = '''    ## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories

2

    <!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->

3

    * [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)

4

    * [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)

5

    <!-- END_DO_NOT_EDIT! Category: big ideas -->'''

6

​

7

print(UpdateIssuesList('Category: big ideas', page, issuesUrl))

8

​

    ## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories
    <!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->
* [Issue 34: Idea: Higher-level RDF language](https://github.com/w3c/EasierRDF/issues/34)
* [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)
* [Issue 32: Idea: Build JavaScript libraries that work in the browser](https://github.com/w3c/EasierRDF/issues/32)
* [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)
* [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)
<!-- END_DO_NOT_EDIT! Category: big ideas -->

1

page = urllib.request.urlopen(readmeUrl).read().decode("utf8")

2

for categoryName in categoryNames:

3

    page = UpdateIssuesList(categoryName, page, issuesUrl)

4

print(page)

5

​

# EasierRDF

_This repository is for experimental/exploratory work on making RDF easier to use, with the goal of making it easy enough for *average* developers (middle 33% of ability).  By "RDF" we mean the whole RDF ecosystem -- including SPARQL, OWL, tools, standards, educational materials, etc. -- everything that a developer touches when using RDF.  Our plan:_
* _focus and coordinate community efforts;_
* _launch additional W3C Community Groups to tackle specific areas of need, including_
  * _[n3-dev Community Group](https://www.w3.org/community/n3-dev/), for standardizing N3 rules; and_
* _contribute to related efforts, such as the [W3C Graph Data Workshop](https://www.w3.org/Data/events/data-ws-2019/cfp.html) in March 2019, which prepare the path for launching new standards work at W3C._

## Introduction

The value of RDF for graph data has been well proven, in many applications, over the 20+ years since it was first created.  However, difficulty of use has caused RDF to be categorized as a niche technology. This is unfortunate because it limits uptake and prevents RDF from being viewed as a viable choice for many use cases that would otherwise be an excellent fit.

This work seeks to build upon our experience with RDF to examine how we can make it easier to use.  What aspects or gaps have caused difficulty?    How can RDF better support features that users commonly need and other graph databases offer?  How can we make RDF -- or a successor -- easy enough for *average* developers?

At the same time, businesses are now showing a rapidly growing interest in graph data.  Businesses have used relational databases for many years, but it is costly to adapt database schema and applications in response to evolving application needs.  Other graph and NoSQL databases have emerged to help meet this need.  Unfortunately, there is a lack of interoperability across existing graph data solutions, motivating [interest in open standards for an interchange framework](https://www.w3.org/Data/events/data-ws-2019/cfp.html).  RDF is an appealing vendor neutral framework for graph data, and is well positioned to take on the role of an interchange framework.  Although this interest in RDF as a graph interchange framework arose independently from the effort to make RDF easier, there is a natural overlap in motivation, and both efforts can benefit each other.

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
* [Issue 43: Nobody knows who does what with what](https://github.com/w3c/EasierRDF/issues/43)
* [Issue 40: Spoggy easy create & read graphs](https://github.com/w3c/EasierRDF/issues/40)
* [Issue 39: SPARQL Triplestore and Reasoning Performance](https://github.com/w3c/EasierRDF/issues/39)
* [Issue 38: Lack of Full OWL2 Support in Triplestores](https://github.com/w3c/EasierRDF/issues/38)
* [Issue 37: Lack of RDF Visualisation Software](https://github.com/w3c/EasierRDF/issues/37)
* [Issue 35: Lack of a Good Editor](https://github.com/w3c/EasierRDF/issues/35)
* [Issue 5: Moribundity of Tools](https://github.com/w3c/EasierRDF/issues/5)
* [Issue 4: Overview of an RDF triple store](https://github.com/w3c/EasierRDF/issues/4)
* [Issue 3: Lack of automated feedback / validation](https://github.com/w3c/EasierRDF/issues/3)
* [Issue 2: Tools are scattered](https://github.com/w3c/EasierRDF/issues/2)
<!-- END_DO_NOT_EDIT! Category: tools -->

## [Category: education](https://github.com/w3c/EasierRDF/labels/Category%3A%20education): For documentation and education
<!-- BEGIN_DO_NOT_EDIT! Category: education -->
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
* [Issue 43: Nobody knows who does what with what](https://github.com/w3c/EasierRDF/issues/43)
* [Issue 16: Easier-to-use competitors](https://github.com/w3c/EasierRDF/issues/16)
* [Issue 15: Define an easier profile of RDF](https://github.com/w3c/EasierRDF/issues/15)
* [Issue 14: Namespaces are lost in the RDF model](https://github.com/w3c/EasierRDF/issues/14)
* [Issue 13: Namespace proliferation](https://github.com/w3c/EasierRDF/issues/13)
* [Issue 12: IRI allocation](https://github.com/w3c/EasierRDF/issues/12)
<!-- END_DO_NOT_EDIT! Category: usage -->

## [Category: language features](https://github.com/w3c/EasierRDF/labels/Category%3A%20language%20features): For language features of RDF itself -- model and syntax
<!-- BEGIN_DO_NOT_EDIT! Category: language features -->
* [Issue 48: Different kinds of identifiers](https://github.com/w3c/EasierRDF/issues/48)
* [Issue 45: Property Graphs](https://github.com/w3c/EasierRDF/issues/45)
* [Issue 42: Maybe "datatype" should be in the RDF Graph explicitly](https://github.com/w3c/EasierRDF/issues/42)
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
* [Issue 47: SPARQL: Miscellaneous features wanted](https://github.com/w3c/EasierRDF/issues/47)
* [Issue 44: SPARQL: The unnamed/default graph should have a standard name](https://github.com/w3c/EasierRDF/issues/44)
* [Issue 29: No standard way to map a JSON predicate to a URI](https://github.com/w3c/EasierRDF/issues/29)
* [Issue 28: SPARQL: Named solution sets](https://github.com/w3c/EasierRDF/issues/28)
* [Issue 27: Lack of a standard rules language](https://github.com/w3c/EasierRDF/issues/27)
* [Issue 26: Lack of standard RDF canonicalization](https://github.com/w3c/EasierRDF/issues/26)
<!-- END_DO_NOT_EDIT! Category: related standards -->

## Uncategorized
[Search](https://github.com/w3c/EasierRDF/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+no%3Alabel) for issues with no category label.

