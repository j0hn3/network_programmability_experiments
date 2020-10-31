# Network Programmability Experiments
This repo contains a variety of my personal experiments with network programability for py personal lab. 
In October 2020 I upgraded my personal laband as part of the rebuilding pricess archived all previous work. 

## device-config-files
This folder cotnains the configuration commands I deployed manually to build my lab, updates to the /etc/hosts file on my jump host, and my to-do list for the lab

## ansible
This folder contains all the ansible playbooks created for maintaince of my lab enviorment. Functionality presently includes:  backing up device configurations, restoring devices to a baseline (aka gold configuration) and, updating the baseline (aka gold) configuration

## lab-configs
This folder structure is created by ansible and contains data for each lab device