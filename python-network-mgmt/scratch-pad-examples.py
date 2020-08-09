import ipaddress
supernet = ipaddress.IPv4Network("192.168.0.0/16")


supernet.netmask
supernet.network_address
net = str(supernet.network_address) + ' ' + str(supernet.netmask)

for subnet in network.subnets(prefixlen_diff=2):
    print(subnet)

for sn in supernet.subnets(new_prefix=24):
  available_subnets.append(str(sn))


  *Without Typecase into String
  >>> pprint(available_subnets)
[IPv4Network('192.168.0.0/24'),
 IPv4Network('192.168.1.0/24'),
 IPv4Network('192.168.2.0/24'),

 =====

 import ipaddress
 from pprint import pprint


dc_ip_scheme = {
 'dc_east': {'supernet': '10.100.0.0/18'},
 'dc_north': {'supernet': '10.100.128.0/18'},
 'dc_south': {'supernet': '10.100.192.0/18'},
 'dc_west': {'supernet': '10.100.64.0/18'}
 }


>>> supernet = ipaddress.IPv4Network("10.100.0.0/16")
>>> for s in supernet.subnets(prefixlen_diff=2):
...     print(s)
... 
10.100.0.0/18
10.100.64.0/18
10.100.128.0/18
10.100.192.0/18

 ipaddress.IPv4Network(dc_ip_scheme['dc_east']['supernet']).subnets(new_prefix=24)

r


for key in dc_ip_scheme.keys():
    print(type(ipaddress.IPv4Network(dc_ip_scheme[key]['supernet'])))

import json
from pprint import pprint
with open("dc_address_plan_original.json", 'r') as file:
    dc_address_plan = json.load(file)


requirement = "R1234"
allocation = {}
for dc in dc_address_plan.keys():
    for subnet, status in dc_address_plan[dc].items():
        if status != 'available':
            continue
        elif status == 'available':
            allocation[dc] = subnet
            dc_address_plan[dc][subnet] = ['reserved', requirement, ]
            break
        


{'east': '10.100.0.0/26',
 'north': '10.100.128.0/26',
 'south': '10.100.192.0/26',
 'west': '10.100.64.0/26'}

message = """
########################################################
For R1234 you have reserved the following address space: 
East DC: {allocation['east']}
West DC: {allocation['west']} 
North DC: {allocation['north']} 
South DC: {allocation['south']} 
########################################################
"""

now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))


+++++
dc_vlan_plan = {}
for item in datacenters