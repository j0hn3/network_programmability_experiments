    #validate the output directory exists, if it doesnt create it
    #ref: https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
    if not os.path.exists('my_folder'):
        os.makedirs('my_folder')