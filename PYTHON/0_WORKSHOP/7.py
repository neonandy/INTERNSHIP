#7 Function to getStrLength to get string length

def getStrLength(string):
    counter = 0

    if string != None:
       for character in string:
            counter =  counter + 1 
    return counter

#invoke

input1 = "NANDAN"  
 
print(f"String length of {input1} is {getStrLength(input1)}")

input2 = None  #none type object is not iterable
 
print(f"String length of {input2} is {getStrLength(input2)}")

input3 = ""  #Empty string
 
print(f"String length of {input3} is {getStrLength(input3)}")
