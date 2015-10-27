#!/usr/bin/python2

import os
import commands
import cgi
import cgitb
cgitb.enable()

print "content-type: text/html"
print

y=cgi.FormContent()

p=y['pof'][0]

print "Go back a page if completed reading"
print "<pre>"
print commands.getoutput("sudo hadoop fs -cat /"+p)
print "</pre>"
