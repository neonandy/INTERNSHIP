class Calculator:
    def multiply(self, a, b, c=None):
        if c is not None:
            return a * b * c
        return a * b

# Usage
calc = Calculator()
print(calc.multiply(2, 3))        # 2 args
print(calc.multiply(2, 3, 4))     # 3 args