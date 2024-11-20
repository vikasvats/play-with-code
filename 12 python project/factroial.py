# write down the factorial of the data
# like 4*3*2*1

def factorial(n):
    if n==1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print( factorial(5))

vikas={}
chaudhary=set()
print(type(vikas))
print(type(chaudhary))