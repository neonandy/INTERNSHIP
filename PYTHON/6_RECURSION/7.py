def genNumbers(numbers):
    if numbers > 5:
        return
    print(numbers)
    genNumbers(numbers + 1)
genNumbers(1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = 5
print(factorial(num))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter number: "))
result = factorial(n)
print(f"factorial of {n} is", result)

