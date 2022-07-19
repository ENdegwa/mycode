#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

# Challenge 01 - Allow user to input lowercase or uppercase answer and produce correct answer# Challenge 02 - If user provides shrubbery as input print super secret answer

round = 0
answer = " "

while round < 3 and answer != "Brian" and answer != "Shruberry":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize() # will allow users input to be Brian with lowercase input
    if answer == "Brian": # logic to check if user is correct
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    elif answer == "Shruberry": # super secret answer
        print("You gave the super secret answer!")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

