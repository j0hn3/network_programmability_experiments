#!/usr/local/bin/python3.7

import l3vpn_config_ops as config_ops 
import l3vpn_customer_ops as customer_ops
import l3vpn_file_ops as file_ops 

if __name__ == "__main__":

    customer_info = customer_ops.get_customer_vars()
    #get information from the customer needed to deploy this new service

    file_ops.write_yaml_file(customer_info,'l3vpn_customer_vars.yaml')
    #save the customer info as a yaml file
    #this is done for extensibility so later this information can be ingested from other
    #sources instead of the l3vpn_customer_ops module 


    pe_config = {}
    for device in customer_info['site_devices']:
        device_name = device
        pe_config[device] = config_ops.render_device_configurations()

    #config is loosing its spacing example below, need to rethink how config data is moved or saved
    # >>> print(pe_config['csr1000v-rtr-01'])
    #vrf definition VPN_1234 rd 1000:1234 address-family ipv4 route-target export 1000:1234 route-target import 1000:1234 exit-address-family
    #interface Loopback1234 description VPN_1234 CUSTOMER vrf forwarding VPN_1234 ip address  
    #router bgp 1000 address-family ipv4 vrf VPN_1234 redistribute connected exit-address-family  
  
    #create a dictionary to store the generated configs
    #for each device at the site generate the needed configuration

    #config ops deploy each configuration

