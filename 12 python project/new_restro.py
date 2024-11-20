import random
# make a restrorent ordering system!

menu={
    "pizza":40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,

}
print("Welcome to the Python restaurent")

print(
    'pizza :40\n'
    'pasta :50\n'
    'burger:60\n'
    'salad :70\n'
    'coffee:80\n'
)
order_total=0
order_number=100

def next_order():
    # global order_total
    order_next = input("Do you want to place next order Yes/no:").lower()
    if order_next=="yes":
        order_now()
    else:
        print(f"Thank you ordering with us your total is {order_total}")
        print(f'your order number is ',random.randint(100, 900))


def ordering_system(item):
    global order_total
    order_total+=menu[item]

    next_order()

def order_now():
    global menu
    order=input("What do you want to order: ").lower()
    # print(order)
    for item in menu:
        if item == order:
            ordering_system(item)

order_now()

