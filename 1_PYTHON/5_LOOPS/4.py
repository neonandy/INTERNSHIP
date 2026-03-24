
#print line for whole function
def print_stars(maxCount):

    star_string = " "

    for count in range(maxCount):
        star_string = star_string + "*"

    print(star_string)
    
print_stars(10)

#key technic to reduce code only in python
def print_stars_v2(maxCount):
    print(maxCount * "*")


print_stars_v2(10)

#print line for (for loop) 90 degree traingle
def print_stars(maxCount):

    star_string = " "

    for count in range(maxCount):
        star_string = star_string + "*" 

        print(star_string)
    
print_stars(10)

#printing 100 stars in 10 lines
def print_gridstars(maxCount):
    for count in range(maxCount):
        print("*" * maxCount)

print_gridstars(10)


#printing list numbers in *s

#technic 1
def print_list_as_stars(numbers):
    numbers = [2, 4, 6, 8, 10]

    for number in numbers:
        print(number * "*")


print_list_as_stars(4)

#technic 2

def print_list_as_stars(numbers):
    

    for number in numbers:
        for count in range(number):
            print("*", end="")
        print("")

numbers = [2, 4, 6, 8, 10]
print_list_as_stars(numbers)


def print_stars(maxCount):

    star_string = " " 

    for count in range(maxCount):
        for count in range(maxCount):
            star_string = star_string + "*" 

            print(star_string)
    
print_stars(5)



