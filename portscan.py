## BY SALAH BADDOU
## DONT COPY PASTA 
#Root>
#!/usr/bin/env python

import socket
import sys,subprocess,threading
from threading import Thread
from datetime import datetime
from optparse import OptionParser

subprocess.call('clear',shell=True) #clear screan

parser = OptionParser(usage="usage: ./portscan.py -H [host] OR --host=IP")

parser.add_option('-H','--host',help="host to Scan example : 192.168.1.1",action="store", default="192.168.1.1")

(options, args) = parser.parse_args()
port_list=[]
class myThread(threading.Thread):
	def __init__(self,threadName,ip,port_start,port_end,c):
		threading.Thread.__init__(self)
		self.threadName = threadName
		self.ip=ip
		self.port_start=port_start
		self.port_end=port_end
		self.c=c
	def run(self):
		scantcp(self.threadName,self.ip,self.port_start,self.port_end,self.c)
def scantcp(threadName,ip,port_start,port_end,c):
	try :
		for port in range(port_start,port_end):
			x=port
			sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(c)
			result=sock.connect_ex((ip,port))
			if result==0:
				port_list.append(port)
			sock.close()
	except KeyboardInterrupt:
		print "Keyboard Interrupt Detected"
		sys.exit()	
	except socket.gaierror:
		print "Hostname coudlnt be resolved"
		sys.exit()
	except socket.error:
		print "Couldnt connect to the host"
		sys.exit()
print '*'*60
ip=options.host
while True:
	try:
		port_start=int(raw_input("Enter Start Ports to scan : "))
		if port_start<=0:
			continue
		else :
			break
	except ValueError:
		print "Please Enter a Valid Number"
while True:
	try :
		port_end=int(raw_input("Enter the End of Ports to scan : "))
		if port_end<=0:
			continue
		else :
			break
	except ValueError:
		print "Please Enter a Valid Number"
c=0.5
print "*"*60
print 'Starting scan now \n'
t1=datetime.now()
print "Scan started at ",t1
print '\nScanning the host : ',ip,'\n'
tot_port=port_end-port_start
tot_port_thread=100 #total port handled by one thread
tnum=tot_port/tot_port_thread #tnum number of threads

if (tot_port%tot_port_thread != 0):
	tnum= tnum+1
threads=[]
try :
	for i in range(tnum):
		port_end=port_start+tot_port_thread-1
		thread = myThread("T1",ip,port_start,port_end,c)
		thread.start()
		port_start=port_end+1
		threads.append(thread)
except :
	print "Problem with starting Thread"


for t in threads:
	t.join()
t2= datetime.now()	
k=0
port_list=sorted(port_list)
for p in port_list:
	k+=1

print "Number Of Open Ports : ",k,"\n"
print "Number Of Closed/Filtered Ports : ",tot_port-k+1,'\n'
print "|	Port 	  |      Status		 |        Service Name      "
print "--------------------------------------------------------------------"
for p in port_list:
	try :
		socket.getservbyport(p)
		print "|	",p," 	  |        OPEN		 |","        ",socket.getservbyport(p)
		print "------------------------------------------------------------------------------"
	except:
		print "|	",p," 	  |        OPEN		 |","        "," No Service Name Was Found"
		print "------------------------------------------------------------------------------"

total=t2-t1
total=str(total)
a=total.split(' ')[-1]
x,y,z=map(str,a.split(':'))
print '\nFinished scan in '+x+' hours '+y+' minutes '+z+' seconds'

