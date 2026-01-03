class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 22
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    def flavor(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")


ice_cream_shop = IceCreamStand("Baskin Robbins", "ice cream")
print(f"Welcome to {ice_cream_shop.restaurant_name} where we serve {ice_cream_shop.cuisine_type}!")
ice_cream_shop.flavor()
print(f"Number of people served: {ice_cream_shop.number_served}")





