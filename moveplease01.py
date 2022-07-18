#!/usr/bin/env python3

import shutil
import os

# tell python to start in home user directory
os.chdir('/home/student/mycode/')

# move the file or folder at the path
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user for a new name for the file
xname = input('What is the new name for kerrigan.obj? ')

# rename the current kerr... file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



