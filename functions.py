import os
from subprocess import getstatusoutput as spo
import subprocess as sp
def query(cmd,id,args):
    if "date" in cmd:
        output = date(id,args)
    elif "apache" in cmd or "server" in cmd or "httpd" in cmd and "install":
        output =httpd(id,args)
    
    return output


#User Administration
def create_user(id,args):
    now=sp.getoutput(f"docker exec {id} useradd {args}")
    return now


def currentuser(id,args):
    now=sp.getoutput(f"docker exec {id} whoami")
    return now


def createuser_nologin(id,args):
    now=sp.getoutput(f"docker exec {id} useradd -s /sbin/sh {args}")   
    return now 


def users(id,args):
    now=sp.getoutput(f"docker exec {id} cat /etc/shadow")
    return now

def user_info(id,args):
    try:
        now=sp.getoutput(f"docker exec {id} cat /etc/passwd")
        return now
    except:
        msg="*****Access Denied !!*****You must be the root user to perform this action*****"
        now=sp.getoutput("echo "+msg)
        return now
    
def login_as_user(id,args):
    try:
        now=sp.getoutput(f"docker exec {id} su {args}")
        return now
    except:
        msg="*****User does not exist or the user has no Shell*****"
        now=sp.getoutput("echo "+msg)
        return now
    
    
    

# File System
def show_file(id,args):
    try:
        output = spo(f"docker exec {id} cat {args}")
        if output and (output[0] == 0):
            content = output[1]
        else:
            content = f"No such file in the directory :- {args}"
    except:
        content = "An error occured, Please try again !!"
    return content
    

def create_file(id,args):
    try:
        output = spo(f"docker exec {id} touch {args}")
        if output and (output[0] == 0):
            msg = "File Created successfully"
    except:
        msg = "An error occured, Please try again !!"
    return msg

def create_dir(id,args):
    try:
        output = spo(f"docker exec {id} mkdir {args}")
        if output and (output[0] == 0):
            msg = "Folder/Directory Created successfully"
    except:
        msg = "An error occured, Please try again !!"
    return msg

def list_dir(id,args):
    try:
        output = spo(f"docker exec {id} ls -l")
        if output and (output[0] == 0):
            msg = output[1]
    except:
        msg = "An error occured, Please try again !!"
    return msg

#Installation and Uninstallation of packages
def httpd(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum install httpd -y")
    if "Complete" in o:
        print("Successfully Installed")
    else:
        print("Not able to install")
        
def python3(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum install python3 -y")
    if "Complete" in o:
        print("Successfully Installed")
    else:
        print("Not able to install")        
   
def python2(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum install python2 -y")
    if "Complete" in o:
        print("Successfully Installed")
    else:
        print("Not able to install")    
       
def c_compiler(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum install gcc -y")
    if "Complete" in o:
        print("Successfully Installed")
    else:
        print("Not able to install")
        
def java(is,args):
    o=sp.getoutput(f"docker exec {id} sudo yum install java -y")
    if "Complete" in o:
        print("Successfully Installed")
    else:
        print("Not able to install")
#Uninstallation
def uninstall_httpd(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum remove httpd -y")
    if "Complete" in o:
        print("Successfully Uninstalled")
    else:
        print("Not able to uninstall")
        
def uninstall_python3(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum remove python3 -y")
    if "Complete" in o:
        print("Successfully Uninstalled")
    else:
        print("Not able to uninstall")        
   
def uninstall_python2(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum remove python2 -y")
    if "Complete" in o:
        print("Successfully Uninstalled")
    else:
        print("Not able to uninstall")    
       
def uninstall_c_compiler(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum remove gcc -y")
    if "Complete" in o:
        print("Successfully Uninstalled")
    else:
        print("Not able to uninstall")
        
def uninstall_java(id,args):
    o=sp.getoutput(f"docker exec {id} sudo yum remove -y")
    if "Complete" in o:
        print("Successfully Uninstalled")
    else:
        print("Not able to uninstall")
      
        
        
        
 #Baisc Linux commands
def date(id,args):
    now = spo(f"docker exec {id} date")
    return now


def ifconfig():
    output=sp.getoutput("ifconfig")
    return output

                
def history(id,config):
    output=sp.getoutput(f"docker exec {id} history")
    return output
        

def pwd(id,config):
    output=sp.getoutput(f"docker exec {id} pwd")
    return output
    
    
def cal(id,config):
     output=sp.getoutput(f"docker exec {id} cal")
     return output
    
 #prompts for y/n
def rm_file(id,args):
    try:
        output=sp.getoutput(f"docker exec {id} rm {args}")
    except:
        output="rm: cannot remove '{args}': No such file or directory"      
    return output   
        
        
def head(id,args):
    try:
        output=sp.getoutput(f"docker exec {id} head {args}")
    except:
        output="head: cannot open '{args}' for reading: No such file or directory"
    return output   
      
    
def tail(id,args):
    try:
        output=sp.getoutput(f"docker exec {id} tail {args}")
    except:
        output="tail: cannot open '{args}' for reading: No such file or directory"
    return output   


def id(id,args):
    output=sp.getoutput(f"docker exec {id} id")
    return output


def wc(id.args):
    try:
        output=sp.getoutput(f"docker exec {id} wc {args}")
    except:
        output="wc: {args}: No such file or directory"
    return output   


def sort(id,args):
    try:
        output=sp.getoutput(f"docker exec {id} sort {args}")
    except:
        output="sort: cannot read: {args}: No such file or directory"
    return output   


def sleep(id,args):
    output=sp.getoutput(f"docker exec {id} sleep {args}")
    return output
