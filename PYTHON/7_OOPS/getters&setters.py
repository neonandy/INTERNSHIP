class Student:
    def __init__(self, name, age):
        self.__name = name #private
        self.__age = age 

    def get_name(self):#getters
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_name(self, name):#setters
        self.__name = name

    def set_age(self, age):
        if isinstance(age, int) :
            self.__age = age
        else:
            print("Invalid age")

        


s = Student("Nandan", 21)

print("Before setting")
print(s.get_name())
print(s.get_age())

print()

s.set_name("Anvik")
s.set_age(22)

print("After setting")
print(s.get_name())
print(s.get_age())
    