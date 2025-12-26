#message = input("Enter some text and I will repeat it: ")
#print(message)
from operator import truediv

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

#essage = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)
