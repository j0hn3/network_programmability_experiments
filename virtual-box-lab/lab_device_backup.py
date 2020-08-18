#!/usr/local/bin/python3.7
import lab_file_ops
import lab_device_ops
import re

if __name__ == "__main__":
    lab_inventory = lab_file_ops.read_json_files('./device_info/inventory/', 'lab_device_inventory.json')
    lab_inventory = lab_device_ops.open_ssh_con(lab_inventory)
    
    #backup the running configuraiton of cisco_ios devices via show run
    #save the output in the devices folder in device_info/device_configs 
    #the name of the file will be unique and use a timestamp for when the config was saved
    lab_inventory = lab_device_ops.type_run_show_cmd_raw_output(lab_inventory, 'cisco_ios', 'show run')
    for dev in lab_inventory.keys():
        user_id, now = lab_file_ops.gen_timestamp()
        if lab_inventory[dev]['netmiko-type'] == 'cisco_ios':
            if lab_inventory[dev]['ssh_con'] != False:
                output_file_path = f'./device_info/device_configs/{dev}/'
                output_file_name = f'{dev}_{now}.txt'
                output_file_data = lab_inventory[dev]['show run']
                output_file_data = output_file_data.replace('!\n', '')
                #remove any lines with only a !
                output_file_data = output_file_data.replace('! \n', '')
                #remove any lines with a ! followed by a space
                output_file_data = re.sub(r'^Building.*', '', output_file_data)
                #remove the Building configuration ... line
                output_file_data = output_file_data.replace('end', '')
                #remove the end statement from the bottom of the config
                output_file_data = re.sub(r'\n{2,}', '\n', output_file_data)
                #remove any blank lines
                lab_file_ops.write_string(output_file_path, output_file_name, output_file_data)

    lab_device_ops.close_ssh_con(lab_inventory)