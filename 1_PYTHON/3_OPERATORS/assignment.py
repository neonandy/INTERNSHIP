def demonstrate_assignment_operators():
    # Assignment Operators
    totalScore = 5
    
    # Assign
    answer = totalScore
    print("\nAssignment Operators:")
    print(f"Assign: totalScore = {answer}")
    
    # Add and assign
    # totalScore = totalScore + 2
    totalScore += 2
    answer = totalScore
    print(f"Add and assign: totalScore += 2 -> {answer}")
    
    # Subtract and assign
    totalScore -= 1
    answer = totalScore
    print(f"Subtract and assign: totalScore -= 1 -> {answer}")
    
    # Multiply and assign
    totalScore *= 3
    answer = totalScore
    print(f"Multiply and assign: totalScore *= 3 -> {answer}")
    
    # Divide and assign
    totalScore /= 2
    answer = totalScore
    print(f"Divide and assign: totalScore /= 2 -> {answer}")
    
    # Modulus and assign
    totalScore %= 3
    answer = totalScore
    print(f"Modulus and assign: totalScore %= 3 -> {answer}")
    
    # Floor divide and assign
    totalScore //= 2
    answer = totalScore
    print(f"Floor divide and assign: totalScore //= 2 -> {answer}")
    
    # Exponent and assign
    totalScore **= 3
    answer = totalScore
    print(f"Exponent and assign: totalScore **= 3 -> {answer}")

# Call each function to demonstrate operators
def demonstrate_operators():
    
    demonstrate_assignment_operators()

# Run the main demonstration function
demonstrate_operators()
