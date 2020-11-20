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