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
