import random
import string

digits = list(string.digits)
letters = list(string.ascii_uppercase[:24])

ticket_pool = digits + letters

winning_ticket = random.sample(ticket_pool, 10)

print("Any ticket matching these 4 characters wins a prize!")
print(",".join(winning_ticket))
