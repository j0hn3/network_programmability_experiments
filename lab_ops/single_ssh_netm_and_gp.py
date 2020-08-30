from netmiko import ConnectHandler

def ssh_session_via_netmiko_and_getpass(device_name, device_attributes):
#this functon takes a device name and a dict of its attributes,  and attempts to open an ssh session
#with the devive using netmiko, the ssh connection (net_connect or Flase if the attempt fails) is
#added to the dict of device attributes under the key ssh_con and the device attributes are returned
#if the ssh connection fails it is marked as a boolean False for later parsing
#examle: for device in inventory.keys):
#if device_name['ssh_con'] == False: break

    device_info = {
    "device_type": device_name['device_type'],
    "host": device_name['mgmt-ip'],
    "username": getpass.getpass('Username:'),
    "password": getpass.getpass(),
    }
    #build a dictionary of device attributes for netmiko to use to connect
    try:
        net_connect = ConnectHandler(**device_info)
    except:
        net_connect = False
    #try to connect to the device via ssh if it suceeds name the connection net_connect
    #if it fails mark net_connect equal to False
    #this is used later to determine if the ssh session was established or not
    device_attributes['ssh_con'] = net_connect
    return device_attributes
