#braking loop

for number in range(10):
    if number == 5:
        print("Breaking the loop at number 5")
        break
    print(number)


#continue statement

Students = ["anvik", "abhiram", "Nandy", "manju"]

for student in Students:
    if student == "Nandy": 
        print("Skipping nandy here")
        continue
    print(student)

#using list comprehension 

squares = [number ** 2 for number in range(6)] 
print(squares)


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