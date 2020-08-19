#this was added into lab_device_ops as a function

#!/usr/local/bin/python3.7
import lab_file_ops
import lab_device_ops
import re

if __name__ == "__main__":
    lab_inventory = lab_file_ops.read_json_files('./device_info/inventory/', 'lab_device_inventory.json')
    #open the lab inventory
    lab_inventory = lab_device_ops.open_ssh_con(lab_inventory)
    #attempt to establish ssh connections to all lab devices
    #devices whcih cannot have an ssh connection opnened will have (ssh_con = False)
    
    lab_inventory = lab_device_ops.type_run_show_cmd_raw_output(lab_inventory, 'cisco_ios', 'show run')
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

    lab_inventory = lab_device_ops.type_run_show_cmd_raw_output(lab_inventory, 'arista_eos', 'show run')
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

    lab_device_ops.close_ssh_con(lab_inventory)
    #close all open ssh sessions