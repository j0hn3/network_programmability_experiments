# Network Programmability Experiments
This repo contains a variety of my personal experiments with network programability in various forms. 

## My To Do List

### DC Network mangement 
- generate configurations for each Allocation ( convert from fstring to jinja2 templates )
- format of req #s being taken as input
- automatic configuration for DC devices (paramiko and test device???)
- generate config for supernets at each DC and add them to routing (((as a summary address ???)
- store all user input as a configuration file wtih a specific methiod to capoture in
- write unit testing for scripts  

### tunnel Builder
- generate configurations for each Allocation ( convert from fstring to jinja2 templates )
- write unit testing for scripts  
- automatic configuration for devices (paramiko and test device???), 
  - include underlay and overlay verification
- add IPSEC, routing to tunnels ??? 

### l3vpn_buider
- build config using jinja2
- deploy configuration to devices
- validate configuration once deployed

### virutal-box-lab
- configure lab devices to specific baselines
  - track available baselines
  - script to load l3vpn gold config 
  - script to load gold config on lab devices (backup then load gold)
  - build new virutal box devices from baseline
- script to start virutal machines


### Other Thoughts
- pull down git repo and run specific scripts from repo against devices 
- program to add JUNOS firewall policies 
- script against device APIs 
  - use ncclient to build netconf configurations for cisco
  - use eAPI client for Arista (https://eos.arista.com/working-with-the-python-eapi-client/)

## Refs

### Links
[netmiko Supported Platforms] https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md#available-device-types
[netmiko try examples] https://pynet.twb-tech.com/blog/automation/netmiko-what-is-done.html
[textfsm and netmiko] https://www.packetflow.co.uk/a-hands-on-guide-to-netmiko-and-textfsm/
[netmiko getting started] https://ktbyers.github.io/netmiko/#tutorialsexamplesgetting-started
[regex tester] https://pythex.org/
[import vars from a file] https://stackoverflow.com/questions/17255737/importing-variables-from-another-file
[dict comprehnsion] https://www.programiz.com/python-programming/dictionary-comprehension
[netmiko examples from kirk byers] https://pynet.twb-tech.com/blog/automation/netmiko.html
[An introduction to the ipaddress module] https://docs.python.org/3.7/howto/ipaddress.html  
[ipaddress manipultation library] https://docs.python.org/3.7/library/ipaddress.html#ipaddress.ip_address
[using the ipaddress module in python] https://www.thepythoncode.com/article/  
[examplds of ipaddress module in python] https://www.programcreek.com/python/example/86160/ipaddress.IPv4Network
[json encoder and decoder] https://docs.python.org/3.7/library/json.html
[reading and writing output to a json file] https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
[datetime examples] https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python
[saving files to a sub directory] https://stackoverflow.com/questions/42255753/saving-files-to-a-subdirectory

### Notes
#### ipaddress python module
- TypeError: Object of type IPv4Network is not JSON serializable -> ipaddress objects created using the ipaddress library cannot be written using json, instead save the ip address or network as a string and typecast it later

#### csr1000v 
- netconf: ssh -s lab-admin@192.168.255.131 netconf 

## lab Inforation 
This folder contains the scripts and configurations i use for my personal lab which runs on virtual box lab. 

## Device Info
All the software i use in this virutal lab is freely available and can be found using the following links:
- Arista EOS: https://www.arista.com/en/support/software-download
- CSR1000v: https://software.cisco.com/download/home/284364978/type/282046477/release/3.15.0S 
  - 3.15.0S is latest freely downloadable version available as of 11/23/19
- Cumulus Linux: https://cumulusnetworks.com/products/cumulus-vx/download/thanks/vmware-3710-/

### Notes
- Arista EOS: 
  - Network Adapters on EOS devices must be set to hardware type PCnet-FAST III or they will not pass data. the management inteface can function as an intel NIC but eth interfaces must be PCnet-FAST III.
    - ref: https://techandtrains.com/2014/11/14/installing-arista-veos-in-virtualbox-and-gns3/
    - vEOS does not appear to support L3VPNs (EOS does), ipv4-vpn address family show commands return (% Not supported)
