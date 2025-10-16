# Rock-Paper-scissors game with the computer

import random #<--import module 

bestOut = int(input("Best out of: ")) 

userScore = 0      #<-- variables to keep track of scores
compScore = 0

for i in range(bestOut):   #<--loop in range the user input
    userMove = str(input("Pick ur move: ")).lower()   #<--user picks move
    moves = ["rock", "paper", "scissors"]
    compMove = str(random.choice(moves)) #<--variable holds a random chose move the list

    #check who won and add score accordingly
    if (userMove == "rock" and compMove == "paper") or \
    (userMove == "paper" and compMove == "scissors") or \
    (userMove == "scissors" and compMove == "rock"):
        compScore += 1    
        print(f"My move was {compMove}, you lose")

    elif (compMove == "rock" and userMove == "paper") or \
    (compMove == "paper" and userMove == "scissors") or \
    (compMove == "scissors" and userMove == "rock"):
        userScore += 1
        print(f"My move was {compMove}, you won")

    elif userMove == compMove:
        userScore += 1
        compScore += 1
        print(f'Its a tie. My move was {compMove}')

    else:
        print("Invalid move")

print(f"Your score: {userScore}, computer's score: {compScore}")

 

