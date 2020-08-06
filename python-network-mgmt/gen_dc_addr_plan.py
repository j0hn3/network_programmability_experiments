import ipaddress
import json


###input Vars to generate DC IP scheme with###
all_dcs_supernet = "10.100.0.0/16" 
#supernet to be divided among all DCs
per_dc_supernet = 18 
#CIDR for per DC supernet
prefix_for_dc_subnets = 26 
#CIDR for host subnet in each DC
datacenters = ['east', 'west', 'north', 'south', ] 
#names of datacenters
output_file_name = 'dc_address_plan_original.json'
#file name to write results to

###script###

supernet = ipaddress.IPv4Network(all_dcs_supernet)
#typecast supernet into ipaddress.network object

dc_supernets = [str(s) for s in supernet.subnets(new_prefix = per_dc_supernet)]
#create a list of supernets for each dc from all_dcs_supernet

dc_ip_scheme = {}
#create dict to store address plan

for item in range(len(datacenters)):
    dc_ip_scheme[datacenters[item]] = {'supernet' : dc_supernets[item]}
#add data to the dc_ip_scheme in the following format dc_ip_scheme{ datacenter { supernet :  dc_supernet }}

for dc in dc_ip_scheme.keys():
    networks =  ipaddress.IPv4Network(dc_ip_scheme[dc]['supernet']).subnets(new_prefix = prefix_for_dc_subnets)
    for ip in networks:
       dc_ip_scheme[dc][str(ip)] = 'available'
#add a list of all the /24s in the supernet assigned to each dc 
#format is dc_ip_scheme[dc][subnet] =  'available'
#available assigned as value as it will be changed later when allocated 

with open(output_file_name, 'w') as file:
    file.write(json.dumps(dc_ip_scheme, indent=4))
#create the json file dc_address_plan_original.json based on the dc_ip_scheme dictionary