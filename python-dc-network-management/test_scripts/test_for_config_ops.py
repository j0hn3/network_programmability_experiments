ip_allocation = {
'east': '10.100.0.32/27',
'west': '10.100.64.32/27',
'north': '10.100.128.32/27',
'south': '10.100.192.32/27'
}

vlan_allocation = {
'east': '1006',
'west': '1006',
'north': '1006',
'south': '1006'
}

req = "R1234"

import config_ops
vlan_config = config_ops(vlan_allocation, req)
ip_config = config_ops.ip_configs(ip_allocation, vlan_allocation, req)

print(vlan_config)
print("\n\n\n")
print(ip_config)