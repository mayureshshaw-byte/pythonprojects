#rock paper scissors game
import random

choice = ["rock", "paper", "scissor"]

computer = random.choice(choice)

user = input("Enter rock, paper or scissor: ")

print("You chose:", user)
print("Computer chose:", computer)

if user == "scissor" and computer == "rock":
    print("computer wins")
elif user == "rock" and computer == "paper":
    print ("computer wins")
elif user == "paper" and computer == "scissor":
    print("computer wins")
elif user == "rock" and computer == "scissor":
    print("You win!")

elif user == "paper" and computer == "rock":
    print("You win!")

elif user == "scissor" and computer == "paper":
    print("You win!")
elif user == computer:
    print("draw")    
else :
    print("invalid input")
