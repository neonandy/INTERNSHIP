def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def DisplayMenu():
    print("----SIMPLE CALCULATOR----")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. ExitQuit")
    
while (True):
    DisplayMenu()
    choice = int(input("Enter your choice:"))

    if choice in {1, 2, 3}:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
    if choice == 1:
        print("Result:",add(a,b))
    elif choice == 2:
        print("Result:",sub(a,b))
    elif choice == 3:
        print("Result:",mul(a,b))
    elif choice == 4:
        print("Quitting....") 
        break
    else:
        print("Invalid choice! Try Again")
                    

