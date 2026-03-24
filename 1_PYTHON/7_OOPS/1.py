#creating Class

class Human:

    #constructor
    def __init__(self,name):
        self.name = name #instance variable/attribute

    #Methods
    def walk(self):
        print(f"{self.name} is walking")

    def talk(self):
        print(f"{self.name} is talking")

#creating object
nandan = Human("Nandan")
anvik = Human("Anvik")

#calling method
nandan.walk()

print()

anvik.talk()

