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

class Admin(User):
    """Admin information class"""
    def __init__(self, first_name, last_name, city, state, occupation):
        super().__init__(first_name, last_name, city, state, occupation)
        self.privileges = Privileges()

class Privileges(Admin):
    """Privileges for Admin user"""
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post",
                "can deleted port",
                "can ban user",
                "can ban admin",
                "can ban user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")





