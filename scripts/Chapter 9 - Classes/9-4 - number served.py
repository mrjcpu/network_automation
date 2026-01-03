class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    def restaurant(self):
        print(f"{self.number_served}")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, served):
        self.number_served += served


restaurant1 = Restaurant('North Italia', 'Italian')
restaurant2 = Restaurant('P.F. Chang\'s', 'Chinese')
restaurant3 = Restaurant('Cheesecake Factory', 'American')


restaurant1.set_number_served(11)
restaurant2.set_number_served(12)
restaurant3.set_number_served(13)

print(f"\nRestaurant 1: {restaurant1.restaurant_name}, Cuisine: {restaurant1.cuisine_type}")
restaurant1.describe_restaurant()
print(f"{restaurant1.restaurant_name} served {restaurant1.number_served} in its first week!")
restaurant1.increment_number_served(20)
print(f"{restaurant1.restaurant_name} served {restaurant1.number_served} in its second week!")

print(f"\nRestaurant 2: {restaurant2.restaurant_name}, Cuisine: {restaurant2.cuisine_type}")
restaurant2.describe_restaurant()
print(f"{restaurant2.restaurant_name} served {restaurant2.number_served} in its first week!")
restaurant2.increment_number_served(20)
print(f"{restaurant2.restaurant_name} served {restaurant2.number_served} in its second week!")

print(f"\nRestaurant 3: {restaurant3.restaurant_name}, Cuisine: {restaurant3.cuisine_type}")
restaurant3.describe_restaurant()
print(f"{restaurant3.restaurant_name} served {restaurant3.number_served} in its first week!")
restaurant3.increment_number_served(20)
print(f"{restaurant3.restaurant_name} served {restaurant3.number_served} in its second week!")