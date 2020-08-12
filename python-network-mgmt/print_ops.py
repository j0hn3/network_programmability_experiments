def print_allocation(req, ip_allocation, vlan_allocation, config_location):
    print(f"""
    ########################################################
    For {req} you have reserved the following address space: 

    Network Configurations can be found in the {config_location} folder
    
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

