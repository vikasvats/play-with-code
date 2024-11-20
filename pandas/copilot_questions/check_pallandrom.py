# write the code to check the list for the pallandrom
import reverse_string as rs
import forward_loop as fw

def check_palindrome():
    
    check = input("Enter the word you want to check palindrome:")
    revers = rs.string_reverse(check)
    forwar = fw.forward(check)
    print(revers)
    print(forwar)
    if revers == frowa:
        print(f'This string is a palindrome {check}')
    else:
        print("This string is not a palindrome")

check_palindrome()
# def forward(num):
#     if __name__=="__main__":
#         bag=""
#         for i in range(0,len(num)):
#             bag+=num[i]
#         return bag

# # forward("vikas")



# def string_reverse(enter1):
#     if __name__=="__main__":
#         # if x==0:
#         # bag1 = ""
#         # # enter = input("enter your string name you want to reverse:")
#         # # for i in range(0,len(enter)):
#         # bag1+=enter[::-1]
#         # # print(f'Throw first method{bag}')
#         # return bag1
#         # # elif x==1:
#         bag1=""
#         # enter1 = input("Enter the string name you want to reverse:")
#         for i in reversed(range(0,len(enter1))):
#             bag1+=enter1[i]
#         # print(f'throw 2nd method bag {bag}')
#         return bag1
