#3 Function isEven to return true if number is even otherwise false

def isEven(number: int):
    if number % 2 == 0:
        return True
    else:
        return False
    
#invoke
isEven(10)

#ternary operator
result = "Number is even" if isEven(10) else "Number is odd" 

print(result)

#we can write like this also
def isEvenSimple(number: int):
    return number % 2 == 0
print("Is number even?", isEvenSimple(10))