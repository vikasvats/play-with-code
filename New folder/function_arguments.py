# # def average(a,b=6):
# #     print("The average is",(a+b)/2)

# # average(4)

# def name(fname,mname='kumar',lname='gupta'):
#     print(fname,mname,lname)

# a="Ayushi"
# b="Vikas"
# name(a,"","Chaudhary")

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c =average(5,6,7,1)

print(c)