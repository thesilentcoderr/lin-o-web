import os

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
