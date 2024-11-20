import random
# R>S
# S>P
# P>R
# rock paper scissor game
# lets play ;)

play=input("Rock,paper,scissor as R,P,S:").lower()
computer=random.choice(['r','p','s'])

print(computer)



if (play=='r' and computer=="s") or (play=="s"and computer=="p") or (play=='p' and computer=="r"):
    print("Your won")
elif (play==computer):
    print("match tie")


else:
    print("try again")

    
