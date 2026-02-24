
#concatinating with list
def print_star_grid_concat(gridSize):
    for row in range(gridSize):
        printMsg = []
        for noOfStars in range(gridSize):
            printMsg.append("*")

        print("".join(printMsg))
    
print_star_grid_concat(5)


#printing star only at borders/ skipping the border

def print_star_grid_borders_only(gridSize):
    for row in range(1, gridSize+1, 1):
        printMsg = []

        for column in range(1, gridSize+1, 1):
            isStar = column == 1 or column == gridSize or row == 1 or row == gridSize
            # Use conditional expression to append "*" or " "
            printMsg.append("*" if isStar else " ")
            #printMsg.append(str(row) + "," + str(column) + " ")

        print("".join(printMsg))
    
print_star_grid_borders_only(5)


