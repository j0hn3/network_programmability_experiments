import ipaddress
import json


###input Vars to generate DC IP scheme with###
all_dcs_supernet = "10.100.0.0/16" 
#supernet to be divided among all DCs
per_dc_supernet = 18 
#CIDR for per DC supernet
prefix_for_dc_subnets = 27 
#CIDR for host subnet in each DC
datacenters = ['east', 'west', 'north', 'south', ] 
#names of datacenters
output_file_name = 'dc_address_plan.json'
#file name to write results
backup_output_file_name = 'dc_address_plan_original.json'
#file name to write results

###script###

VLANS = list(range(1005,4095))
#generate a list of extended range VLANS

supernet = ipaddress.IPv4Network(all_dcs_supernet)
#typecast supernet into ipaddress.network object

dc_supernets = [str(s) for s in supernet.subnets(new_prefix = per_dc_supernet)]
#create a list of supernets for each dc from all_dcs_supernet

dc_ip_scheme = {'datacenters': {} }
#create dict to store address plan

for item in range(len(datacenters)):
    dc_ip_scheme['datacenters'][datacenters[item]] = {'supernet' : dc_supernets[item]} 
    dc_ip_scheme['datacenters'][datacenters[item]]['IPv4_Addresses'] = {}

#for item in range(len(datacenters)):
#    dc_ip_scheme[datacenters[item]]= {'supernet' : dc_supernets[item]}
#add data to the dc_ip_scheme in the following format dc_ip_scheme{ datacenter { supernet :  dc_supernet }}

for dc in dc_ip_scheme['datacenters'].keys():
    networks =  ipaddress.IPv4Network(dc_ip_scheme['datacenters'][dc]['supernet']).subnets(new_prefix = prefix_for_dc_subnets)
    for ip in networks:
       dc_ip_scheme['datacenters'][dc]['IPv4_Addresses'][str(ip)] = 'available'
#add a list of all the /24s in the supernet assigned to each dc 
#format is dc_ip_scheme[dc][subnet] =  'available'
#available assigned as value as it will be changed later when allocated 

for dc in dc_ip_scheme['datacenters'].keys():
    dc_ip_scheme['datacenters'][dc]['VLANS'] = {}
    for VLAN in VLANS:
        dc_ip_scheme['datacenters'][dc]['VLANS'][VLAN] = 'available'

dc_ip_scheme['update_log'] = {}
#create a new dictionary entry to track updates 

with open(output_file_name, 'w') as file:
    file.write(json.dumps(dc_ip_scheme, indent=4))
#create the json file to store the working copy of the address scheme 

with open(backup_output_file_name, 'w') as file:
    file.write(json.dumps(dc_ip_scheme, indent=4))
#create the json file to store a backup copy of the address scheme 