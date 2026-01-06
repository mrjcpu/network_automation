from restaurant import Restaurant

restaurant1 = Restaurant('North Italia', 'Italian')
restaurant2 = Restaurant('P.F. Chang\'s', 'Chinese')
restaurant3 = Restaurant('Cheesecake Factory', 'American')

print(f"Restaurant 1: {restaurant1.restaurant_name}, Cuisine: {restaurant1.cuisine_type}")
restaurant1.describe_restaurant()
print(f"Restaurant 2: {restaurant2.restaurant_name}, Cuisine: {restaurant2.cuisine_type}")
restaurant2.describe_restaurant()
print(f"Restaurant 3: {restaurant3.restaurant_name}, Cuisine: {restaurant3.cuisine_type}")
restaurant3.describe_restaurant()