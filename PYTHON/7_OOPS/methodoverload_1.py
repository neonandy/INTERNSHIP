#python doesnt support tru method overloading

class calculator:
    def add(self, a, b, c=0):#default parameter
        return a + b + c

# Creating object
calc = calculator()

# Calling the same method with different number of arguments
print(f"Sum of 2 numbers: {calc.add(10, 20)}")
print(f"Sum of 3 numbers: {calc.add(10, 20, 30)}")
