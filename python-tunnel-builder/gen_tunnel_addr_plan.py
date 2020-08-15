#!/usr/local/bin/python3.7

import ipaddress
import tunnel_addr_plan_input_vars
import file_ops

if __name__ == "__main__":
 
    tunnel_supernet = ipaddress.IPv4Network(tunnel_addr_plan_input_vars.tunnel_supernet)
    #typecast tunnel_supernet from input vars into an ipv4 address network object

    tunnel_subnets = [str(s) for s in tunnel_supernet.subnets(new_prefix = 31)]
    #create a list of /31 subnets from the tunnel supernet 

    tunnel_address_plan = {'subnets': {}, 'update_log': {} }
    #create a dict that will be output as a json file

    tunnel_address_plan['subnets']  = {str(subnet) : 'available' for subnet in tunnel_subnets }
    #populate the subnets dictionary using a comprehension to store the subnets and their status
    #the key is cast as a string from the items in tunnel_subnets as ipaddress objects not writeable in json
    #the value will be 'available'
    #tunnel_address_plan {subnets : { subnet as string : 'available' }

    user_id, now = file_ops.gen_timestamp()
    #get the userid and timestamp using file_ops
    tunnel_address_plan['update_log']['created'] = {'user': user_id, 'timestamp': now}
    #update the tunnel_address_plan['update_log'] dict with who created the file and when
    #tunnel_address_plan{ update_log{req/created :{user : userid, timestamp : date & time }}}

    file_ops.write_files_as_json( 
        tunnel_address_plan, 
        tunnel_addr_plan_input_vars.output_file_directory,
        tunnel_addr_plan_input_vars.output_file_name,
        )
    #write tunnel_address_plan as a json file using file_ops
    

   