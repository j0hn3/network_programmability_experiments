import ipaddress
import jinja2
import l3vpn_customer_vars as cx

def generate_l3vpn_jinja2_vars():
    customer_number = str(cx.customer_number)

    internal_asn = str(cx.internal_asn)

    vpn_name = "VPN_"
    vpn_name  += customer_number

    rd = internal_asn + ":" + customer_number

    rt_export = internal_asn + ":" + customer_number
    rt_import = internal_asn + ":" + customer_number
    #standard import and export policy


    customer_subnet = ipaddress.IPv4Network(cx.customer_subnet)
    #convert customer input into IP address object
    customer_ips = []
    for ip in customer_subnet.hosts():
        customer_ips.append(str(ip))
    first_useable_customer_ip = str(customer_ips[0])
    first_useable_customer_mask = str(customer_subnet.netmask)

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