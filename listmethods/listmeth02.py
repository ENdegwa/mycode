#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# Challenge 01 Make your own list to display with list methods
protoa2 = [ 232, 234, 56534, 345] # list of numbers to display
print(protoa2) # display protoa2 list of numbers
proto3 = [ 22, 1, 3, 545345] # list of numbers to display 
print(proto3) # display proto3 list of numbers
protoa2.append("diro") # add diro to end of list
print(protoa2) # display protoa2 list of numbers after adding "diro"
proto3.extend(protoa2) # pass protoa2 to extend the method
print(proto3) # display proto3 as list of numbers

