from netmiko import ConnectHandler

def open_ssh_con(inventory):
#open an ssh connection to each device marked as reachable in the inventory and ...
#return and updated inventory
    
    #inventory = ping_device(inventory)
    ##verify which lab devices are reachable using the ping_device function

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