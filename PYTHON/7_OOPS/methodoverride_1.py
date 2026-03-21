class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog is Barking")#overrides the parent  class method



#usage
animal = Animal()
dog = Dog()

animal.sound()
dog.sound()