# # this the code to finding the largest number in list

arr = [443,55,66,334,343,7747,886,45,33,3246,77,3,3,7,45,664,5775]

def largest_number(x,y):
    # this method 1st
    if y==0:
        length = len(x)
        greater_number = 0
        for i in range(0,length):
            if greater_number < x[i]:
                greater_number=x[i]
        print (f'this is gratest number in list throw 1st method {greater_number}\n')

    elif y==1:
        
        greater_number = 0

        if greater_number < x[i] and x[::-1]:
            greater_number = x[i]
            print('this the second method {greater_number}')
        else:
            print("this code is not work")

largest_number(arr,0)


def formula_for_reverse_loop(data):

    blank_list = data[::-1]

    print(f"This is reverse list:{blank_list}")

formula_for_reverse_loop (arr)
