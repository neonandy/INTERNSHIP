def demonstrate_logical_operators():
    # Logical Operators
    isReady, isGood = True, False
    
    # AND
    answer = isReady and isGood
    print("\nLogical Operators:")
    print(f"AND: {isReady} and {isGood} -> {answer}")
    
    # OR
    answer = isReady or isGood
    print(f"OR: {isReady} or {isGood} -> {answer}")
    
    # NOT
    answer = not isReady
    print(f"NOT: not {isReady} -> {answer}")



# Call each function to demonstrate operators
def demonstrate_operators():
    
    demonstrate_logical_operators()
    
# Run the main demonstration function
demonstrate_operators()
