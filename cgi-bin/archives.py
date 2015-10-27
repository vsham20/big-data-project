#!/usr/bin/python2

import commands
import thread
import cgi
import cgitb
cgitb.enable()


print "content-type: text/html"
print

y=cgi.FormContent()

AN=y['an'][0]
PD=y['pd'][0]
Dir=y['ppd'][0]
OD=y['od'][0]


print commands.getoutput('sudo hadoop archive -archiveName %s -p %s (%s)* %s' %(AN,PD,Dir,OD) )
print "Archive %s created successfully"%AN
