import jinja2
import os
import json


file = open('./vsrx-rtr-00-interfaces.json', 'r')
vsrx_inventory = json.load(file)
file.close()


loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = jenv.get_template('vsrx-interface-template-rev2.j2')

for rtr in vsrx_inventory.keys():
    print('!', vsrx_inventory[rtr]['local_router_hostname'], sep='')
    for link in vsrx_inventory[rtr]['data_links'].keys():
        print(template.render(LINK_ID=link, 
        LOCAL_ROUTER_NUMBER=vsrx_inventory[rtr]['local_router_number'], 
        ROUTERS_ON_SEGMENT=vsrx_inventory[rtr]['data_links'][link]['dest'],
        LINK_TYPE=vsrx_inventory[rtr]['data_links'][link]['type']))