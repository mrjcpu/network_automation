##5-1car = 'subaru'
#if car == 'subaru':
#    print("I predict True")
#else:
#    print("I predict False")

#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')

#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')

##5-2
#car = "Tesla"
#if car == car.title():
#    print("The car is not a Ford")
#else:
#    print("The car is Ford")

#mileage = 18653
#if mileage >= 30000:
#    print(f"Mileage is greater than 30000 by {mileage-30000} miles")
#else:
#    print(f"Mileage is less than 30000 by {30000-mileage} miles")

#if mileage % 2 == 0:
#    print(f"Mileage is and even number")
#else:
#    print(f"Mileage is and odd number")

#car_list = ['audi', 'ford', 'bmw']
#if car in car_list:
#    print(f"The car is in the list of cars")
#else:
#    print(f"The car is not in the list of cars")

##5-3 through 5-5 - Alien Colors
#alien_color = 'green'

#if alien_color == 'green':
#    points = 5
#if alien_color == 'blue':
#    points = 10
#if alien_color == ('red'):
#    points = 15

#if points == 15:
#    print (f"You scored {points} points from a headshot!")
#elif points == 10:
#    print (f"You scored {points} but did not score a headshot!")
#elif points == 5:
#    print (f"You scored {points} and barely hit the enemy!")

#5-6 - Stages of Life
#age = 66

#if age < 2:
#    print("You are a baby.")
#if age >= 2 and age < 4:
#    print("You are a toddler.")
#if age >= 4 and age < 13:
#    print("You are a kid.")
#if age >= 13 and age < 20:
#    print("You are a teenager.")
#if age >= 20 and age < 65:
#    print("You are an adult.")
#if age >= 65:
#    print("You are an elder.")

##5-7 Favorite Fruit
#favorite_fruits = ['apple', 'orange', 'plum', 'grapes', 'watermelon']

#if 'apple' in favorite_fruits:
#    print("Yes, apple is one of my favorite fruits")
#else:
#    print("No, apple is not one of my favorite fruits")

#if 'orange' in favorite_fruits:
#    print("Yes, orange is one of my favorite fruits")
#else:
#    print("No, orange is not one of my favorite fruits")

##5-8 through 9 Hello Admin
#usernames = []

#if not usernames:
#    print(f"Please enter a username")
#for username in usernames:
#    if username == 'admin':
#        print(f"Hello {username}, would you like to configure a change?")
#    else:
#        print(f"Hello {username.title()}, welcome!")

##5-10 - Checking Usernames
#current_users = ['admin', 'JACK', 'jIll', 'Morgan', 'alexandra']
#new_users = ['dora', 'michelle', 'nani', 'JILL', 'Alexandra']
#current_users_upper = [user.upper() for user in current_users]
#current_users_title = [user.title() for user in current_users]
#current_users_normalized = {user.lower() for user in current_users}
#print(current_users_normalized)

#for users in new_users:
#    if users in current_users:
#        print(f"The user '{users}' has already been used.")
#    elif users in current_users_upper:
#        print(f"The user '{users}' has already been used.")
#    elif users in current_users_title:
#        print(f"The user '{users}' has already been used.")
#    if users.lower() in current_users_normalized:
#        print(f"The user '{users}' has already been used.")
#    else:
#        print(f"The user '{users}' has not been used.")

##5-11 Ordinal Numbers
#numbers = list(range(1,11))
#for number in numbers:
#    if number == 1:
#        print("1st")
#    elif number == 2:
#        print("2nd")
#    elif number == 3:
#        print("3rd")
#    else:
#        print(f"{number}th")



special_suffixes = {1: "st", 2: "nd", 3: "rd"}

for number in range(1, 11):
    suffix = special_suffixes.get(number, "th")
    print(f"{number}{suffix}")