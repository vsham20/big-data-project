#!/usr/bin/python2
import commands
commands.getoutput('yum install hadoop -y')

commands.getoutput('yum install jdk -y')

f=open('/etc/hadoop/hdfs-site.xml',"w")
f1=open('/etc/hadoop/core-site.xml',"w")

f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/Data</value>
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
</configuration>""" )

f.close()
f1.close()
commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')
commands.getoutput('hadoop-daemon.sh start datanode')
commands.getoutput('jps')
raw_input()