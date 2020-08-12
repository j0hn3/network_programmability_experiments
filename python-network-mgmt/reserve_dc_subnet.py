import json
import datetime
import pwd
import os
import file_ops
import config_ops
import print_ops

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


if __name__ == "__main__":
    req = get_req()
    #get a requirement number for the allocation

    username = pwd.getpwuid(os.getuid()).pw_name
    #get the name of the user logged into the system running this script
    #ref: https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python

    dc_address_plan = file_ops.read_json_files('./dc_address_plan/', 'dc_address_plan.json')
    #open the file containaining the address plan for the dc usinf file_ops

    dc_address_plan, ip_allocation = reserve_subnet( dc_address_plan, req )
    #reserve the first available subnet at each DC

    dc_address_plan, vlan_allocation = reserve_vlan( dc_address_plan, req )
    #reserve VLANS in the address plan

    dc_address_plan = append_update_log(dc_address_plan, req, username)
    #update the update_log in the address plan for the allocation just made

    file_ops.write_files_as_json(dc_address_plan, './dc_address_plan/', 'dc_address_plan.json')
    #save the updated address plan for the dc using file_ops

    print_ops.print_allocation(req, ip_allocation, vlan_allocation, './dc_network_configs/')
    #print the reservations for the user

    vlan_config = config_ops.vlan_configs(vlan_allocation, req)
    ip_config = config_ops.ip_configs(ip_allocation, vlan_allocation, req)
    #generate configurations based on the allocations

    file_ops.create_folder('./dc_network_configs/')
    ip_config_file_name = req
    ip_config_file_name += '_ip_config.txt'
    #assemble file name for ip_configs
    file_ops.write_string('./dc_network_configs/', ip_config_file_name, ip_config)

    vlan_config_file_name = req
    vlan_config_file_name += '_vlan_config.txt'
    #assemble file name for vlan_configs
    file_ops.write_string('./dc_network_configs/', vlan_config_file_name, vlan_config)
    #write the configurations to the dc_configs directory