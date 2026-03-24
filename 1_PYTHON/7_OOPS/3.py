#creating a class

class Student :

    #constructor
    def __init__(self,name,marks):
        self.name = name #instance variable/attribute
        self.marks = marks #instance variable/attribute

    #method
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

#creating object

student_1 = Student("Nandan", 85)
student_2 = Student("Anvik", 90)

#calling method
student_1.display_info(
student_2.display_info()