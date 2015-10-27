#!/usr/bin/python2

import cgi 
import cgitb
cgitb.enable()

print "content-type: text/html"

data=cgi.FormContent()

username=data['username'][0]
password=data['password'][0]

if username == "mohit" and password == "redhat":
	print "location: http://192.168.1.28/Installation.html"
	print
else:
	print "location: http://192.168.1.28/login-in.html"
	print


