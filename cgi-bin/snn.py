#!/usr/bin/python2
import commands

commands.getoutput('sudo yum install hadoop -y')

commands.getoutput('sudo yum install jdk -y')

e1=open('/etc/hadoop/hdfs-site.xml',"w")

e2=open('/etc/hadoop/core-site.xml',"w")

e1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.http.address</name>
<value>192.168.1.21:50070</value>
</property>

<property>
<name>dfs.secondary.http.address</name>
<value>192.168.1.22:50090</value>
</property>

<property>
<name>fs.checkpoints.edits.dir</name>
<value>/old</value>
</property>

<property>
<name>fs.checkpoint.dir</name>
<value>/new</value>
</property>

</configuration>""")
e2.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://192.168.1.21:9001</value>
</property>
</configuration>""" )

	
e1.close()
e2.close()

x=commands.getoutput("ping -c 1 %s | grep received | cut -f4 -d' ' ")
if x!=1:
	commands.getoutput("sudo iptable -F")
	commands.getoutput("sudo hadoop-daemon.sh stop namenode")
	commands.getoutput("sudo hadoop-daemon.sh start namenode")

r=open("/etc/crontab","a+")
	r.write("\n 59 * * * * hadoop secondarynamenode -checkpoint force")
	r.close()

commands.getoutput('sudo hadoop-daemon.sh start secondarynamenode')

commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')



