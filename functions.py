import os
from subprocess import getstatusoutput as spo
import subprocess as sp
def query(cmd,id,args):
    if "date" in cmd:
        print("Check date")
        output = date(id,args)
    elif "installapache" in cmd:
        output =httpd(id,args)
    elif "installpy3" in cmd:
        output = python3(id,args)
    elif "installpy2" in cmd:
        output = python2(id,args)
    elif "installgcc" in cmd:
        output = c_compiler(id,args)
    elif "installjava" in cmd:
        output = java(id,args)
    elif "uninstallapache" in cmd:
        output = uninstall_httpd(id,args)
    elif "uninstallpy3" in cmd:
        output = uninstall_python3(id,args)
    elif "uninstallpy2" in cmd:
        output = uninstall_python3(id,args)
    elif "uninstallgcc" in cmd:
        output = uninstall_c_compiler(id,args)
    elif "uninstalljava" in cmd:
        output = uninstall_java(id,args)
    elif "ifconfig" in cmd:
        output = ifconfig()
    elif "history" in cmd:
        output = history(id,args)
    elif "pwd" in cmd:
        output = pwd(id,args)
    elif "cal" in cmd:
        output = cal(id,args)
    elif "head" in cmd:
        output = head(id,args)
    elif "tail" in cmd:
        output = tail(id,args)
    elif "wc" in cmd:
        output = wc(id,args)
    elif "sort" in cmd:
        output = sort(id,args)
    elif "sleep" in cmd:
        output = sleep(id,args)
    elif "ls" in cmd:
        output = list_dir(id,args)
    elif "touch" in cmd:
        output=create_file(id,args)
    elif "hiddenfile" in cmd:
        output = list_dir_h(id,args)
    elif "mkdir" in cmd:
        output = create_dir(id,args)
    elif "rmdir" in cmd:
        output = delete_dir(id,args)
    elif "adduser" in cmd:
        output = create_user(id,args)
    elif "id" in cmd:
        output = currentuser(id,args)
    elif "addusernologin" in cmd:
        output = createuser_nologin(id,args)
    elif "shadow" in cmd:
        output = users(id,args)
    elif "passwd" in cmd:
        output = user_info(id,args)
    elif "loginuser" in cmd:
        output = login_as_user(id,args)
    else:
        output = "No command found"
    print("Returning output")
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

def delete_dir(id,args):
    try:
        output = spo(f"docker exec {id} rmdir {args}")
        if output and (output[0] == 0):
            msg = "Folder/Directory Deleted successfully"
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

def list_dir_h(id,args):
    try:
        output = spo(f"docker exec {id} ls -a")
        if output and (output[0] == 0):
            msg = output[1]
    except:
        msg = "An error occured, Please try again !!"
    return msg

#Installation and Uninstallation of packages
def httpd(id,args):
    o=sp.getoutput(f"docker exec {id} yum install httpd -y")
    if "Complete" in o:
        return "Successfully Installed"
    else:
        return "Not able to install"
        
def python3(id,args):
    o=sp.getoutput(f"docker exec {id} yum install python3 -y")
    if "Complete" in o:
        return "Successfully Installed"
    else:
        return "Not able to install"        
   
def python2(id,args):
    o=sp.getoutput(f"docker exec {id} yum install python2 -y")
    if "Complete" in o:
        return "Successfully Installed"
    else:
        return "Not able to install"    
       
def c_compiler(id,args):
    o=sp.getoutput(f"docker exec {id} yum install gcc -y")
    if "Complete" in o:
        return "Successfully Installed"
    else:
        return "Not able to install"
        
def java(id,args):
    o=sp.getoutput(f"docker exec {id} yum install java -y")
    if "Complete" in o:
        return "Successfully Installed"
    else:
        return "Not able to install"
#Uninstallation
def uninstall_httpd(id,args):
    o=sp.getoutput(f"docker exec {id} yum remove httpd -y")
    if "Complete" in o:
        return "Successfully Uninstalled"
    else:
        return "Not able to uninstall"
        
def uninstall_python3(id,args):
    o=sp.getoutput(f"docker exec {id} yum remove python3 -y")
    if "Complete" in o:
        return "Successfully Uninstalled"
    else:
        return "Not able to uninstall"        
   
def uninstall_python2(id,args):
    o=sp.getoutput(f"docker exec {id} yum remove python2 -y")
    if "Complete" in o:
        return "Successfully Uninstalled"
    else:
        return "Not able to uninstall"    
       
def uninstall_c_compiler(id,args):
    o=sp.getoutput(f"docker exec {id} yum remove gcc -y")
    if "Complete" in o:
        return "Successfully Uninstalled"
    else:
        return "Not able to uninstall"
        
def uninstall_java(id,args):
    o=sp.getoutput(f"docker exec {id} yum remove -y")
    if "Complete" in o:
        return "Successfully Uninstalled"
    else:
        return "Not able to uninstall"
      
        
        
        
 #Baisc Linux commands
def date(id,args):
    print("In date")
    now = sp.getoutput("date")
    print("Date",now)
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


def wc(id,args):
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

def user_defined(id,cmd):
    print("Function user def",cmd)
    output=sp.getoutput(f"docker exec {id} {cmd}")
    print("Fun ouptut",output)
    return output 
