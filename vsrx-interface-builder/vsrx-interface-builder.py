#!/usr/bin/env python3
import jinja2
import os
import json

#this script will genreate interface configurations for all vsrx lab devices
#in a format they can easily be copied and paste into the device via the cli

#open the vsrx-interfaces json file in the working pwd as a dict named vsrx_inventory
file = open('./vsrx-interfaces.json', 'r')
vsrx_inventory = json.load(file)
file.close()


loader = jinja2.FileSystemLoader(os.getcwd())
#set the loader to use the pwd
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
#set jenv enviorment varables to help with output
template = jenv.get_template('vsrx-interface-template.j2')
#specify the j2 template to use

##loop through all the interfaces for all the routers in the invetory and generate config for them
#for rtr in vsrx_inventory.keys():
#    print('\n!', vsrx_inventory[rtr]['local_router']['hostname'], sep='')
#    print('configure')
#    #seperate the intefaces for each dedvice with a newline !hostname
#    for link in vsrx_inventory[rtr]['data_links'].keys():
#        print(template.render(LINK_ID=link, 
#        LOCAL_ROUTER_NUMBER=vsrx_inventory[rtr]['local_router']['number'], 
#        ROUTERS_ON_SEGMENT=vsrx_inventory[rtr]['data_links'][link]['dest'],
#        LINK_TYPE=vsrx_inventory[rtr]['data_links'][link]['type']))
#    print('commit and-quit')

#loop through all the interfaces for all the routers in the invetory and generate config for them
output = ''
for rtr in vsrx_inventory.keys():
    output += ('\n!'+ vsrx_inventory[rtr]['local_router']['hostname']+'\n')
    output += ('configure\n')
    #seperate the intefaces for each dedvice with a newline !hostname
    for link in vsrx_inventory[rtr]['data_links'].keys():
        output += (template.render(LINK_ID=link, 
        LOCAL_ROUTER_NUMBER=vsrx_inventory[rtr]['local_router']['number'], 
        ROUTERS_ON_SEGMENT=vsrx_inventory[rtr]['data_links'][link]['dest'],
        LINK_TYPE=vsrx_inventory[rtr]['data_links'][link]['type']))
        output += '\n'
    output += ('commit and-quit')
    output += ('\n+++++++++++++++++++++++++++++++++++++++++')

file = open('./vsrx-interfaces.set', 'w')
file.write(output)
file.close
