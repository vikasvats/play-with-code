import random

def guess(x):
    random_number = random.randint(1,x)
    guess= 0
    while guess != random_number:
        guess= int(input(f'guess a number between 1 and {x}:'))
        if guess < random_number:
            print("Sorry,guess again. too low.")
        elif guess>random_number:
            print('sorry,guess again. too high.')
    print(f'yay, congrats, You have guessed the number {random_number} correctly')

def computer_guess(x):
    low =1
    high=x
    feedback =""
    while feedback != "c":
        guess=random.randint(low,high)
        feedback = input(f'is {guess}too high (H),too low (L),or correct (c)??') 
        if feedback == "h":
            high=guess-1
        elif feedback=="l":
            low=guess +1
    print(f'yay! The computer guesses your number,{guess},correctly!')

computer_guess(10)





# guess(12)



    