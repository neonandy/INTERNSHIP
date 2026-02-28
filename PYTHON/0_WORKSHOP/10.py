#10 function to bhet sum of all elements in a integer array get sum

def get_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number


    return sum

#invoke
numbers = [1, 2, 3, 4, 5]
result = get_sum(numbers)
print("Sum of the numbers =", result)



def get_sumSimple(numbers):

   # sum = 0
    length = len(numbers)
    
    for index in range(0, length, 1):
        sum = sum + numbers[index]
    
    return sum

numbers = ["nandy", "sandy", "andy", "mandy"]
result = get_sumSimple(numbers)
print("Sum of the numbers =", result)