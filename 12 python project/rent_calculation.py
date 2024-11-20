# this the program regarding to the rent
# rent is distrubuted among the friends please
'''please take a look of this question
enter your hostel/flat rent
enter the amount of food ordered
enter the total of electricity spend
enter the charge per unit
enter the number of persons living in room/flat
each person will pay'''

flat_rent=int(input("Enter your flat rent/hostel "))
food_ordered=int(input("Enter total amount of food orderd "))
electricity=int(input("Enter your electricity spend "))
electricity_charges=int(input("Enter the charges per unit "))
persons=int(input("Enter number of persons living in room "))

print(f'Each person will pay ',((flat_rent + food_ordered) + (electricity*electricity_charges))/persons)

import this
