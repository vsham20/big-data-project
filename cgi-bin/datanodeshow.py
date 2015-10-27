#!/usr/bin/python2


import commands
import cgi
import cgitb
cgitb.enable()

print "content-type: text/html"
print


print "<pre>"
print commands.getoutput('sudo hadoop  dfsadmin -report')
print "</pre>"

