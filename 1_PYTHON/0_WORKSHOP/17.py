# 17 - Function to print intersection or common elements of two integer arrays  getCommonElements

def printCommonElements(input1, input2):

    for input1_index in range(0, len(input1), 1):
        isFound = False
        for input2_index in range(0, len(input2), 1):
            if input1[input1_index] == input2[input2_index]:
                isFound = True
                break
        
        if isFound:
            print(input1[input1_index])


def invoke_printCommonElements():
    input1 = [1,2,3,4,7,9,8]
    input2 = [9,6,7,8]

    printCommonElements(input1, input2)

invoke_printCommonElements()