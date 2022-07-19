#!/usr/bin/env python3

## Make a program that prompts the user for a numberic score, then returns the letter grade associated with that score.


    
message = 'Your letter grade based on your score is '
    
grade =int(input("What is your grade percentage? "))

    # if 90 or above return back letter grade A
if grade > 89:
    message = message + "A"
    # if 80 to 89 return back letter grade B
elif grade > 79:
    message = message + "B"
    # if 70 to 79 return back letter grade C
elif grade > 69: 
    message = message + "C"
    # if 60 to 69 return back letter grade D
elif grade > 59: 
    message = message + "D"
else:
    message = message + "F"

    # display the letter grade
print(message)

        

