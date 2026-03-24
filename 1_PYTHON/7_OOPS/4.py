#optional arguments in constructor
class Engineer :


    #constructor with optional arguments
    def __init__(self,name = "Unknown", field = "IT"):
        self.name = name
        self.field = field

    #method 
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Field: {self.field}")


#creating object
engineer_1 = Engineer("Nandan", "Software")
engineer_2 = Engineer()

#calling method
engineer_1.display_info()
engineer_2.display_info()