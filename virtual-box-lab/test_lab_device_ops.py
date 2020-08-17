#!/usr/local/bin/python3.7

import lab_device_ops

if __name__ == "__main__":

    inventory = {
        "csr1000v-rtr-01-up": {
            "mgmt-ip": "192.168.255.131",
            "netmiko-type": "cisco_ios",
            "lab-user": "lab-admin",
            "lab-pass": "En@ble123"
        },
        "csr1000v-rtr-02-down": {
            "mgmt-ip": "192.168.255.254",
            "netmiko-type": "cisco_ios",
            "lab-user": "lab-admin",
            "lab-pass": "En@ble123"
        }
    }

    

    print('\n\n\n+++++')
    print("TESTING: lab_device_ops.open_ssh_con")
    inventory = lab_device_ops.open_ssh_con(inventory)

    for dev in inventory.keys():
        if dev == 'csr1000v-rtr-01-up' and inventory[dev]['ssh_con'].find_prompt() == 'csr1000v-rtr-01#':
            print('PASS: ssh session opened for', dev)
        elif dev == 'csr1000v-rtr-02-down' and inventory[dev]['ssh_con'] == False:
            print('PASS: opening ssh session for', dev, "failed sucessfully")
        else:
            print('FAIL: Something went wrong check the test cases our output data')
            print('Data Returned:\n', inventory)

    print(('\n'))
    print("TESTING: lab_device_ops.close_ssh_con")
    inventory = lab_device_ops.close_ssh_con(inventory)
    for dev in inventory.keys():
        if inventory[dev]['ssh_con'] != False:
            print('FAIL: ssh session for', dev, 'is STILL alive !!!')
        else:
            print('PASS: ssh session for', dev, 'is closed')

    print(('+++++\n'))