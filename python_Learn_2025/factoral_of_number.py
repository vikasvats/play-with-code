# https://www.geeksforgeeks.org/python-program-for-factorial-of-a-number/?ref=lbp

num = 6
sum = 1
for i in range(1, num+1):
    sum+=i*sum
    # print(f"factorial of {num} is {sum}")
print(f"factorial of {num} is {sum}")