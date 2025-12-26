# 6-1 People

users = {
    "mjosepher": {
        "first_name": "dora",
        "last_name": "josepher",
        "age": 44,
        "city": "gilbert",
    },
    "djosepher": {
        "first_name": "dora",
        "last_name": "josepher",
        "age": 44,
        "city": "gilbert",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    city = user_info["city"]

    print(f"Full name: {full_name.title()}")
    print(f"Location: {city.title()}")
