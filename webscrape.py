#!/usr/bin/python

# This module allow us to retrieve web pages.
import urllib2

# This module allows us to create regular expressions
import re

"""
This asks a user to input a website to scan for emails. It takes the input, and stores it in the variable askPage.
Website to try: http://www.dsu.edu/about-dsu/directory
"""
askPage = raw_input("What webpage would you like to scan for emails?\n")

#This retrieves a webpage
webObject = urllib2.urlopen(askPage)

#This reads the webpage
webPage = webObject.readlines()

#This expression will look for email addresses and I don't know how. If I wanted to learn more, I would visit pythex.org.
expression = re.compile("[a-zA-Z0-9-_\.]*@[a-zA-Z0-9-_]*\.[a-zA-Z]{2,3}")

#This expression will look for href tags containing URLs we can spider.
linkExpression = re.compile('href="[^"]*">')

#Counts the number of emails we find
emailCounter = 0

#Counts the number of links we find
linkCounter = 0

#Search every line in the webpage for an email address.
for line in webPage:
    # for every line, search it for our regular expression.
    match = expression.search(line)
    # if we find a match, return its output
    if match:
        # Increases our email counter
        emailCounter += 1
        # specifically only return group(0)
        print match.group(0)
    else:
        # if we don't find an email address, check for a link.
        match = linkExpression.search(line)
        if match:
            # Increase our link counter
            linkCounter += 1
            print match.group(0)


print "Total emails found: %i" % emailCounter
print "Total links found: %i" % linkCounter