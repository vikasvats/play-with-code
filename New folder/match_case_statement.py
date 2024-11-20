x = int(input("Enter your number:"))
match x:
    case 0:
        print("case is 0")
    case 4:
        print("case is 4")
    case 7:
        print("case is 7")
    case _ if x<80:
        print("x is less than 80")
    case _ if x<70:
        print("x is less than 70")