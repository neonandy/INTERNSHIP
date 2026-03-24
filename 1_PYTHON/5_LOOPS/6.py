
#inverted pyramid

def print_inverted_star_pyramid(height):
    for level in range (1, height+1, 1):
        noOfSpaces = level - 1
        noOfStars = (height - level)*2 + 1
        print(noOfSpaces * " " + noOfStars * "*")
        


print_inverted_star_pyramid(5)



#priting the pyramid

def print_star_pyramid(height):
    
    noOfStars = 1
    for level in range(1, height+1, 1):
        noOfSpaces = height - level 
        print(noOfSpaces * " " + noOfStars * "*")
        noOfStars = noOfStars + 2

print_star_pyramid(5)


