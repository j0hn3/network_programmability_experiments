import json

def open_address_scheme(file_name = 'ip_address_scheme.json'):
#open a a file containing the ip address scheme in JSON format and return a dictionary
    with open(file_name, 'r') as file:
        json_object = json.load(file)
    return json_object

def write_changes_to_address_scheme(address_scheme_dict, file_name = 'ip_address_scheme.json'):
#take a dictionary containing the updated address scheme, file name and write it to a file in JSON format
    with open(file_name, 'w') as file:
        file.write(address_scheme_dict)
