
# This is the restaurant management system

# Define the menu of the restaurant
menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}

print("Welcome to PYTHON Restaurant")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80")
order_total = 0

anything_else=False

def order_again():

    order_number = 100
    item = input("Enter your order: ").lower()

    if item in menu:
        global order_total
        
        global anything_else
        order_total += menu[item]
        print(f"Item added your order total Rs {order_total}")

        more=input("Do you want anything else Yes/No:").lower()
        if more=="yes":
            anything_else=True
        else:
            print(f"Your total bill is {order_total}")
            order_number+=1
            print(f"Your order number is {order_number}")
            

    else:
        print("Sorry, we don't have that item on the menu.")

order_again()

while anything_else==True:
     order_again()
    
else:
     print(f"Your order total is Rs {order_total}")
    