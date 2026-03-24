#2 Function swapNumbers to swap two variables values

def swapNumbers(item1: int, item2: int):

    temp = item1
    item1 = item2
    item2 = temp

    return item1, item2

#invokation code

number1= 10
number2= 20

print(f"Before swapping: value of number1={number1}, number2={number2}")

number1, number2 = swapNumbers(number1, number2)

print(f"After swapping: value of number1={number1}, number2={number2}")

#we can write like this also

def swapSimple(number1, number2):

    return number2, number1

number1 =  10
number2 = 20

print(f"Before swapping: value of number1={number1}, number2={number2}")

number1, number2 = swapSimple(number1, number2)

print(f"After swapping: value of number1={number1}, number2={number2}")


#return keyword is very important in function, it is used to return the value from the function to the caller. If we don't use return keyword then the function will return None by default.