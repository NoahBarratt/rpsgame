# this is the "game.py" file...

import random
from typing_extensions import ParamSpecArgs

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("Rock, Paper, Scissors, Shoot!")

# PROMPT USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors'")

print(user_choice)

# COMPUTER CHOICE AT RANDOM

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

if computer_choice == "rock" and user_choice == "scissors":
    print("Oh, the computer won. It's ok.")
    print("Thanks for playing. Please play again!")

if computer_choice == "scissors" and user_choice == "paper":
    print("Oh, the computer won. It's ok.")
    print("Thanks for playing. Please play again!")

if computer_choice == "rock" and user_choice == "paper":
    print("Congragulations, you won!")
    print("Thanks for playing. Please play again!")

if computer_choice == "paper" and user_choice == "scissors":
    print("Congragulations, you won!")
    print("Thanks for playing. Please play again!")

if computer_choice == "scissors" and user_choice == "rock":
    print("Congragulations, you won!")
    print("Thanks for playing. Please play again!")

if computer_choice == "paper" and user_choice == "rock":
    print("Oh, the computer won. It's ok.")
    print("Thanks for playing. Please play again!")

if computer_choice == "paper" and user_choice == "paper":
    print("It's a tie!")
    print("Thanks for playing. Please play again!")

if computer_choice == "rock" and user_choice == "rock":
    print("It's a tie!")
    print("Thanks for playing. Please play again!")

if computer_choice == "scissors" and user_choice == "scissors":
    print("It's a tie!")
    print("Thanks for playing. Please play again!")
breakpoint()

