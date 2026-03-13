# 19 - Function to print binary values of various input like integer, char , also perform shift operations on integers

def printBinaryForm(number: int):
    no_of_bits = number.bit_length()
    print(f"Number of bits = {no_of_bits}")

    mask = 1
    mask = mask << no_of_bits-1

    for _ in range(no_of_bits):
        if (number & mask):
            print("1", end=" ")
        else:
            print("0", end=" ")
        
        mask = mask >> 1


def invoke_printBinaryForm():
    printBinaryForm(1)
    printBinaryForm(1024)

invoke_printBinaryForm()