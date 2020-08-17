#!/usr/local/bin/python3.7
import lab_file_ops
import lab_device_ops

if __name__ == "__main__":
    lab_inventory = lab_file_ops.read_json_files('./device_info/inventory/', 'lab_device_inventory.json')

