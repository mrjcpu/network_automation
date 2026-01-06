import random
import string

digits = list(string.digits)
letters = list(string.ascii_uppercase[:4])

ticket_pool = digits+letters

winning_ticket = random.sample(ticket_pool, 6)

print("And the winning ticket is:")
print(" ".join(winning_ticket))


