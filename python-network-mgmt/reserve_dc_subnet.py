import json
import datetime
import pwd
import os
import file_ops

def get_req():
    req = int(input("Enter a Requrement number for this allocation: "))
    req = "R" + str(req)
    return req    

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


def append_update_log(dc_address_plan, req, username ):
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    dc_address_plan['update_log'][req] = {'time': now, 'user_id': username}
    return dc_address_plan



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

    username = pwd.getpwuid(os.getuid()).pw_name
    #get the name of the user logged into the system running this script

    dc_address_plan = file_ops.read_json_files('./dc_address_plan/', 'dc_address_plan.json')
    #open the file containaining the address plan for the dc usinf file_ops

    dc_address_plan, ip_allocation = reserve_subnet( dc_address_plan, req )
    #reserve the first available subnet at each DC

    dc_address_plan, vlan_allocation = reserve_vlan( dc_address_plan, req )
    #reserve VLANS in the address plan

    dc_address_plan = append_update_log(dc_address_plan, req, username)

    file_ops.write_files_as_json(dc_address_plan, './dc_address_plan/', 'dc_address_plan.json')
    #save the updated address plan for the dc using file_ops

    print_allocation(req, ip_allocation, vlan_allocation)
    #print the reserved subnets