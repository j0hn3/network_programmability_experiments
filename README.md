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

