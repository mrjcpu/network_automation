def greet_users(names):
    """Print a simple greeting to each user in the lists"""
    for name in names:
        msg=f"Hello {name.title()}. How are you today?"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)