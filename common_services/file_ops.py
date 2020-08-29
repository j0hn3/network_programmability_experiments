import datetime
import json
import yaml
import os

###
#create_folder
#gen_timestamp
#get_userid
####
#read_text_file_as_string
#read_yaml_file
#read_json_file
####
#write_text_file_from_string
#write_yaml_file
#write_json_file
####

###Various Operations

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

def gen_timestamp():
#generate a timestamp in the format year-month-day-hour-minute-second
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d-%H-%M-%S')
    return now

def get_userid():
#get the id of the user logged into the system who ran this script
    user_id = pwd.getpwuid(os.getuid()).pw_name
    return user_id

###Read Files

def read_text_file_as_string(input_file_name, input_file_path = './',):
#read a text file from disk and return a string
    input_file_and_path = input_file_path + input_file_name 
     #create a full name for the file and path, note path must end in / for linux systems
    with open(input_file_and_path, 'r') as file:
        opened_file = file.read()
    file.close()
    return opened_file

def read_yaml_file(input_file_name, input_file_path = './',):
#read a yaml file from disk and retun a dict
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems
    with open(input_file_and_path, 'r') as file:
        opened_file = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return opened_file

def read_json_file(input_file_name, input_file_path = './'):
#read a json file from disk and return a dict
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems
    with open(input_file_and_path, 'r') as file:
        opened_file = json.load(file)
    file.close()
    return opened_file

###Write Files

def write_text_file_from_string(output_file_data, output_file_name, output_file_path = './'):
#take a string and write it to disk as a text file
    create_folder(output_file_path)
    #create any folders in the output file path if needed 
    output_file_and_path = output_file_path + output_file_name
    #create a full name for the file and path, note path must end in / for linux systems
    with open(output_file_and_path, 'w') as file:
        file.write(output_file_data)
    file.close()
    return None

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

def write_json_file(output_file_data, output_file_name, output_file_path = './'):
#take a dict and write it to disk as a json file
    create_folder(output_file_path)
    #create any folders in the output file path if needed 
    output_file_and_path = output_file_path + output_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(output_file_and_path, 'w') as file:
        file.write(json.dumps(output_file_data, indent=4))
    file.close()
    return None