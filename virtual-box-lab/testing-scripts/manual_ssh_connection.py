from netmiko import ConnectHandler

device = {
    "device_type": "arista_eos",
    "host": "192.168.255.133",
    "username": 'lab-admin',
    "password": 'En@ble123',
    "secret": 'En@ble123',
}

try:
    net_connect = ConnectHandler(**device)
except:
    print("Failed")

print(net_connect.find_prompt())

command = "show run"
net_connect = ConnectHandler(**device)
net_connect.enable()
output = net_connect.send_command(command)
print(output)

#################
from getpass import getpass
cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.255.131",
    "username": getpass(prompt='Username: ', stream=None),
    "password": getpass(),
}

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command(command)