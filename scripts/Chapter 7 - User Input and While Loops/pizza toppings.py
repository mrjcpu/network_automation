prompt = "\nName what pizza toppings you would like to have: "
prompt += "\n(Enter 'quit' when finished)"

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message.title())

