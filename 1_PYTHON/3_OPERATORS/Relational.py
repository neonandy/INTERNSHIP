def demonstrate_relational_operators():
    # Relational Operators
    countOfMangos, countOfApples = 10, 3
    
    # Equal to
    answer = countOfMangos == countOfApples
    print("\nRelational Operators:")
    print(f"Equal to: {countOfMangos} == {countOfApples} -> {answer}")
    
    # Not equal to
    answer = countOfMangos != countOfApples
    print(f"Not equal to: {countOfMangos} != {countOfApples} -> {answer}")
    
    # Greater than
    answer = countOfMangos > countOfApples
    print(f"Greater than: {countOfMangos} > {countOfApples} -> {answer}")
    
    # Less than
    answer = countOfMangos < countOfApples
    print(f"Less than: {countOfMangos} < {countOfApples} -> {answer}")
    
    # Greater than or equal to
    answer = countOfMangos >= countOfApples
    print(f"Greater than or equal to: {countOfMangos} >= {countOfApples} -> {answer}")
    
    # Less than or equal to
    answer = countOfMangos <= countOfApples
    print(f"Less than or equal to: {countOfMangos} <= {countOfApples} -> {answer}")


# Call each function to demonstrate operators
def demonstrate_operators():
    demonstrate_relational_operators()
    
# Run the main demonstration function
demonstrate_operators()
