def read_text_file_as_string(input_file_name, input_file_path = './',):
#read a text file from disk and return a string
    input_file_and_path = input_file_path + input_file_name 
     #create a full name for the file and path, note path must end in / for linux systems
    with open(input_file_and_path, 'r') as file:
        opened_file = file.read()
    file.close()
    return opened_file


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