#Parsing icmp test data
#https://stackoverflow.com/questions/316866/ping-a-site-in-python

import subprocess

host = "192.168.255.132"

ping = subprocess.Popen(
    ["ping", "-c", "3", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)
out, error = ping.communicate()
out = str(out)
print(out, "\n")
out = out.split("\\n")
print(out, "\n")
out1 = out[1].split(" ")
print(out1, "\n")
out2 = out[2].split(" ")
print(out2, "\n")


###Working

>>> print(out, "\n")
b'PING 192.168.255.131 (192.168.255.131): 56 data bytes\n64 bytes from 192.168.255.131: icmp_seq=0 ttl=255 time=0.987 ms\n64 bytes from 192.168.255.131: icmp_seq=1 ttl=255 time=0.806 ms\n\n--- 192.168.255.131 ping statistics ---\n2 packets transmitted, 2 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 0.806/0.897/0.987/0.090 ms\n' 

>>> out = out.split("\\n")
>>> print(out, "\n")
["b'PING 192.168.255.131 (192.168.255.131): 56 data bytes", '64 bytes from 192.168.255.131: icmp_seq=0 ttl=255 time=0.987 ms', '64 bytes from 192.168.255.131: icmp_seq=1 ttl=255 time=0.806 ms', '', '--- 192.168.255.131 ping statistics ---', '2 packets transmitted, 2 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 0.806/0.897/0.987/0.090 ms', "'"] 

>>> out1 = out[1].split(" ")
>>> print(out1, "\n")
['64', 'bytes', 'from', '192.168.255.131:', 'icmp_seq=0', 'ttl=255', 'time=0.987', 'ms'] 

>>> out2 = out[2].split(" ")
>>> print(out2, "\n")
['64', 'bytes', 'from', '192.168.255.131:', 'icmp_seq=1', 'ttl=255', 'time=0.806', 'ms'] 


###Failed
>>> out = str(out)
>>> print(out, "\n")
b'PING 192.168.255.132 (192.168.255.132): 56 data bytes\nRequest timeout for icmp_seq 0\nRequest timeout for icmp_seq 1\n\n--- 192.168.255.132 ping statistics ---\n3 packets transmitted, 0 packets received, 100.0% packet loss\n' 

>>> out = out.split("\\n")
>>> print(out, "\n")
["b'PING 192.168.255.132 (192.168.255.132): 56 data bytes", 'Request timeout for icmp_seq 0', 'Request timeout for icmp_seq 1', '', '--- 192.168.255.132 ping statistics ---', '3 packets transmitted, 0 packets received, 100.0% packet loss', "'"] 

>>> out1 = out[1].split(" ")
>>> print(out1, "\n")
['Request', 'timeout', 'for', 'icmp_seq', '0'] 

>>> out2 = out[2].split(" ")
>>> print(out2, "\n")
['Request', 'timeout', 'for', 'icmp_seq', '1'] 