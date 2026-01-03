class User:
    """User information class"""
    def __init__(self, first_name, last_name, city, state, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.occupation = occupation
        self.login_attempts = 0
    def get_full_name(self):
        """Display full name"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()
    def get_location(self):
        """Display location"""
        location = f"{self.city}, {self.state}"
        return location.title()
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Morgan', 'Josepher', 'Gilbert', 'Az', 'Network Engineer')
user2 = User('Iggy', 'Ramos', 'Descanso', 'Ca', 'Salesman')

print(f"\nUser 1 is {user1.get_full_name()}.")
print(f"{user1.get_full_name()} lives in {user1.get_location()}.")
increment_login_attempts = user1.increment_login_attempts()
print(f"Login Attempts: {user1.login_attempts}.")
reset_login_attempts = user1.reset_login_attempts()
print(f"Login Attempts: {user1.login_attempts}.")

print(f"\nUser 2 is {user2.get_full_name()}.")
print(f"{user2.get_full_name()} lives in {user2.get_location()}.")
increment_login_attempts = user2.increment_login_attempts()
print(f"Login Attempts: {user2.login_attempts}.")
reset_login_attempts = user2.reset_login_attempts()
print(f"Login Attempts: {user2.login_attempts}.")