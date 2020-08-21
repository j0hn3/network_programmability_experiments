# virtual-box-lab
This folder contains the scripts and configurations i use for my personal lab which runs on virtual box lab. 

## Device Info
All the software i use in this virutal lab is freely available and can be found using the following links:
- Arista EOS: https://www.arista.com/en/support/software-download
- CSR1000v: https://software.cisco.com/download/home/284364978/type/282046477/release/3.15.0S 
  - 3.15.0S is latest freely downloadable version available as of 11/23/19
- Cumulus Linux: https://cumulusnetworks.com/products/cumulus-vx/download/thanks/vmware-3710-/

### Notes
- Arista EOS: 
  - Network Adapters on EOS devices must be set to hardware type PCnet-FAST III or they will not pass data
    - the management inteface can function as an intel NIC but eth interfaces must be PCnet-FAST III
    - vEOS does not appear to support L3VPNs (% Not supported)