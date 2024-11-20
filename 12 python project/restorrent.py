# menu = {
#     "pizza": 40,
#     "pasta": 50,
#     "burger": 60,
#     "salad": 70,
#     "coffee": 80
# }

# print("Welcome to PYTHON Restaurant")
# print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80")
# bill_no = 100
# order_total = 0
# current_order_number=100

# def generate_order_number():
#      global current_order_number
#      order_number = current_order_number 
#      current_order_number += 1 
#      return order_number




# def order():
#     global order_total
#     item=input("Enter your order:").lower()

#     if item in menu:
#         order_total+=menu[item]
#         again=input(f"order recieved for {item} total bill rs {order_total} want to place new order Yes/No:")
#         if again=='yes':
#             order()
#         else:
#             print(f"your total bill is {order_total}")    
#             print(f"your Order number is {generate_order_number()}")    
            
# order()

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
current_order_number = 100


def generate_order_number():
    global current_order_number
    current_order_number += 1
    order_number = current_order_number
    current_order_number = order_number
    return order_number

    current_order_number += 1
    
def order():
    global current_order_number
    global order_total
    item = input("Enter your order: ").lower()

    if item in menu:
        order_total += menu[item]
        again = input(f"Order received for {item}. Total bill so far: Rs {order_total}. Want to place another order? Yes/No: ").lower()
        if again == 'yes':
            order()
        else:
            print(f"Your total bill is Rs {order_total}")    
            print(f"Your order number is {generate_order_number()}")
            current_order_number += 1
    else:
        print("Sorry, we don't have that item on the menu.")
        more = input("Would you like to order something else? Yes/No: ").lower()
        if more == 'yes':
            order()

order()
