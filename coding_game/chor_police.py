import random
x = 0 # choor
x= 1# not choor
choose = int(random.choice(['1','2','3','4']))
n=4
player1="raja 1"
player2="mantri 2"
player3="choor 3"
player4="shipahi 4"

play=input("Enter the game:")#play

if play=="play":
    if choose==1:
        print("raja")    
    elif choose==2:
        print("mantri")    
    elif choose==3:
        print("choor")    
    elif choose==4:
        print("shiphai")    
