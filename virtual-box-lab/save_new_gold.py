#!/usr/local/bin/python3.7
import lab_device_ops

if __name__ == "__main__":
    device = input("Enter device name (case sensitive):")
    lab_device_ops.save_new_gold_config(device)
    #currently only supports cisco devices