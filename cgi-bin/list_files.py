#!/usr/bin/python2

import os
import commands
import cgi
import cgitb
cgitb.enable()

print "content-type: text/html"
print

print "<pre>"
print commands.getoutput("sudo hadoop fs -ls /")
print "</pre>"
