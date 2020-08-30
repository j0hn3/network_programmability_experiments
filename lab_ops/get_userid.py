import os

def get_userid():
#get the id of the user logged into the system who ran this script
    user_id = pwd.getpwuid(os.getuid()).pw_name
    return user_id
