from netmiko import ConnectHandler
from getpass import getpass
import subprocess 
import lab-device-inventory


def ping_device(inventory):
#ping every device in the inventory, parse the ping results and mark the device up or down
    for device in inventory.keys():
        host = device['mgmt-ip']    
        ping = subprocess.Popen(
            ["ping", "-c", "3", host],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, error = ping.communicate(0
        #ref https://stackoverflow.com/questions/316866/ping-a-site-in-python
        out = str(out)
        #typecast restult from ping in bytes into a string
        out = out.split("\\n")
        out1 = out[1].split(" ")
        out2 = out[2].split(" ")
        #parse the ping output

        if out[1] == 'timeout' and out[2] == 'timeout':
            inventory['device']['reachable'] = False
        else:
            inventory['device']['reachable'] = True
        #if the first two pings fail mark the device as down (reachable = False) 
        #otherwise mark it as up (reachable = True)
        #adding a new kv pair to the inventory dictionary

    for device in inventory.keys():
        print(f"{inventory['device']} is {inventory['device']['reachable']}")
        #print the device and its status

    return inventory


def open_ssh_con(inventory):
#open an ssh connection to each device marked as reachable in the inventory and ...
#return and updated inventory
    inventory = ping_device(inventory)
    #verify which lab devices are reachable using the ping_device function

    for device in inventory.keys():
    #for each device in inventory if the device is marked as unreachable also mark the ssh_con as False
    #else stablish an ssh connection to it and add it to the inventory under ssh_con
        if inventory['device']['reachable'] == False:
            inventroy['device']['ssh_conn'] = False
        else:
            device_info = {
                "device_type": device['netmiko-type'],
                "host": device['mgmt-ip'],
                "username": device['lab-user'],
                "password": device['lab-pass'],
            }
            net_connect = ConnectHandler(**device_info) 
            inventroy['device']['ssh_conn'] = net_connect 
    
    return inventory



