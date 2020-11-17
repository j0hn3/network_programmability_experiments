#Ref: https://vimeo.com/120005103
#CAPITAL LETTERS should be replace by actual vars

import jinja2
import os

loader = jinja2.FileSystemLoader(os.getcwd())
#set loader to working directory 

jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
#set the j2 enviorment 

template = jenv.get_template('TEMPLATE_NAME.j2')
#open the j2 template from the pwd

print(template.render(J2_TEMPLATE_VAR=PYTHON_VAR, J2_TEMPLATE_VAR=DATA))
#render returns a string 
#EXAMPLE: REMOTE_ROUTER_NAME='vsrx-rtr-02'