#6 function to print the ASCII value of a character/string input

def printASCIIvalue(string):
    for character in string:
        print(f"ASCII value of {character} is --> {ord(character)}") 

#invoke
printASCIIvalue("ABC")
 
print()

printASCIIvalue("123")

print()

printASCIIvalue("abc")

#ord() is a std library used to find ascii values