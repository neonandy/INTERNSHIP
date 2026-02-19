#1
students = ["Nandy", "yashas", "abhi", "anvik"]

for student in students:
    print(student)
    print(student.upper()[0:1])

#2
values = range(10)

for item in range(10):
    print(item)


for item in range (0, 10, 1):
    print(item)

for item in range (0, 10, 2):
    print(item)

#for (int index=10, index>1, index--)
#  in C++ is equivalent to for item in range (10, 0, -1) in Python
for item in range (10, 0, -1):
    print(item)
    

#print the multiplication table from 2 to 10
#loop through 2 to 10

for i in range (1, 11):
    print(f"Multiplication table of {i}:")

    #loop through 1 to 10 multiply with i 
    for j in range (1, 11):
        print(f"{i} x {j} = {i*j}")



