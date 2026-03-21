class Family:
    def __init__(self, name):
        self.name = name

    def family_name(self):
        return f"The family name is {self.name}"
    
class Person(Family):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def person_info(self):
        return f"{self.family_name()} and the person's age is {self.age}"


person_1 = Person("Smith", 30)
person_2 = Person("Johnson", 25)

print(person_1.person_info())
print(person_2.person_info())