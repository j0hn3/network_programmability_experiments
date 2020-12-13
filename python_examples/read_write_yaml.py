import yaml

def read_yaml_file(input_file_name, input_file_path = './',):
#read a yaml file from disk and retun a dict
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems
    with open(input_file_and_path, 'r') as file:
        opened_file = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return opened_file

def write_yaml_file(output_file_data, output_file_name, output_file_path = './'): 
#take a dict and write it to disk as a yaml file
    create_folder(output_file_path)
    #create any folders in the output file path if needed 
    output_file_and_path = output_file_path + output_file_name
    #create a full name for the file and path, note path must end in / for linux systems
    with open(output_file_and_path, 'w') as file:
        file.write(yaml.dump(output_file_data))
    file.close()
    return None

####

import yaml
file_path = open(PATH, 'r')
file = yaml.load(file_path)
file_path.close()
print(yaml.dump(file))

