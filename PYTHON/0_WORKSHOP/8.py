#8 Function to get vowels count

def CountVowels(string):

    counter = 0
    if string is not None: #best practice
        for character in string:
            if(character == 'a' or
            character == 'e' or
            character == 'i' or
            character == 'o' or
            character == 'u' or
            character == 'A' or
            character == 'E' or
            character == 'I' or
            character == 'O' or
            character == 'U'):
                counter = counter + 1
    return counter

#invoke

input1 = None
print(f"Number of vowels in {input1} is : {CountVowels(input1)}")

input2 = ""
print(f"Number of vowels in {input2} is : {CountVowels(input2)}")

input3 = "N"
print(f"Number of vowels in {input3} is : {CountVowels(input3)}")

input4 = "Nandan"
print(f"Number of vowels in {input4} is : {CountVowels(input4)}")