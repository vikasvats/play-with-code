# write the code to reverse the string
def string_reverse(enter1):
        # if x==0:
        # bag1 = ""
        # # enter = input("enter your string name you want to reverse:")
        # # for i in range(0,len(enter)):
        # bag1+=enter[::-1]
        # # print(f'Throw first method{bag}')
        # return bag1
        # # elif x==1:
        bag1=""
        # enter1 = input("Enter the string name you want to reverse:")
        for i in reversed(range(0,len(enter1))):
            bag1+=enter1[i]
        # print(f'throw 2nd method bag {bag}')
        return bag1

if __name__=="__main__":
      string_reverse()

