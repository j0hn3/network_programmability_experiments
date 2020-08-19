from netmiko import ConnectHandler

def open_ssh_con(inventory):
#open an ssh connection to each device marked as reachable in the inventory and ...
#return and updated inventory

    for device in inventory.keys():
        device_info = {
            "device_type": inventory[device]['netmiko-type'],
            "host": inventory[device]['mgmt-ip'],
            "username": inventory[device]['lab-user'],
            "password": inventory[device]['lab-pass'],
        }
        try:
            net_connect = ConnectHandler(**device_info)
        except:
            net_connect = False
        #try to connect to the device via ssh, if it fails mark net_connect as false 
        #this is used later to determine if the ssh connecton is alive or not
        
        try:
            net_connect.enable()
        except:
            pass
        #try to enter privilidged mode if the device type supports it

        inventory[device]['ssh_con'] = net_connect

    return inventory

def close_ssh_con(inventory):
#for all devices with an active ssh connection...
#disconnect it and update the inventory for that device to false
    for device in inventory.keys():
        if inventory[device]['ssh_con'] != False:
            inventory[device]['ssh_con'].disconnect()
            inventory[device]['ssh_con'] = False
    
    return inventory

def device_run_show_cmd_raw_output(inventory, device, command):
#run a show command against a device and return the outout as raw text
    output = inventory['device']['ssh_con'].send_command(command)
    inventory['device'][command] = output
    return inventory

def device_run_show_cmd_textfsm_output(inventory, device, command):
#run a show command against a device and return the output parsed using textfsm    
    output = inventory['device']['ssh_con'].send_command(command, use_textfsm=True)
    inventory['device'][command] = output
    return inventory

def type_run_show_cmd_raw_output(inventory, device_type, command):
#run a show commands against a type of device (cisco_ios etc) 
#return the raw output
    for dev in inventory.keys():
        if device_type == inventory[dev]['netmiko-type']:
            if inventory[dev]['ssh_con'] != False:
            #if the ssh connection has not failed and is = False
                output = inventory[dev]['ssh_con'].send_command(command)
                inventory[dev][command] = output
    return inventory

