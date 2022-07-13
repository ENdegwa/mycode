#!/usr/bin/env python3

# create a list containing three items 
my_list = [ "192.168.0.5", 5060, "UP" ]

#display the first item 
print(" The first item in the list (IP): " + my_list[0])

#Insert str() because 5060 is an integer and not a string, We can force an interger to be a string with () function
print("The second item in the list (port): " + str(my_list[1]) )
#display the third item 
print("The last item in the list (state): " + my_list[2] )

# Challenge 01 display only the IP addresses on the screen given the list provided

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("The first IP address is: " + iplist[3])

print("The second IP address is: " +iplist[4])

# Extra Solutions 

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

