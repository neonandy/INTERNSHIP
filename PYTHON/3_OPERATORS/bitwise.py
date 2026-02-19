def demonstrate_bitwise_operators():
    # Bitwise Operators
    redTeamScore, whiteTeamScore = 5, 2  # redTeamScore = 101 in binary, whiteTeamScore = 10 in binary
    
    # AND
    answer = redTeamScore & whiteTeamScore
    print("\nBitwise Operators:")
    print(f"AND: {redTeamScore} & {whiteTeamScore} -> {answer}")
    
    # OR
    answer = redTeamScore | whiteTeamScore
    print(f"OR: {redTeamScore} | {whiteTeamScore} -> {answer}")
    
    # XOR
    answer = redTeamScore ^ whiteTeamScore
    print(f"XOR: {redTeamScore} ^ {whiteTeamScore} -> {answer}")
    
    # NOT
    answer = ~redTeamScore
    print(f"NOT: ~{redTeamScore} -> {answer}")
    
    # Left shift
    answer = redTeamScore << whiteTeamScore
    print(f"Left shift: {redTeamScore} << {whiteTeamScore} -> {answer}")
    
    # Right shift
    answer = redTeamScore >> whiteTeamScore
    print(f"Right shift: {redTeamScore} >> {whiteTeamScore} -> {answer}")


# Call each function to demonstrate operators
def demonstrate_operators():
    
    demonstrate_bitwise_operators()
    

# Run the main demonstration function
demonstrate_operators()
