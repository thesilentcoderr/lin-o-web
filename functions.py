import os

def query(cmd):
    if "date" in cmd:
        op = date()
    return op

def date():
    now = os.date()
    return now
