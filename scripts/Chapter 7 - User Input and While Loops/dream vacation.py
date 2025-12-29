destinations = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    destination = input("What is your favorite destination? ")
    destinations[name] = destination

    repeat = input("Would you like to ask someone else? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n---Polling Results---")
for name, destination in destinations.items():
    print(f"{name} would like to go to {destination}")


