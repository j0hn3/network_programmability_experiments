#!/usr/local/bin/python3.7
from netmiko import ConnectHandler
import re
import lab_file_ops

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


def backup_all_devices():
#this takes the lab_device_backup and converts it into a module in lab_device_ops
    lab_inventory = lab_file_ops.read_json_files('./device_info/inventory/', 'lab_device_inventory.json')
    #open the lab inventory
    lab_inventory = open_ssh_con(lab_inventory)
    #attempt to establish ssh connections to all lab devices
    #devices whcih cannot have an ssh connection opnened will have (ssh_con = False)
    
    lab_inventory = type_run_show_cmd_raw_output(lab_inventory, 'cisco_ios', 'show run')
    #backup the running configuraiton of cisco_ios devices via show run
    #save the output in the devices folder in device_info/device_configs 
    #the name of the file will be unique and use a timestamp for when the config was saved
    for dev in lab_inventory.keys():
        user_id, now = lab_file_ops.gen_timestamp()
        if lab_inventory[dev]['netmiko-type'] == 'cisco_ios':
            if lab_inventory[dev]['ssh_con'] != False:
            #for every lab device of type cisco_ios with an active ssh connection 
                output_file_path = f'./device_info/device_configs/{dev}/'
                #path to save file
                output_file_name = f'{dev}_{now}.txt'
                #create file name based on device name and timestamp
                output_file_data = lab_inventory[dev]['show run']
                #create a string to hold the output for formatting
                output_file_data= output_file_data.strip()
                #strip off whitespace at the beginning and end of the file
                output_file_data = re.sub(r'.*!.?\n', '', output_file_data)
                #remove all lines with only ! or ! and spaces
                output_file_data = re.sub(r'(\n)(\n+)', '\n', output_file_data)
                #replace multiple empty lines with a single one 
                lab_file_ops.write_string(output_file_path, output_file_name, output_file_data)
                #write the output to a file using file_ops

    lab_inventory = type_run_show_cmd_raw_output(lab_inventory, 'arista_eos', 'show run')
    #backup the running configuraiton of arista_eos devices via show run
    #save the output in the devices folder in device_info/device_configs 
    #the name of the file will be unique and use a timestamp for when the config was saved
    for dev in lab_inventory.keys():
        user_id, now = lab_file_ops.gen_timestamp()
        if lab_inventory[dev]['netmiko-type'] == 'arista_eos':
            if lab_inventory[dev]['ssh_con'] != False:
            #for every lab device of type arista_eos with an active ssh connection 
                output_file_path = f'./device_info/device_configs/{dev}/'
                #path to save file
                output_file_name = f'{dev}_{now}.txt'
                #create file name based on device name and timestamp
                output_file_data = lab_inventory[dev]['show run']
                #create a string to hold the output for formatting
                output_file_data= output_file_data.strip()
                #strip off whitespace at the beginning and end of the file
                lab_file_ops.write_string(output_file_path, output_file_name, output_file_data)
                #write the output to a file using file_ops

    close_ssh_con(lab_inventory)
    #close all open ssh sessions