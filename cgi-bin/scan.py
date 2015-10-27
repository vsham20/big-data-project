#!/usr/bin/python2


import commands
import cgi
import cgitb
cgitb.enable

print "content-type:text/html" 
print 


network=commands.getoutput('sudo route -n | grep 255 |cut -d" " -f1')
host1 = commands.getoutput("sudo arp-scan --interface=eth0 %s/24 |grep '192.168.*' |cut -f1" % network)
print "<pre>"
print host1 
print "</pre>"

