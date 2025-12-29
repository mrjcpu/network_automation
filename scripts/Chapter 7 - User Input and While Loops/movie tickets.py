prompt = "\nWhat is your age? (Enter 'quit' to exit): "

while True:
    message = input(prompt)

    if message.lower() == "quit":
        break

    if not message.isdigit():
        print("Please enter a valid number.")
        continue

    age = int(message)

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")