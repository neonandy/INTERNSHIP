# 18 - Function to get count of words in the string  getCountOfWords
# There will be no word or atleast one word in the input
def getWordCount(string):
    counter = 1

    if (len(string) == 0):
        return 0
    
    for char in string:
        if char == ' ' or char == '\t' or char == '\n':
            counter+=1
  
    return counter


def invoke_getWordCount():
    input = ""
    count = getWordCount(input)
    print(f"Count of words = {count}")

invoke_getWordCount()
