# rock paper sessior
# r>s,s>p,p>r
import random

def play():
    user=input("What's your choice r for rock, s sessior, p paper:")
    computer = random.choice(["rock","paper","sessior"])

    print(f'computer choose:{computer}')

    if user==computer:
        print("It's a tie")
    else:
        is_winner(user,computer)

def is_winner(user,computer):
    if (user=="rock" and computer=="sessior") or (user=="sessior" and computer=="paper") or (user=="paper" and computer=="rock"):
        print("Your are winner")
    else:
        print("You are losser")

play()