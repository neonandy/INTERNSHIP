#nested conditional statements
def test(x):
    if x % 2 == 0:
        if x % 5  == 0:
            return "Divisible by 15"
        else:
            return "Even but not divisible by 10"
    return "odd"
print(test(10))