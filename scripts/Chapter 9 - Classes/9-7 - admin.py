class User:
    """User information class"""
    def __init__(self, first_name, last_name, city, state, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.occupation = occupation
    def get_full_name(self):
        """Display full name"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()
    def get_location(self):
        """Display location"""
        location = f"{self.city}, {self.state}"
        return location.title()

class Admin:
    """Admin information class"""
    def __init__(self, first_name, last_name, city, state, occupation):
        super().__init__(first_name, last_name, city, state, occupation)
        self.privileges = ["cann add post", "can delete post"]

user1 = User('Morgan', 'Josepher', 'Gilbert', 'Az', 'Network Engineer')
user2 = User('Iggy', 'Ramos', 'Descanso', 'Ca', 'Salesman')

print(f"User 1 is {user1.get_full_name()}.")
print(f"{user1.get_full_name()} lives in {user1.get_location()}.")

print(f"User 2 is {user2.get_full_name()}.")
print(f"{user2.get_full_name()} lives in {user2.get_location()}.")