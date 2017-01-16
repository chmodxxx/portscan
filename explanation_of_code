The Header : 

import socket to use socket connection
import subprocess to clear the shell 
import datetime to output the time and calculate the time of execution(t2-t1)
import threading to use multithreading
import optparse to use the options parser (-H)

The Part 1:

The Part 1 is simple , it focuses on the optionparser the first line is a usage example if the args aren't respected, and the 2nd line
is the definition of the option -H after that we will use the Host IP output using options.host

The Part 2:

Part 2 is the declaration of the class myThread with the method init and run to initiate the arguments of the thread (ip,ports..), and run
to start the thread, you noticed that starting of a thread means calling the function scantcp.

The Part 3:

Part 3 is where the function scantcp is defined i'm using exception handling in case of error sockets, a loop that start from the port start
to the last port where we create an IPV4 socket TCP and setting the default time out to c to have faster result when the target port doesnt 
respond, after that I stored the result of the function socket.connect_ex() in the variable result notice that this  function returns 0 if
we target accepted the connection which means the port is open otherwise it returns an error variable which we didnt use, after that the
program prints Port is open if result=0 and it outputs the name of the service using the method socket.getservbyport and if it doesnt find
the name of the service it just outputs Service name not found.
And finally the exceptions messages output.

The Part 4:
Part 4 is the part where user inputs the begining of the ports and the end and we define some variables like number of ports handled by 
thread , I chose 50 because i didnt use large inputs.
The condition if (tot_port%tot_port_thread != 0):    basically means if user outputs for example 120 port notice that threads will be 2 
                  	tnum= tnum+1
so the last 20 port won't be handled thats why I incremeneted the value of threads so it will be 3 threads, and finally I declared a list 
variable threads which we will use to terminate the treads with function .join()

The Part 5:
Part 5 is the port of the execution of threads, with a for loop of number of threads initiation of thread with parametres and starting it
the variable change is because for example we have 130 port, so 3 threads, we need first thread to handle 50 port from(1-50) the second
one from(51-100) and so on , finally we append the thread to the list

The Part 6:
Part 6 is the end of program the t.join() means : wait_until_finished(thread t) in our loop it means wait until all threads finished then go
and finally the program gets the date of end splits it and with mathematical operation (t2-t1) the output is the time the operation took.
