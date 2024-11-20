
num1=int(input("enter you number:"))
calc=input("sum.sub,multi,devide:").lower()
num2=int(input("enter you number:"))

if calc=="sum":
    print(num1+num2)
elif calc=="sub":
    print(num1-num2)
elif calc=="multi":
    print(num1*num2)
elif calc=="devide":
    print(num1/num2)

