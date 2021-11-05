#!/usr/bin/env python3

# coding: utf-8

# In[26]:


'''This is for updating the issues lists in the EasierRDF github repo at 
https://github.com/w3c/EasierRDF .

Usage: 
	./GetEasierRdfIssuesByCategory.py > README.md

Author: David Booth 11/5/21
License: CC0
'''

import urllib.request
import urllib.parse
import json
import re

issuesUrl='https://github.com/w3c/EasierRDF/issues'
categoriesUrl='https://github.com/w3c/EasierRDF/labels?q=Category%3A'
readmeUrl = 'https://raw.githubusercontent.com/w3c/EasierRDF/master/README.md'

def GetCategories(categoriesUrl='https://github.com/w3c/EasierRDF/labels?q=Category%3A'):
    '''See https://stackoverflow.com/questions/41753769/get-all-github-issues-from-repo-with-specific-label'''
    url = categoriesUrl
    url = re.sub(r'^https://github\.com/', 'https://api.github.com/repos/', url)
    # print(url)
    header={'Accept': 'application/json'}
    req = urllib.request.Request(url=url, headers=header, method='GET')
    categoriesJson = urllib.request.urlopen(req).read()
    categoriesObjects = json.loads(categoriesJson.decode("utf-8"))
    return categoriesObjects

categoryNames = ['Category: big ideas',
                'Category: tools',
                'Category: education',
                'Category: usage',
                'Category: easier profile',
                'Category: language features',
                'Category: related standards']

categoryNames = [ co['name'] for co in GetCategories() if re.match(r"Category:", co['name']) ]
# print("\n".join(categoryNames))
# exit(0)
# print(json.dumps(GetCategories()))
# exit(0)

def GetIssuesByLabel(label='Category: big ideas', issuesUrl='https://github.com/w3c/EasierRDF/issues'):
    '''See https://stackoverflow.com/questions/41753769/get-all-github-issues-from-repo-with-specific-label'''
    url = issuesUrl + "?labels=" + urllib.parse.quote(label)
    url = re.sub(r'^https://github\.com/', 'https://api.github.com/repos/', url)
    # print(url)
    header={'Accept': 'application/json'}
    req = urllib.request.Request(url=url, headers=header, method='GET')
    issuesJson = urllib.request.urlopen(req).read()
    issuesObjects = json.loads(issuesJson.decode("utf-8"))
    return issuesObjects

def ObjectToMarkdown(issuesObjects):
    issuesMdList = [ '* [Issue {}: {}]({})\n'.format(i['number'], i['title'], i['html_url']) for i in issuesObjects]
    issuesMd = "".join(issuesMdList)
    return issuesMd

GetIssuesByLabel()


# In[27]:


def UpdateIssuesList(categoryName, page, issuesUrl='https://github.com/w3c/EasierRDF/issues'):
    '''Update the issue list in the given category in the page.  
    The rest of the page is unchanged.
    The issue list in each category is marked like this:
    
    ## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories
    <!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->
    * [Issue 34: Idea: Higher-level RDF language](https://github.com/w3c/EasierRDF/issues/34)
    * [Issue 33: Idea: Build powerful query engines](https://github.com/w3c/EasierRDF/issues/33)
    * [Issue 32: Idea: Build JavaScript libraries that work in the browser](https://github.com/w3c/EasierRDF/issues/32)
    * [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)
    * [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)
    <!-- END_DO_NOT_EDIT! Category: big ideas -->'''
    categoryEncoded = urllib.parse.quote_plus(categoryName)
    beginMarker = '<!-- BEGIN_DO_NOT_EDIT! ' + categoryName + ' -->'
    endMarker   = '<!-- END_DO_NOT_EDIT! ' + categoryName + ' -->'
    beforeMiddleAfter = page.split(beginMarker)
    if len(beforeMiddleAfter) != 2:
        raise Exception('ERROR: Did not find beginMarker in page: '+beginMarker)
    before = beforeMiddleAfter[0]
    middleAfter = beforeMiddleAfter[1].split(endMarker)
    if len(middleAfter) != 2:
        raise Exception('ERROR: Did not find endMarker in page: '+endMarker)
    middle = middleAfter[0]
    after = middleAfter[1]
    issuesList = ObjectToMarkdown(GetIssuesByLabel(categoryName))
    page = before + beginMarker + '\n' + issuesList + endMarker + after
    return page


# print(ObjectToMarkdown(GetIssuesByLabel('Category: big ideas')))



# In[33]:


page = '''    ## [Category: big ideas](https://github.com/w3c/EasierRDF/labels/Category%3A%20big%20ideas): For major ideas that span multiple issue categories
    <!-- BEGIN_DO_NOT_EDIT! Category: big ideas -->
    * [Issue 31: Idea: Base Linked Data on a JavaScript API](https://github.com/w3c/EasierRDF/issues/31)
    * [Issue 30: Idea: Attract JavaScript front-end developers](https://github.com/w3c/EasierRDF/issues/30)
    <!-- END_DO_NOT_EDIT! Category: big ideas -->'''

# print(UpdateIssuesList('Category: big ideas', page, issuesUrl))


# In[34]:

def main():
    page = urllib.request.urlopen(readmeUrl).read().decode("utf8")
    for categoryName in categoryNames:
        page = UpdateIssuesList(categoryName, page, issuesUrl)
    print(page)

if __name__ == "__main__":
    main()

