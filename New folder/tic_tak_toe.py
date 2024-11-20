
if __name__== "__main__":
        # this is the function that play tick tak toe
     def board():   
        first= print(' 1 | 2 | 3 ')
        print("---|---|---")
        second = print(' 4 | 5 | 6 ')
        print("---|---|---")
        third = (' 7 | 8 | 9 ')

     def gameplay():

        enter=input("What do you choose to X|O").lower()
        # for x we need us x and fro zero we use zero
        if enter == "x":
             position = input("Enter you position X")
             for i in range(len(9)):
                 
                if board().first=="1":
                    board().first.replace("X")
                    print(board())

gameplay()



