
class Animal:
    def make_sound(self):#one method name
        print("The animal makes a sound.")

class Dog(Animal):#diffrent behaviour
    def make_sound(self):
        print("Barking")

class Cat(Animal):
    def make_sound(self):#diffrent behaviour
        print("Meowing")


#creating object
animal = Animal()
dog = Dog()
cat = Cat()

#calling method


animal.make_sound()
dog.make_sound()
cat.make_sound()