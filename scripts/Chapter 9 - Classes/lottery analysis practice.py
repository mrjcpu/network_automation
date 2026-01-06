import random
import string

digits = list(string.digits)
letters = list(string.ascii_uppercase[:4])
ticket_pool = digits + letters
winning_ticket = random.sample(ticket_pool, 4)
attempts = 0

print("And the winning ticket is:"," ".join(winning_ticket))

while True:
    my_ticket = random.sample(ticket_pool, 4)
    attempts += 1

    print(f"\nMy ticket is:", " ".join(my_ticket))

    if my_ticket == winning_ticket:
        print(f"\nYou win with {" ".join(my_ticket)}!")
        print(f"It took {attempts} attempts!")
        break

my_ticket = random.sample(ticket_pool, 4)
