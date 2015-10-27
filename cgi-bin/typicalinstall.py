#!/usr/bin/python2

import commands,os
import thread
import cgi
import cgitb
cgitb.enable()


print "content-type: text/html"
print
	

def NN(x):
				
	os.system('sshpass -predhat scp namenode.py %s:/root/' % x)

	os.system('sshpass -predhat ssh %s python2 namenode.py' % x)

	os.system('sshpass -predhat ssh %s rm -rfv namenode.py' % x)

def JT(y):
	os.system('sshpass -predhat scp jobtracker.py %s:/root/' % y) 

	os.system('sshpass -predhat ssh %s python2 jobtracker.py' % y)

	os.system('sshpass -predhat ssh %s rm -rfv jobtracker.py' % y)

def Client(): 
	os.system('python2 client.py')



def DN(z):
	os.system('sshpass -predhat scp datanode.py %s:/root/' % z) 

	os.system('sshpass -predhat ssh %s python2 datanode.py' % z)

	os.system('sshpass -predhat ssh %s rm -rfv datanode.py' % z)

def TT(v):
	os.system('sshpass -predhat scp tasktracker.py %s:/root/' % v) 

	os.system('sshpass -predhat ssh %s python2 tasktracker.py' % v)

	os.system('sshpass -predhat ssh %s rm -rfv tasktracker.py' % v)

network=commands.getoutput('route -n | grep 255 |cut -d" " -f1')
host1 = commands.getoutput("arp-scan --interface=eth0 %s/24 |grep '192.168.*' |cut -f1" % network)
print host1
host = list(host1.split())
i=0

o=open('namenode.py',"w")

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

commands.getoutput('jps')'''%host[0] )

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
commands.getoutput('jps')'''%(host[0], host[0]))

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
commands.getoutput('jps')'''% host[0])

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
commands.getoutput('jps')''' % host[0])

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
f1.close()''' %(host[0] , host[0]))
commands.getoutput('sudo chmod 755 client.py')
q.close()




	
thread.start_new_thread(NN, (host[0],))

thread.start_new_thread(JT,(host[0],))

thread.start_new_thread(Client,())


while True:
	i=i+1
	count = 0
	for n in host:
		if count >=0:
			thread.start_new_thread(DN, (n,))
			thread.start_new_thread(TT, (n,))
			count= count+1
		else:
			count = count+1
		


