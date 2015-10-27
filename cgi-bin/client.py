#!/usr/bin/python2
import commands
commands.getoutput('yum install hadoop -y')

commands.getoutput('yum install jdk -y')

f=open('/etc/hadoop/mapred-site.xml',"w")
f1=open('/etc/hadoop/core-site.xml',"w")

f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>192.168.1.1:9002</value>
</property>
</configuration>""")

f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://192.168.1.1:9001</value>
</property>
</configuration>""")



f.close()
f1.close()