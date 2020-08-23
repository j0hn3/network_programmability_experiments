import json
import yaml
import os

def create_folder(path):
#this function creates a folder (defined in the path var) if it does not already exist 
    try:
        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)
    except IOError as exception:
        raise IOError('%s: %s' % (path, exception.strerror))
    return None


def read_file(input_file_name, input_file_path = './',): 
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(input_file_and_path, 'r') as file:
        opened_file = file.read()
    file.close()
    return opened_file

def read_yaml_file(input_file_name, input_file_path = './',): 
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(input_file_and_path, 'r') as file:
        opened_file = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return opened_file

def write_yaml_file(output_file_data, output_file_name, output_file_path = './',): 
#write a data (output_file_data) to a path (output_file_path & output_file_name) in json format
    create_folder(output_file_path)
    #create any folders in the output file path if needed 
    output_file_and_path = output_file_path + output_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(output_file_and_path, 'w') as file:
        file.write(yaml.dump(output_file_data))
    file.close()

def read_json_file(input_file_path, input_file_name): 
#this function will open a .json file and return it as a dictionary
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(input_file_and_path, 'r') as file:
        opened_file = json.load(file)
    file.close()
    return opened_file