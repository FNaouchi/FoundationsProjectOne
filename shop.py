####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Coded Bakery"
signature_flavors = ["banana", "orange", "date", "lemon"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our Menu:")
    for i in menu:
        print("- \"%s\" (KD %.3f)" %(i, menu[i]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for i in original_flavors:
        print("- \"%s\"" %(i))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for i in signature_flavors:
        print("- \"%s\"" %(i))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in original_flavors or order in menu or order in signature_flavors:
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    while(True):
        order = input()
        if order == "exit" or order == "Exit":
            break
        else:
            if is_valid_order(order) == True:
                order_list.append(order)
            else:
                print("Invalid input")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        return "Total price is eligible for credit card payment."
    else:
        return "Total price is NOT eligible for credit card payment."
    


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0.0
    for i in order_list:
        if i in original_flavors:
            total = total + 2
        elif i in signature_flavors:
            total = total + 2.75
        elif i in menu:
            total = total + menu[i]
        else:
            print("Error in counting")
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for i in order_list:
        print("- %s" %(i))

    total = get_total_price(order_list)
    print()
    print("Your total price is %.3f KD" %(total))
    print("%s" %(accept_credit_card(total)))
    print("Thank you for shopping at %s" %(cupcake_shop_name))
