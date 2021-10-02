import os
from subprocess import getstatusoutput as spo
import subprocess as sp
def query(cmd):
    if "date" in cmd:
        op = date()
    return op

def date():
    now = os.system()
    return now


#User Administration
def create_user(username):
    now=sp.getoutput("useradd "+username)
    return now
def currentuser():
    now=sp.getoutput("whoami")
    return now
def createuser_nologin(username):
    now=sp.getoutput("useradd -s /sbin/sh "+username)   
    return now 
def users():
    now=sp.getoutput("cat /etc/shadow")
    return now
def user_info():
    try:
        now=sp.getoutput("cat /etc/passwd")
        return now
    except:
        msg="*****Access Denied !!*****You must be the root user to perform this action*****"
        now=sp.getoutput("echo "+msg)
        return now

def login_as_user(username):
    try:
        now=sp.getoutput("su "+username)
        return now
    except:
        msg="*****User does not exist or the user has no Shell*****"
        now=sp.getoutput("echo "+msg)
        return now
    
    
    

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

#Installation of packages
def httpd:
    o=sp.getoutput("sudo yum install httpd")
    if "Complete" in o:
        print("Successfully Installed")
        
def python3:
    o=sp.getoutput("sudo yum install python3")
    if "Complete" in o:
        print("Successfully Installed")
   
def python2:
    o=sp.getoutput("sudo yum install python2")
    if "Complete" in o:
        print("Successfully Installed")
       
def c_compiler:
    o=sp.getoutput("sudo yum install gcc")
    if "Complete" in o:
        print("Successfully Installed") 
        
 def java:
    o=sp.getoutput("sudo yum install java")
    if "Complete" in o:
        print("Successfully Installed")
        
      
        
        
        
 #Baisc Linux commands
def ifconfig():
    output=sp.getoutput("ifconfig")
    return output

                
 def history():
    output=sp.getoutput("history")
    return output
        

def pwd():
    output=sp.getoutput("pwd")
    return output
    
    
def cal():
     output=sp.getoutput("cal")
     return output
    
 #prompts for y/n
def rm_file(file_name):
    try:
        output=sp.getoutput(f'rm {file_name}')
    except:
        output="rm: cannot remove '{file_name}': No such file or directory"      
    return output   
        
        
def head(file_name):
    try:
        output=sp.getoutput(f'head {file_name}')
    except:
        output="head: cannot open '{file_name}' for reading: No such file or directory"
    return output   
      
    
def tail(file_name):
    try:
        output=sp.getoutput(f'tail {file_name}')
    except:
        output="tail: cannot open '{file_name}' for reading: No such file or directory"
    return output   


def man(cmd):
     try:
        output=sp.getoutput(f'man {cmd}')
     except:
        output="No manual entry for {cmd}"
     return output   
    

def id():
    output=sp.getoutput("id")
    return output


def wc(file_name):
    try:
        output=sp.getoutput(f'wc {file_name}')
    except:
        output="wc: {file_name}: No such file or directory"
    return output   


def sort(file_name):
    try:
        output=sp.getoutput(f'sort {file_name}')
    except:
        output="sort: cannot read: {file_name}: No such file or directory"
    return output   


def sleep(time):
    output=sp.getoutput(f'sleep {time}')
    return output
                        
    
    



    
        
        
    
    
    
 



    

