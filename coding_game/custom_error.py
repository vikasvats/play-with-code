# code with harry coustom error
a=int(input("Enter between value 5 to 9"))

if (a<5 or a>9):
    raise ValueError("value sould be between 5 and 9")
else:
    print(f"number is :{a}")

 