#creating a class

class Mobile:

    #constructor
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price


#creating object
mobile_1 = Mobile("Nokia", 15000)
mobile_2 = Mobile("Samsung", 20000)

print(f"Brand of mobile_1: {mobile_1.brand}")
print(f"Price of mobile_1: {mobile_1.price}")

print(f"Brand of mobile_2: {mobile_2.brand}")
print(f"Price of mobile_2: {mobile_2.price}")