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
   pprint(available_subnets)
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


 supernet = ipaddress.IPv4Network("10.100.0.0/16")
 for s in supernet.subnets(prefixlen_diff=2):
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

+++++

from jinja2 import Template
Template() function to create our template object
template.render()


 from jinja2 import Template
 ipaddr_template = Template(' {{interface}} has IP address {{ip_address}}') 
 print(ipaddr_template)
<Template memory:7fd508a5fe90>
 interface_1 = ipaddr_template.render(interface='ge-0/0/0', ip_address='192.168.1.1')
 print(interface_1)
 ge-0/0/0 has IP address 192.168.1.1
 print(type(interface_1))
<type 'unicode'>
 print(str(interface_1))
 ge-0/0/0 has IP address 192.168.1.1


 try:
    if os.path.isfile(path):
        return None # or print and error, or pass etc...
    else:
        with open(path, 'w') as outFile:
            outFile.write(text)
        except IOError as exception:
            raise IOError("%s: %s" % (path, exception.strerror))


try:
    os.mkdir(path)
except FileExistsError:

def write(self, path, text):
    try:
        if os.path.isfile(path):
            return None # or print and error, or pass etc...
        else:
            with open(path, 'w') as outFile:
                outFile.write(text)
    except IOError as exception:
        raise IOError("%s: %s" % (path, exception.strerror))
    return None

def create_folder(path):
    try:
        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)
    except IOError as exception:
        raise IOError('%s: %s' % (path, exception.strerror))
    return None


bl = '\n'
names = ['john', 'jordan', 'steve']
greeting_list = ''
for name in names:
    greeting_list += f"Hello {name}"
    greeting_list += bl

print(greeting_list)
>>> print(greeting_list)
Hello john
Hello jordan
Hello steve



bl = '\n'
names = ['john', 'jordan', 'steve']
greeting_list = ''
for name in names:
    greeting_list += f"""
    Hello {name.title()}"""

print(greeting_list)

>>> print(greeting_list)

    Hello john
    Hello jordan
    Hello steve


{vlan_allocation[{dc}]}

dc = 'east'
subnet = '10.100.0.32/27'
req = 'R1234'
vlan_allocation = {'east': '1006'}
int_dc = vlan_allocation[dc]

ip_template = f"""
    ###Datacenter {dc}
    
    #{dc}.rtr.01

    interface 1/1/1
    ip address {subnet}
    description {req}
    no shutdown

    router ospf 100
    network {subnet}

    ip prefix-list DATACENTER_ACTIVE_SUBNETS add {subnet}
    
    #{dc}.rtr.02

    interface vlan {int_dc}
    ip address {subnet}
    description {req}
    no shutdown

    router ospf 100
    network {subnet}

    ip prefix-list DATACENTER_{dc.upper()}_ACTIVE_SUBNETS add {subnet}

    ++++++++++++++++++++++++++++++++
    
    """