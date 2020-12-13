#!/usr/bin/env python3
import jinja2
import os
import yaml
import datetime

#open the network topology yaml file as a dictionary 
file = open('./vsrx-baseline.yaml', 'r')
topology = yaml.load(file)
file.close()

#tell jinja2 to load templates from the pwd and specify the tempate to be used
loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = jenv.get_template('vsrx-baseline.j2')

#specify the output directory path, leaving the router name to be defined later by .format()
output_dir = '/home/lab-admin/lab/device-configs/{router}/baseline_config/'

#generate a iso8601_basic_short timestamp to be used later to name the output file
now = datetime.datetime.now()
timestamp = now.strftime('%Y%m%d%H%M%S')

#specify the output file, leaving the router and file name to be defined later by .format()
output_file = '/home/lab-admin/lab/device-configs/{router}/baseline_config/{timestamp}.set'

#Create a status message leaving the router name to be defined later by .format()
status_message = 'Configuration file for {router} created'

#create a list of all keys (router names) in the topology file
#this will be looped through for tempplate geneateion and used to ref the topology dict later
routers = [router for router in topology['routers'].keys()]

#loop through the list of routers previously generated, render and save a config for it
for router in routers:

    #render the config using the jinja2 template    
    output = template.render(topology, rtr=router)

    #validate the output directory exists, if it doesnt create it
    #ref: https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
    if not os.path.exists(output_dir.format(router=router)):
        os.makedirs(output_dir.format(router=router))

    #save the output to a file
    file = open (output_file.format(router=router, timestamp=timestamp), 'w')
    file.write(output) 
    file.close

    #print a status message each time a config is rendered and saved 
    print(status_message.format(router=router))


'''
This script will geneate a baseline config and save it in the device specific directory
for each router in the topology 
'''