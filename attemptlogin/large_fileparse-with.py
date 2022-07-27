#!/usr/bin/python3 

# use for counting
loginfail = 0 
loginsuccess=0 
# open for reading 
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as kfile:

    for line in kfile: 
        if " - - - -] Authorization failed" in line:
            loginfail += 1
            # Challenge 01, Try writing code to display number of successful logins.
        elif " - - - -] Loaded 2 encryption keys" in line:
            loginsuccess += 1
print("The number of failed login attempts is", loginfail)
print("The number of successful login attempts is", loginsuccess)
