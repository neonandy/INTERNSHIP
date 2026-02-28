#1.SET ~ it is an UNORDERED(no indexing) collection of unique elements it is MUTABLE {}
numbers = {10, 20, 30, 30}
print(numbers) #{10,20,30} ~ duplicate elements can be removed

#ADD and REMOVE
numbers.add(40)
numbers.remove(20)
print(numbers)

#MEMBERSHIP
print(30 in numbers)
print(50 not in numbers)

#OPERATIONS
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B) #UNION {1, 2, 3, 4, 5}
print(A & B) #INTERSECTION {3}
print(A - B) #DIFFERENCE {1, 2}


#2.FROZENSET ~ it is an IMMUTABLE and UNORDERED version of a set
ids = frozenset([101, 102, 103])
print(ids)

#IMMUTABILITY (Cannot be Change)
ids.add(104) #error

#difference between set and frozenset is
    #  (SET can Changeble and can add and remove)
    #  (FROZENSET cannot be changeble and cannot be add and remove) 

#byte array ~ is a mutable sequence of bytes (values 0 - 255)

data = bytearray([65, 66, 67])
print(data)