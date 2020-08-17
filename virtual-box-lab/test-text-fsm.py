from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.255.131",
    "username": input('Username:'),
    "password": getpass(),
}
command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command, use_textfsm=True)

pprint(output)

#Valid ntc-templates not found, please install https://github.com/networktocode/ntc-templates
#and then set the NET_TEXTFSM environment variable to point to the ./ntc-templates/templates
#directory.

#export NET_TEXTFSM=/Users/jdwright/GitHub/ntc-templates/templates