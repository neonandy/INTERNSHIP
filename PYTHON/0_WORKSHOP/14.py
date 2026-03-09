#14. Function to merge two arrays and return combined output

def mergeTwoArray(list1: list, list2:list):

    for item in list2:
        list1.append(item)
    
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

mergeTwoArray(list1, list2)

print(list1)