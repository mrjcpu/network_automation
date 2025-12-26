# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'sausage']
    }

print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
