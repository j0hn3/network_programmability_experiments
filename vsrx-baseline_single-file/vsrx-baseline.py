#!/usr/bin/env python3
import jinja2
import os
import yaml

file = open('./vsrx-baseline.yaml', 'r')
topology = yaml.load(file)
file.close()

loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = jenv.get_template('vsrx-baseline.j2')
output = template.render(topology)
print(output)

file = open ('./vsrx-baseline.set', 'w')
file.write(output) 
file.close


"""
- this script will generate a single .set file containing a baseline config for all vsrx 
devices based on the .j2 and .yaml files in the pwd
- the .yaml file contains the base os conifs and interface topology
- the .j2 template file renders a configuration based on the .yaml file
"""