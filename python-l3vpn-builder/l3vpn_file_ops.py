def read_file(input_file_name, input_file_path = './',): 
    input_file_and_path = input_file_path + input_file_name
    #create a full name for the file and path, note path must end in / for linux systems 
    with open(input_file_and_path, 'r') as file:
        opened_file = file.read()
    file.close()
    return opened_file
