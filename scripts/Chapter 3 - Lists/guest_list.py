guest_list = ['jesus', 'david', 'solomon']

print(f"I would like to invite {guest_list[0].title()}, {guest_list[1].title()}, and {guest_list[2].title()} to dinner.")

print(f"{guest_list[0].title()} cannot make it.")

del guest_list[0]
guest_list.insert(0, 'paul')
print(f"{guest_list[0].title()} can take his place.")

print(f"I would like to invite {guest_list[0].title()}, {guest_list[1].title()}, and {guest_list[2].title()} to dinner.")

guest_list.append('peter')
guest_list.append('samson')
guest_list.append('lot')

print(f"Please {guest_list[0].title()} come to dinner.")
print(f"Please {guest_list[1].title()} come to dinner.")
print(f"Please {guest_list[2].title()} come to dinner.")
print(f"Please {guest_list[3].title()} come to dinner.")
print(f"Please {guest_list[4].title()} come to dinner.")
print(f"Please {guest_list[5].title()} come to dinner.")
print(guest_list)
print("I just found out I can only invite 3 people to dinner")
guest_popped_1 = guest_list.pop(4)
guest_popped_2 = guest_list.pop(2)
guest_popped_3 = guest_list.pop(0)
print(f"I am sorry, {guest_popped_1.title()}, but you cannot come to dinner.")
print(f"I am sorry, {guest_popped_2.title()}, but you cannot come to dinner.")
print(f"I am sorry, {guest_popped_3.title()}, but you cannot come to dinner.")