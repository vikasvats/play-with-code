# # https://www.geeksforgeeks.org/python-program-to-add-two-numbers/
# # add two numbers in python

# num1 =int(input("Enter your number"))
# num2 =int(input("Enter your number"))

# print(num1+num2)

# # function method

# def add(num3,num4):
#     return num3+num4

# num6= 5
# num7= 7

# print(add(num6 , num7))

# add two numbers using operator.add() method

num1 = 15
num2 = 17

# # adding two nos

# import operator
# su = operator.add(num1,num2)
# print(su)
# print(f"Sum of {num1} and {num2} is {su}")

# add two number using lambda function

add_numbers = lambda x, y: x + y

# take input from the user

result = add_numbers(num1,num2)

# 
print(f"The sum of {num1} and {num2} is {result} ")