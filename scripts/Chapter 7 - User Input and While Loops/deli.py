sandwich_orders = ['pastrami', 'turkey club','pastrami', 'monte cristo', 'pastrami', 'cheesesteak']
available_orders = ['turkey club', 'monte cristo', 'cheesesteak']
finished_sandwiches = []

#print(sandwich_orders)
#print(finished_sandwiches)

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()

    if sandwich_order not in available_orders:
        print(f"Sorry, we are out of {sandwich_order}")
        continue

    print(f"We finished your {sandwich_order.title()} sandwich!")
    finished_sandwiches.append(sandwich_order)

print("\nThe following sandwich orders are completed:")
for sandwich_order in finished_sandwiches:
    print(sandwich_order.title())


