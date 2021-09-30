import os
from subprocess import getstatusoutput as spo

def query(cmd):
    if "date" in cmd:
        op = date()
    return op

def date():
    now = os.system()
    return now


#User Administration
def create_user(username):
    now=os.system("useradd "+username)
    return now
def currentuser():
    now=os.system("whoami")
    return now
def createuser_nologin(username):
    now=os.system("useradd -s /sbin/sh "+username)   
    return now 
def users():
    now=os.system("cat /etc/shadow")
    return now
def user_info():
    try:
        now=os.system("cat /etc/passwd")
        return now
    except:
        print("*****Access Denied !!*****")
        print("*****You must be the root user to perform this action*****")
def login_as_user(username):
    try:
        now=os.system("su "+username)
        return now
    except:
        print("*****User does not exist or the user has no Shell*****")


# File System
def show_file(path,file_name):
    try:
        full_path = os.path.join(path,file_name)
        output = spo(f'cat {full_path}')
        if output and (output[0] == 0):
            content = output[1]
        else:
            this_dir = spo('dir')[1]
            content = f"No such file in the directory :- {this_dir}"
    except:
        content = "An error occured, Please try again !!"
    return content
    

def create_file(path,file_name):
    try:
        full_path = os.path.join(path,file_name)
        output = spo(f"touch {full_path}")
        if output and (output[0] == 0):
            msg = "File Created successfully"
        else :
            msg = f"Oops!!, {path} is NOT valid ."
    except:
        msg = "An error occured, Please try again !!"
    return msg

def create_dir(path,dir_name):
    try:
        full_path = os.path.join(path,dir_name)
        output = spo(f"mkdir {full_path}")
        if output and (output[0] == 0):
            msg = "Folder/Directory Created successfully"
        else :
            msg = f"Oops!!, {path} is NOT valid ."
    except:
        msg = "An error occured, Please try again !!"
    return msg

def list_dir(path):
    try:
        output = spo(f"ls -l {path}")
        if output and (output[0] == 0):
            msg = output[1]
        else :
            msg = f"Oops!!, {path} is NOT valid ."
    except:
        msg = "An error occured, Please try again !!"
    return msg