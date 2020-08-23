import l3vpn_file_ops as file_ops 

def site_lookup(customer_info):
    #look up the site provided by the customer and return the asn and deviecs
    network_inventory = file_ops.read_json_file('./network_inventory/', 'virtual_box_network.json')
    #open the network inventory
    if customer_info['customer_site'] == 'virtual_box_lab':
    #based on the customer site specificed provide the asn and the site devices
        customer_info['internal_asn'] = network_inventory['asn']
        customer_info['site_devices'] = network_inventory['site_devices']
    return customer_info


def get_customer_vars():
    customer_number = int(input("Customer Number:"))
    #customer_site = input("Enter site name:")
    #will automatically be input for now
    customer_site = 'virtual_box_lab'
    customer_subnet = input("Enter subnet for this site in CIDR notation:")
    customer_info = {
        'customer_number': customer_number,
        'customer_subnet': customer_subnet,
        'customer_site': customer_site,
    }
    customer_info = site_lookup(customer_info)
    return customer_info