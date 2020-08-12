import json
import os

def create_folder(path):
#ref: https://stackoverflow.com/questions/42255753/saving-files-to-a-subdirectory
#this function creates a folder (defined in the path var) if it does not already exist 
    try:
        if os.path.isdir(path):
            pass
        else:
            os.makedirs(path)
    except IOError as exception:
        raise IOError('%s: %s' % (path, exception.strerror))
    return None

def write_files_as_json (output_file_data, output_file_path, output_file_name):
#write a data (output_file_data) to a path (output_file_path & output_file_name) in json format
    output_file_and_path = output_file_path + output_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(output_file_and_path, 'w') as file:
        file.write(json.dumps(output_file_data, indent=4))
    file.close()

def read_json_files(input_file_path, input_file_name): 
#this function will open a .json file and return it as a dictionary
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(input_file_and_path, 'r') as file:
        opened_file = json.load(file)
    file.close()
    return opened_file

def write_string(output_file_path, output_file_name, output_file_data):
    output_file_and_path = output_file_path + output_file_name
    with open(output_file_and_path, 'w') as file:
        file.write(output_file_data)
    file.close()