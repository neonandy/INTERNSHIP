#Multilevel inheritance

class Animal:
    def eat(self):   print("Eating")
    def sleep(self): print("Sleeping")

class Dog(Animal):
    def bark(self):  print("Woof!")

class GuideDog(Dog):           # inherits from Dog, which inherits from Animal
    def guide(self):
        print("Guiding owner safely")

g = GuideDog()
g.eat()    # from Animal   
g.bark()   # from Dog      
g.guide()  # own method    

print(GuideDog.__mro__) 
#(Method Resolution Order) shows the exact chain Python searches when you call any method.
# GuideDog → Dog → Animal → object