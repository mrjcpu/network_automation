class Car:
    """Simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        descriptive_name = f"Vehicle: {self.year} {self.make} {self.model}"
        return descriptive_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")
    def increment_odometer(self, miles):
        """Add  the given amount to the odometer reading"""
        self.odometer_reading += miles
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 40
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}--kwh battery.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.get_descriptive_name()
my_leaf.read_odometer()
my_leaf.increment_odometer(100)
my_leaf.read_odometer()
my_leaf.describe_battery()

#my_new_car.update_odometer(23_500)
#my_new_car.read_odometer()

#my_new_car.increment_odometer(10000)
#my_new_car.read_odometer()