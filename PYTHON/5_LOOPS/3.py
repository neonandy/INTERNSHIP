#using else with loops

#1
numbers = [2, 4, 5, 6]

for number in numbers:
    print(number)
    if (number == 3):
        print("3 is found so braking!")
        break
else:
    print("3 is not found in the list")

#2
numbers = [2, 4, 3, 5, 6]

for number in numbers:
    print(number)
    if (number == 3):
        print("3 is found so braking!")
        break
else:
    print("3 is not found in the list")