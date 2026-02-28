#9 Function to Reverse string
def reverseString(string):
    
    length = len(string)
    print(f"Length of string is {length}\n")

    print("First loop:")
    for start in range(0, length, 1):
        print (start)

    print("\nSecond loop:")
    for end in range(length-1, -1, -1):
        print (end)

#invoke
        
name = "abcd"
reverseString(name)

print(name)











def reverseStringsimple(string):
    reversedString = ""
    if string is not None:
        for character in string:
            reversedString = character + reversedString
    return reversedString

#invoke
input1 = "Nandan"
print(f"Reverse of {input1} is {reverseStringsimple(input1)}")