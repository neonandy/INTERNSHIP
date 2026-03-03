#12. Function to print max and min value from an int array

def getMaxMin(numbers: list)-> tuple[int, int]:
    max = numbers[0]
    min = numbers[0]


    for index in range(1,len(numbers),1):
        if numbers[index]> max:
            max = numbers[index]
        
        if numbers[index]< min :
            min = numbers[index]

    return max, min


    #invoke

input1 = [1, 2, 100, 4, 5 , -1]


resultMax, resultMin = getMaxMin(input1)
(f'{resultMax}, {resultMin} ')