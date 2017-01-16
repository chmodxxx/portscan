## BY SALAH BADDOU
## DONT COPY PASTA 
#Root>
import socket
import sys,subprocess,threading
from threading import Thread
from datetime import datetime
from optparse import OptionParser

subprocess.call('clear',shell=True)
#Part_1
parser = OptionParser(usage="usage: ./portscan.py -H [host] OR --host=IP")

parser.add_option('-H','--host',help="host to Scan example : 192.168.1.1",action="store", default="192.168.1.1")

(options, args) = parser.parse_args()
#End_Part_1
#Part_2
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
#End_Part_2
#Part_3
def scantcp(threadName,ip,port_start,port_end,c):
	try :
		for port in range(port_start,port_end):
			sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(c)
			result=sock.connect_ex((ip,port))
			if result==0:
				try :
					print "[+] Port Open : ----------> \t ",port,'(',socket.getservbyport(port),')'
				except :
					print 'Service name not found)'
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
#End_Part_3
#Part_4
print '*'*60
ip=options.host
port_start=int(raw_input("Enter The Start Port to scan : "))
port_end=int(raw_input("Enter The End of Ports to scan : "))
c=0.5
print "*"*60
print 'Starting scan now \n'
t1=datetime.now()
print "Scan started at ",t1
print '\nScanning the host : ',ip,'\n'
tot_port=port_end-port_start
tot_port_thread=50 #total port handled by one thread
tnum=tot_port/tot_port_thread #tnum number of threads

if (tot_port%tot_port_thread != 0):
	tnum= tnum+1
threads=[]
#End_Part_4
#Part_5
try :
	for i in range(tnum):
		port_end=port_start+tot_port_thread-1
		thread = myThread("T1",ip,port_start,port_end,c)
		thread.start()
		port_start=port_end+1
		threads.append(thread)
except :
	print "Problem with starting Thread"

#End_Part_5
#Part_6
for t in threads:
	t.join()
t2= datetime.now()
total=t2-t1
total=str(total)
a=total.split(' ')[-1]
x,y,z=map(str,a.split(':'))
print 'Finished scan in '+x+' hours '+y+' minutes '+z+' seconds'
#End_Part_6
