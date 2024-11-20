
# # # # numbers=[1,-2,3,-4,-6,-7,-8,9,10,-2]
# # # # count=0
# # # # for num in numbers:
# # # #     if(num>0):
# # # #         count+=1

# # # # print(count)

# # # # sum of even numbers
# # # n = 10
# # # sum_even=0

# # # for i in range(1,n+1):
# # #     if i%2==0:
# # #         print(i)
# # #         sum_even+=i

# # # print(sum_even)

# # # print the multiplaction table for a given numbers up to 10,but skip the fifth itereation

# # n=10
# # number=3
# # for i in range(1,n+1):
# #     if i==5:
# #         continue
# #     print(number,"x",i,"=",number*i)

# # reverse a string:
# input_str="Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str=char+reversed_str

# print(reversed_str)

# find the first non repeted charactor
# input_str="teeter"

# for char in input_str:
#    print(char)
#    if input_str.count(char)==1:
#         print("char is:",char)
#         break

number = 5
factorial =1

while number>0:
    factorial= factorial * number

    number= number - 1

print(factorial)
print(5*4*3*2*1)