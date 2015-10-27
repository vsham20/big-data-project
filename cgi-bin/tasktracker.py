#!/usr/bin/python2
import commands
commands.getoutput('yum install hadoop')

commands.getoutput('yum install jdk')


host = raw_input("input the IP of jobtracker")

f=open('/etc/hadoop/mapred-site.xml',"w")

f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>192.168.1.1:9002</value>
</property>
</configuration>""")

f.close()

commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')
commands.getoutput('hadoop-daemon.sh start tasktracker')
commands.getoutput('jps')

raw_input()