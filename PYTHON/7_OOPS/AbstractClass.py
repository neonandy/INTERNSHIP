from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

# Usage
mgr = Manager(8, 500)
print("Salary:", mgr.calculate_salary())