#from passlib.utils.compat import native_string_types

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

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=0):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}--kwh battery.")

    def get_range(self):
        """Print a statement describing the battery range"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """ Upgrade the battery size"""
        if self.battery_size != 65:
            self.battery_size = 65
        else:
            self.battery_size()

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to electrics cars.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}--kwh battery.")

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks"""
        print("This car does not have a gas tank!")



my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(10000)
my_new_car.read_odometer()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(f"\n{my_leaf.get_descriptive_name()}")
my_leaf.read_odometer()
my_leaf.increment_odometer(100)
my_leaf.read_odometer()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_tesla = ElectricCar('tesla', 'model 3', 2025)
print(f"\n{my_tesla.get_descriptive_name()}")
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


