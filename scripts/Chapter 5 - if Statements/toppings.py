availble_toppings = ['mushrooms', 'pineapple', 'pepperoni']
requested_toppings = ['pepperoni', 'pineapple']


for requested_topping in requested_toppings:
    if requested_topping in availble_toppings:
        print(f"Adding {requested_topping} to the list of toppings")
    else:
        print(f"We are out of {requested_topping}")

