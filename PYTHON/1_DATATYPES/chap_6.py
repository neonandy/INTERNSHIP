#LIST ~ it is a ordered , mutable(changeable) colection of elemnts ~ [] , it is one of the most widely used data structure

fruits = ["apple", "banana", "orange"]
print(fruits)

#mutable
fruits[1] = "mango"
print(fruits) # ['apple', 'mango', 'orange']

#Adding Elements to a List

#1.append() ~ add one element at the end
fruits.append("grape")
print(fruits)

#2.insert() ~ Add at a specific index
fruits.insert(1, "kiwi")
print(fruits)

#Remove Elements from a list
#1.remove() ~ remove by value
fruits.remove("apple")
print(fruits)

#2.pop() ~ remove by index
fruits.pop(0)
print(fruits)

#indexing
print(fruits[0])#apple
print(fruits[-1])#orange

#slicing
fruits = ["apple", "banana", "orange", "carrot", "Beetroot"]
print(fruits[1:4])

