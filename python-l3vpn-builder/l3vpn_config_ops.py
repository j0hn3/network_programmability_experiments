import ipaddress
import yaml
from jinja2 import Template
import l3vpn_file_ops as file_ops

def generate_l3vpn_jinja2_vars():
#take the information from the customer and parse it into the vars
#needed to generate the vars needed to build the l3vpn config 
    customer_info = file_ops.read_yaml_file('l3vpn_customer_vars.yaml')
    customer_number = str(customer_info['customer_number'])
    internal_asn = str(customer_info['internal_asn'])

    vpn_name = "VPN_"
    vpn_name  += customer_number

    rd = internal_asn + ":" + customer_number

    rt_export = internal_asn + ":" + customer_number
    rt_import = internal_asn + ":" + customer_number
    #standard import and export policy


    customer_subnet = ipaddress.IPv4Network(customer_info['customer_subnet'])
    #convert customer input into IP address object
    customer_ips = []
    for ip in customer_subnet.hosts():
        customer_ips.append(str(ip))
    first_useable_customer_ip = str(customer_ips[0])
    first_useable_customer_mask = str(customer_subnet.netmask)

    #format the data into a dictionary to be used by jinja2 to render the config
    customer_vars = {
       'vpn_name': vpn_name,
       'rd': rd,
       'rt_export': rt_export,
       'rt_import': rt_import,
       'customer_number': customer_number,
       'first_useable_customer_ip': first_useable_customer_ip,
       'first_useable_customer_mask': first_useable_customer_mask,
       'internal_asn': internal_asn,
    }

    return customer_vars 

def render_device_configurations():
    template = file_ops.read_yaml_file('l3vpn_customer_template.jinja2')
    pe_j2_template = Template(template)
    #open the template file and typecast it as a jinja2 template 

    customer_vars = generate_l3vpn_jinja2_vars()
    #generate the customer variables for the jinja2 template 

    pe_config = pe_j2_template.render(customer_vars)
    #render the pe configuration 
    
    print(pe_config)

    return pe_config 


