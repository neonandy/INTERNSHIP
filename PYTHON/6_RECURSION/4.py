

def printNumber(number):

    if(number == 0):
        return
    
    number = number - 1

    print(f"Before recursion: {number}")
    printNumber(number)

    print(f"After recursion: {number}")

printNumber(5)