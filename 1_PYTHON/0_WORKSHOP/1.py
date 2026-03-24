#1) Function getSum to get sum of numbers

def getSum(number1, number2) -> int:
    return number1 + number2

#invoke

sum = getSum(5, 10)
print("Sum of two numbers is:", sum)

sum2 = getSum(1.2, 2.5)
print("Sum of two numbers is:", sum2)

sum2 = getSum("Hii", " Anu Madum")
print("Sum of two numbers is:", sum2)

#wecan write like this also

def getIntegerSum(number1: int, number2: int)-> int:
    return number1 + number2

print("Sum of two int_Numbers is:", getIntegerSum(1.5, 1.7))
 