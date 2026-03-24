#function isnumber to return true if is is an integer 

def isNumber(number):

    isInteger = True #flag variable

    for eachCharacter in number:
        if (eachCharacter >= '0' and eachCharacter <= '9'):
            continue
        else:
            isInteger = False
            break

    return isInteger

#invoke

result = "it is an integer" if isNumber("a123b") else "it is not an integer"
print(result)

#we can write like this also
def isNumberSimple(number):
    #
    for eachCharacter in number:
        if (eachCharacter < '0' or eachCharacter > '9'):
            return False
    return True

result = isNumberSimple("a1234")

print("it is a number", result)
    