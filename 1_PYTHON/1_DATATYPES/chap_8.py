#DICTIONARY ~ it is a collection of (key - value) pairs it is accessed by keys not the index

student = { "name" : "Nandan",
           "age": 21,
           "course": "Python"}

print(student)

#ACCESSING
print(student["name"]) #Nandan

#ADDING and UPDATING

student["grade"] = "A"
student["age"] = 22
print(student)

#REMOVING

del student["course"]
print(student)

#NESTED DICT

students = {
    101: {"name": "Nandan", "marks" : 85},
    102: {"name": "Ravi", "marks" : 78}
}

print(students[102]["name"]) #accessing