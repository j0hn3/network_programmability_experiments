import json

def read_json_file(input_file_name, input_file_path = './'):
#read a json file from disk and return a dict
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems
    with open(input_file_and_path, 'r') as file:
        opened_file = json.load(file)
    file.close()
    return opened_file


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