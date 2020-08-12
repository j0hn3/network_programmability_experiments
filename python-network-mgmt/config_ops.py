def vlan_configs(vlan_allocation, req):
    vlan_config = ''

    for dc, vlan in vlan_allocation.items():
    #for each datacenter and vlan in the allocation generate the following multi-line string
        vlan_template = f"""
        
    ###Datacenter: {dc}

    #{dc}.sw01
    vlan {vlan}
    description {req}
    no shutdown

    #{dc}.sw02
    vlan {vlan}
    description {req}
    no shutdown
++++++++++++++++++++++++++++++++

    """
        vlan_config += vlan_template
        #append the multi-line string generated from the template to a string containing the entire config

    return vlan_config

#####

def ip_configs(ip_allocation, vlan_allocation, req):
    ip_config = ''
    for dc, subnet in ip_allocation.items():
    #for each datacenter and subnet in the allocation generate the following multi-line string
        svi = vlan_allocation[dc]   
        ip_template = f"""
    ###Datacenter {dc}
    
    #{dc}.rtr.01

    interface {svi}
    ip address {subnet}
    description {req}
    no shutdown

    router ospf 100
    network {subnet}

    ip prefix-list DATACENTER_{dc.upper()}_ACTIVE_SUBNETS add {subnet}
    
    #{dc}.rtr.02

    interface {svi}
    ip address {subnet}
    description {req}
    no shutdown

    router ospf 100
    network {subnet}

    ip prefix-list DATACENTER_{dc.upper()}_ACTIVE_SUBNETS add {subnet}

    ++++++++++++++++++++++++++++++++
    
    """
        ip_config += ip_template
        #append the multi-line string generated from the template to a string containing the entire config

    return ip_config

#####
