import random
import string

digits = list(string.digits)
letters = list(string.ascii_uppercase[:5])
ticket_pool = digits + letters
winning_ticket = random.sample(ticket_pool, 4)
attempts = 0

print(f"The winning ticket is:", " ".join(winning_ticket))

while True:
    my_ticket = random.sample(ticket_pool, 4)
    attempts += 1

    print(f"\nMy ticket is", " ".join(my_ticket))

    if my_ticket == winning_ticket:
        print(f"\n🎉 Winner!")
        print(f"It took {attempts} attempts to win!")
        break
my_ticket = random.sample(ticket_pool, 10)

print("Any ticket matching these 4 characters wins a prize!")
print(",".join(winning_ticket))
