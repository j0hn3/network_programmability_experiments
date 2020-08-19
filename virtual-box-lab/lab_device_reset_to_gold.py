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