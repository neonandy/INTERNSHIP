# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Subclass inheriting from Vehicle
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding...")

# Creating object of Bike
my_bike = Bike()

# Calling methods
my_bike.start()   # inherited from Vehicle
my_bike.ride()    # defined in Bike