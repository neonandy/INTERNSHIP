#without condition

def increment_and_print(counter: int):

    counter =  counter + 1
    print(f"{counter}")

    increment_and_print(counter)

increment_and_print(2)

#withcondition

def increment_and_print(counter: int):
    if counter >= 10:
        return
    counter =  counter + 1
    print(f"{counter}")

    increment_and_print(counter)

increment_and_print(1)


#simple example
def increment_and_print(counter: int):
    if (counter >= 2):
        return    
    
    counter = counter + 1
    
    print(f"{counter}")
    increment_and_print(counter)
    print(f"{counter}")
    

increment_and_print(0)

