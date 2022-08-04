#!/usr/bin/env python3

import zipfile

# Challenge 01 Write a scirpt that can be used to run against a file and return if file iis a zip file or not (True or False) 

def main(): 

    # ask for user input 
    iszip = input("What is the file you would like to examine")

    if zipfile.is_zipfile(iszip):  # returns true if file is a zip file
        print("True, this is a zip file")

    else: 
        print("False, this is not a zip file")
if __name__ == "__main__":

    main()

