#11. function to find given string is palindrome!

def isPalindrome(string):
    leftIndex = 0
    rightIndex = len(string) - 1
    result = True

    while(leftIndex < rightIndex):
        if string[leftIndex] != string[rightIndex]:
            result = False
            break

        leftIndex += 1
        rightIndex -= 1

    return result

input1 = "MaM" 
input2 = "MalayalaM"
input3 = "NandaN"

result = isPalindrome(input3)
#result = isPalindrome(input2)
#result = isPalindrome(input3)

if result :
    print("String Is Palindrome!")
else:
    print("String is not Palindrome")