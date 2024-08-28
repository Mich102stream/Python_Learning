# Rock paper scissors game

import random # import random module

choices = ["rock", "paper", "scissors"] # list of choices

computer = random.choice(choices) # random.choice() method is used to select a random item from a list.

player = input("rock, paper or scissors? ").lower()  # .lower() method is used to convert the input to lowercase.

print("Computer chose " + computer) # print the computer's choice

if player == computer:  # check if it's a draw
    print("It's a draw")
elif player == "rock" and computer == "scissors":   # check if player wins
    print("Player wins")
elif player == "paper" and computer == "rock":  # check if player wins
    print("Player wins")
elif player == "scissors" and computer == "paper":  # check if player wins
    print("Player wins")
else:
    print("Computer wins")  # if none of the above conditions are met then computer wins.
