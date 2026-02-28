#Tuples ~ is a ordered collection of elements , tht is immutable(can't be change) & Elements have fixed positins ~ ()

colors = ("red","green","blue")
print(colors)

#indexing
print(colors[0]) #'red'
print(colors[-1])#'blue'

#slicing
colors = ("red","green","blue", "black")
print(colors[1:3])


#immutable
#colors[0] = "yellow"  #error cant be add or change the tuple

#with mixed data types
student = ("Nandan" , 22, "Python")
print(student) 



#membership ~ used to check whether a value exists 

numbers = (10, 20, 30, 40)

print(20 in numbers) #true
print(50 in numbers) #false


#EXAMPLE for BOTH

allowed_ids = (101, 102, 103)

user_id = 102
if user_id in allowed_ids:
    print("Access Granted")
else:
    print("Access denied")

user_id = 104
if user_id in allowed_ids:
    print("Access Granted")
else:
    print("Access denied")

    

