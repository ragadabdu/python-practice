import random 

myMove = ""

def pickMove():
    moves = ["rock", "paper", "scissors"]
    myMove = str(random.choice(moves))
    return myMove

urMove = str(input("Pick ur move: "))

myMove = pickMove()

if urMove == "rock" and myMove == "paper":
    print(f"My move was {myMove} you lost")

elif urMove == "paper" and myMove == "scissors":
    print(f"My move was {myMove} you lost")

elif urMove == "scissors" and myMove == "rock":
    print(f"My move was {myMove} you lost")
elif myMove == "rock" and urMove == "paper":
    print(f"My move was {myMove} you won")

elif myMove == "paper" and urMove == "scissors":
    print(f"My move was {myMove} you won")

elif myMove == "scissors" and urMove == "rock":
    print(f"My move was {myMove} you won")

else:
    print("Invalid move")
 

