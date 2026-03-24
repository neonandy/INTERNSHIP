#13. Function to Search in an sorted array!

def searchInSortedArray(numbers, key):
    leftIndex = 0
    rightIndex = len(numbers)-1
    found = False

    while(leftIndex <= rightIndex):
        middleIndex = int(leftIndex + (rightIndex-leftIndex)/2)

        if(numbers[middleIndex]==key):
            found = True
            break

        if(numbers[middleIndex]>key):
            #you must search on the left side of the array
            rightIndex = middleIndex - 1
        else:
            #you must search on the right side of the array
            leftIndex = middleIndex + 1

    return found
    
def invoke_search():
    input1 = [1, 2, 3, 4, 5, 6]
    key = 7

    result = searchInSortedArray(input1, key)

    if result:
        print("Number is found")
    else:
        print("Number is not found")



invoke_search()



