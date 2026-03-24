#15. Function to get Second largest element in an array

def getSecondLargest(numbers: list)-> int:

    largestMax = numbers[0]
    Secondlargest = numbers[0]

    for index in range(1, len(numbers), 1):
        #if new number we scanned is greater
        if numbers[index] > largestMax:
            SecondLargest = largestMax
            largestMax = numbers[index]
        else:
            numbers[index]> Secondlargest
            SecondLargest = numbers[index]

    return SecondLargest




input1 = [-1, -2,  -5]
result = getSecondLargest(input1)
print(f"second Largest number is {result}")


