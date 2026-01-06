from privileges import Admin, User, Privileges


user1 = User('Morgan', 'Josepher', 'Gilbert', 'Az', 'Network Engineer')
user2 = User('Iggy', 'Ramos', 'Descanso', 'Ca', 'Salesman')
admin1 = Admin('Marty', 'McFly', 'Hill Valley', 'Ca', 'time traveler')

print(f"User 1 is {user1.get_full_name()}.")
print(f"{user1.get_full_name()} lives in {user1.get_location()}.")

print(f"\nUser 2 is {user2.get_full_name()}.")
print(f"{user2.get_full_name()} lives in {user2.get_location()}.")

admin1.privileges.show_privileges()


