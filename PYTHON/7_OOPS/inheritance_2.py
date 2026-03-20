
#single inheritance
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):   # Inheriting from Animal

    def bark(self):
        print("Dog is barking")


# Usage
d = Dog()
d.eat()    # inherited method
d.bark()   # own method