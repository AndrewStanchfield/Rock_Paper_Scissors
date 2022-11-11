# Import 'randint' from the random module.
from random import randint

# Create a list of options to choose and store it in the play variable.
play = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer.
computer = play[randint(0,2)]

# Setting the player to False allows the loop to run again.
player = False

while player == False:
# Set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("You can only play Rock, Paper, or Scissors. Don't forget the CAPITOL letter!")

    # Player was set to True, but we want it to be False so the loop continues
    player = False
    computer = play[randint(0,2)]