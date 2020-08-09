import json
import datetime

def get_req():
    req = int(input("Enter a Requrement number for this allocation: "))
    req = "R" + str(req)
    return req

def open_address_scheme(file_name = 'dc_address_plan.json'):
#open a a file containing the ip address scheme in JSON format and return a dictionary
    with open(file_name, 'r') as file:
        dc_address_plan = json.load(file)
    return dc_address_plan

def reserve_subnet( dc_address_plan, req ):
    ip_allocation = {}
    #create a dict to store a copy subnets allocated in the format {dc:network} 
    for dc in dc_address_plan['datacenters'].keys():
        for subnet, status in dc_address_plan['datacenters'][dc]['IPv4_Addresses'].items():
        #for each dc loop through all the enties until you find the first subnet (key) which has a value of 'available'
            if status != 'available':
                continue
            elif status == 'available':
                ip_allocation[dc] = subnet
                dc_address_plan['datacenters'][dc]['IPv4_Addresses'][subnet] = ['reserved', req, ]
                break
    return dc_address_plan, ip_allocation

def reserve_vlan( dc_address_plan, req ):
    vlan_allocation = {}
    for dc in dc_address_plan['datacenters'].keys():
        for vlan, status in dc_address_plan['datacenters'][dc]['VLANS'].items():
        #for each dc loop through all the enties until you find the first subnet (key) which has a value of 'available'
            if status != 'available':
                continue
            elif status == 'available':
                vlan_allocation[dc] = vlan
                dc_address_plan['datacenters'][dc]['VLANS'][vlan] = ['reserved', req, ]
                break
    return dc_address_plan, vlan_allocation


def save_address_scheme(dc_address_plan, req, file_name = 'dc_address_plan.json'):
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    dc_address_plan['update_log'][req] = now
    with open(file_name, 'w') as file:
        file.write(json.dumps(dc_address_plan, indent=4))



def print_allocation(req, ip_allocation, vlan_allocation):
    print(f"""
    ########################################################
    For {req} you have reserved the following address space: 
    
    East DC 
    Subnet: {ip_allocation['east']} 
    VLAN: {vlan_allocation['east']}

    West DC 
    Subnet: {ip_allocation['west']}
    VLAN: {vlan_allocation['west']}

    North DC 
    Subnet: {ip_allocation['north']}
    VLAN: {vlan_allocation['north']} 

    South DC
    Subnet: {ip_allocation['south']}
    VLAN: {vlan_allocation['south']}
    ########################################################
    """)


if __name__ == "__main__":
    req = get_req()
    #get a requirement number for the allocation
    dc_address_plan = open_address_scheme()
    #open the file containaining the address plan for the dc
    dc_address_plan, ip_allocation = reserve_subnet( dc_address_plan, req )
    #reserve the first available subnet at each DC
    dc_address_plan, vlan_allocation = reserve_vlan( dc_address_plan, req )
    print(vlan_allocation)
    dc_address_plan, save_address_scheme(dc_address_plan, req)
    #save the updated address plan for the dc
    print_allocation(req, ip_allocation, vlan_allocation)
    #print the reserved subnets