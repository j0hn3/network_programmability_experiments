def vlan_configs(vlan_allocation, req)
    vlan_config = ''
    
    vlan_template = f"""Datacenter {dc}

    {dc}.sw01
    vlan {vlan}
    description {req}
    no shutdown

    {dc}.sw02
    vlan {vlan}
    description {req}
    no shutdown

    """

    for dc, vlan in vlan_allocation.items():



def ip_configs(ip_allocation, vlan_allocation, req)
    ip_config = ''

    ip_template = f"""Datacenter {dc}
    {dc}.rtr.01

    interface {vlan_allocation[{dc}]}
    ip address {subnet}
    description {req}
    no shutdown

    router ospf 100
    network {subnet}

    ip prefix-list DATACENTER_{DC.upper()}_ACTIVE_SUBNETS add {subnet}

    """

    for dc, subnet in ip_allocation.items():

