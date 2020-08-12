output_file_data ="""

    ###Datacenter east
    
    #east.rtr.01

    interface 1006
    ip address 10.100.0.32/27
    description R1234
    no shutdown

    router ospf 100
    network 10.100.0.32/27

    ip prefix-list DATACENTER_EAST_ACTIVE_SUBNETS add 10.100.0.32/27
    
    #east.rtr.02

    interface 1006
    ip address 10.100.0.32/27
    description R1234
    no shutdown

    router ospf 100
    network 10.100.0.32/27

    ip prefix-list DATACENTER_EAST_ACTIVE_SUBNETS add 10.100.0.32/27
    """

output_file_path = './test_scripts/test_output/'
output_file_name = 'test_ip_allocation.txt'
import file_ops
file_ops.create_folder(output_file_path)
file_ops.write_string(output_file_path, output_file_name, output_file_data)