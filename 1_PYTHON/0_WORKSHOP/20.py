#20 - Function to remove spaces from the string  removeSpaces

def removeSpaceFromString(string):
    output = ""

    for character in string:
        if character != ' ' and character != '\t' and character != '\n':
            output = output + character
    
    print(output)

def invoke_removeSpaceFromString():
    input = "  a"
    removeSpaceFromString(input)

## Invocation
invoke_removeSpaceFromString()
















