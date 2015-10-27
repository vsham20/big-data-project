#!/usr/bin/python2

import commands
import cgi
import cgitb
cgitb.enable()

print "content-type: text/html"
print



data=cgi.FormContent()

NNIP=data['nn'][0]
JTIP=data['jt'][0]
u=data['client'][0]

network=commands.getoutput('route -n | grep 255 |cut -d" " -f1')
host1 = commands.getoutput("arp-scan --interface=eth0 %s /24 |grep '192.168.*' |cut -f1" %network)
print "Do not use the first IP(network IP)"
print host1


o=open(' namenode.py',"w")

o.write('''#!/usr/bin/python2
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
<name>dfs.name.dir</name>
<value>/Name</value>
</property>
</configuration>""")
f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>""" )

	

f.close()
f1.close()

commands.getoutput('hadoop namenode -format')

commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')

commands.getoutput('hadoop-daemon.sh start namenode')

commands.getoutput('jps')

raw_input()'''% NNIP)

o.close()
commands.getoutput('sudo chmod 755 namenode.py')

m=open('jobtracker.py',"w")

m.write('''#!/usr/bin/python2
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
<value>%s:9002</value>
</property>
</configuration>""" )

f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>""")



f.close()
f1.close()
commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')
commands.getoutput('hadoop-daemon.sh start jobtracker')
commands.getoutput('jps')
raw_input()'''%(JTIP, NNIP))

m.close()
commands.getoutput('sudo chmod 755 jobtracker.py')

n=open('datanode.py',"w")

n.write('''#!/usr/bin/python2
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
<value>hdfs://%s:9001</value>
</property>
</configuration>""" )

f.close()
f1.close()
commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')
commands.getoutput('hadoop-daemon.sh start datanode')
commands.getoutput('jps')
raw_input()'''% NNIP)

n.close()
commands.getoutput('sudo chmod 755 datanode.py')

p=open('tasktracker.py',"w")

p.write('''#!/usr/bin/python2
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
<value>%s:9002</value>
</property>
</configuration>""")

f.close()

commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')
commands.getoutput('hadoop-daemon.sh start tasktracker')
commands.getoutput('jps')

raw_input()''' % JTIP)

p.close()
commands.getoutput('sudo chmod 755 tasktracker.py')

q=open('client.py',"w")

q.write('''#!/usr/bin/python2
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
<value>%s:9002</value>
</property>
</configuration>""")

f1.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>""")



f.close()
f1.close()''' %(JTIP, NNIP))
commands.getoutput('sudo chmod 755 client.py')
q.close()

e=open('snn.py',"w")

e.write('''#!/usr/bin/python2
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
     <value>%s:50070</value>
     </property>

     <property>
     <name>dfs.secondary.http.address</name>
     <value>%s:50090</value>
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
<value>hdfs://%s:9001</value>
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


commands.getoutput('PATH=/usr/java/jdk1.7.0_51/bin/:$PATH')

'''%(NNIP,SNIP,NNIP))
e.close()
commands.getoutput('sudo chmod 755 snn.py')



commands.getoutput('sudo sshpass -predhat scp namenode.py %s:/root/' % NNIP)

commands.getoutput('sudo sshpass -predhat ssh %s /python2 namenode.py' % NNIP)

commands.getoutput('sudo sshpass -predhat ssh %s rm -rfv namenode.py' % NNIP)		

commands.getoutput('sudo sshpass -predhat scp jobtracker.py %s:/root/' % JTIP) 

commands.getoutput('sudo sshpass -predhat ssh %s /python2 jobtracker.py' % JTIP)

commands.getoutput('sudo sshpass -predhat ssh %s rm -rfv jobtracker.py' % JTIP)

commands.getoutput('sudo sshpass -predhat scp client.py %s:/root/' %u) 

commands.getoutput('sudo sshpass -predhat ssh %s python2 client.py' % u)

commands.getoutput('sudo sshpass -predhat ssh %s rm -rfv client.py' % u)

commands.getoutput('sudo sshpass -predhat scp datanode.py %s:/root/' % JTIP) 

commands.getoutput('sudo sshpass -predhat ssh %s /root/datanode.py' % JTIP)

commands.getoutput('sudo sshpass -predhat ssh %s rm -rfv /root/datanode.py' % JTIP)


commands.getoutput('sudo sshpass -predhat scp tasktracker.py %s:/root/' % JTIP) 

commands.getoutput('sudo sshpass -predhat ssh %s python2 tasktracker.py' % JTIP)

commands.getoutput('sudo sshpass -predhat ssh %s rm -rfv tasktracker.py' % JTIP)


			
print "Cluster formed successfully.Please go back one page to continue"

