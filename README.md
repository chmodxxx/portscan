<b><h1>Portscan</h1></b><br>
Simple Portscanner using multithreading to optimise execution time using TCP sockets in <b> python</b> 
<br>The variable c depends on how fast you want the results, also the number of ip per threads depends on your computer, as you can see it may print the result of a high number port before a lower one, because the thread of that port finished , currently working on sorting the output
<br>
<h1><b>Usage : </b></h1><br>
<pre><code> ./portscan.py -H #Host_IP
</code></pre>
<br><br>
<h3>Example of execution :</h3>

<pre><code>#)python portscan.py -H 192.168.1.1</code></pre>
<pre><code>
************************************************************
Enter The start of Ports to scan : 1
Enter The end of Ports to scan : 100</code></pre><pre><code>
************************************************************
Starting scan now 

Scan started at  2017-01-16 11:39:49.133652

Scanning the host :  192.168.1.1 

[+] Port Open : ----------> 	  21 ( ftp )
[+] Port Open : ----------> 	  22 ( ssh )
[+] Port Open : ----------> 	  23 ( telnet )
[+] Port Open : ----------> 	  80 ( http )

Finished scan in 0 hours 00 minutes 00.239604 seconds

</code></pre>

<h2>Explanation of the code :</h2>

<p>You'll need to read the file explanation_of_code and the script comments</p>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <b>BY SALAH BADDOU</b> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
