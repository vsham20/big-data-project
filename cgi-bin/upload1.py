#!/usr/bin/python2
import commands
import cgi
import cgitb
cgitb.enable()


print "content-type: text/html"
print 

y=cgi.FormContent()

path=y['pof'][0]

print commands.getoutput("sudo hadoop fs -put %s /" %path)
print "File uploaded successfully please go back a page to continue"

