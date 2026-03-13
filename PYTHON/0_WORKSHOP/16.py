# 16 - Function to print unique elements in an integer array   printUniqueElements
# Ignore those numbers completely which have duplicates 

def printUniqueElements(numbers):

    for read_index in range(0, len(numbers), 1):
        isDuplicate = False

        for compare_index in range(0, len(numbers),1):
            if read_index == compare_index:
                continue

            if numbers[read_index] == numbers[compare_index]:
                isDuplicate = True
                break
        
        if(isDuplicate == False):
            # This is unique element, hence print it
            print(numbers[read_index])

def invoke_printUniqueElements():
    input1 = [1,2,3,2,4,1]
    #input1 = [1,2,3,4,5]
    printUniqueElements(input1)

invoke_printUniqueElements()