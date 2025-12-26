users = {
    'mjosepher': {
        'first': 'morgan',
        'last': 'josepher',
        'age': 45,
        'city': 'Gilbert',
        'state': 'Arizona'
    },
    'djosepher': {
        'first': 'dora',
        'last': 'josepher',
        'age': 44,
        'city': 'Gilbert',
        'state': 'Arizona'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['city']}, {user_info['state']}"

    print("User's info:")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")
