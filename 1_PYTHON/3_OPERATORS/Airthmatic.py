def demonstrate_arithmetic_operators():
    # Arithmetic Operators
    countOfMangos, countOfApples = 10, 3
    
    # Addition
    answer = countOfMangos + countOfApples
    print("Arithmetic Operators:")
    print(f"Addition: {countOfMangos} + {countOfApples} = {answer}")
    
    # Subtraction
    answer = countOfMangos - countOfApples
    print(f"Subtraction: {countOfMangos} - {countOfApples} = {answer}")
    
    # Multiplication
    answer = countOfMangos * countOfApples
    print(f"Multiplication: {countOfMangos} * {countOfApples} = {answer}")
    
    # Division
    answer = countOfMangos / countOfApples
    print(f"Division: {countOfMangos} / {countOfApples} = {answer}")
    
    # Modulus
    answer = countOfMangos % countOfApples
    print(f"Modulus: {countOfMangos} % {countOfApples} = {answer}")
    
    # Exponentiation
    answer = countOfMangos ** countOfApples
    print(f"Exponentiation: {countOfMangos} ** {countOfApples} = {answer}")
    
    # Floor Division
    answer = countOfMangos // countOfApples
    print(f"Floor Division: {countOfMangos} // {countOfApples} = {answer}")


def demonstrate_operators():
    demonstrate_arithmetic_operators()


# Run the main demonstration function
demonstrate_operators()
