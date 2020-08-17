from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.255.131",
    "username": getpass(prompt='Username: ', stream=None),
    "password": getpass(),
}

cisco2 = {
    "device_type": "cisco_ios",
    "host": "192.168.255.254",
    "username": 'lab-admin',
    "password": 'En@ble123',
}

    
    
 
try:
    net_connect = ConnectHandler(**cisco2)
except:
    print("Failed")

print(net_connect.find_prompt())

command = "show ip int brief"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

with ConnectHandler(**cisco1) as net_connect:
    # Use TextFSM to retrieve structured data
    output = net_connect.send_command(command, use_textfsm=True)

Valid ntc-templates not found, please install https://github.com/networktocode/ntc-templates
and then set the NET_TEXTFSM environment variable to point to the ./ntc-templates/templates
directory.

commands = ["interface loopback 1", "description TEST", "ip address 1.2.3.4 255.255.255.255"]
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

commands = ["no interface loopback 1",]
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

    cfg_file = "config_changes.txt"
with ConnectHandler(**device1) as net_connect:
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()


    net_connect.disconnect()

++++++++++++++
https://stackoverflow.com/questions/316866/ping-a-site-in-python

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



+++++ before try and except with paramiko tried using ping to test a device reachability it did not work reliably 

def ping_device(inventory):
#ping every device in the inventory, parse the ping results and mark the device up or down
    for device in inventory.keys():
        host = inventory[device]['mgmt-ip']    
        ping = subprocess.Popen(
            ["ping", "-c", "3", host],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate()
        #ref https://stackoverflow.com/questions/316866/ping-a-site-in-python
        out = str(out)
        #typecast restult from ping in bytes into a string
        out = out.split("\\n")
        out1 = out[1].split(" ")
        out2 = out[2].split(" ")
        #parse the ping output

        if out[1] == 'timeout' and out[2] == 'bytes':
            inventory[device]['reachable'] = True
        else:
            inventory[device]['reachable'] = False
        #if the first two pings fail mark the device as down (reachable = False) 
        #otherwise mark it as up (reachable = True)
        #adding a new kv pair to the inventory dictionary

    for device in inventory.keys():
        print(f"{device} is reachable (T/F): {inventory[device]['reachable']}")
        #print the device and its status

    return inventory

def open_ssh_con(inventory):
#open an ssh connection to each device marked as reachable in the inventory and ...
#return and updated inventory
    
    #inventory = ping_device(inventory)
    ##verify which lab devices are reachable using the ping_device function

    for device in inventory.keys():
    #for each device in inventory if the device is marked as unreachable also mark the ssh_con as False
    #else stablish an ssh connection to it and add it to the inventory under ssh_con
        if inventory[device]['reachable'] == False:
           inventory[device]['ssh_conn'] = False
        else:
            device_info = {
                "device_type": inventory[device]['netmiko-type'],
                "host": inventory[device]['mgmt-ip'],
                "username": inventory[device]['lab-user'],
                "password": inventory[device]['lab-pass'],
            }
            with ConnectHandler(**device_info) as net_connect: 
                inventory[device]['ssh_conn'] = net_connect 
    
    return inventory