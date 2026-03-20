class Database:

    def __init__(self):
        self.__storage = {} #private variable to store data

    def write(self, key, value, ):
        self.__storage[key] = value #encapsulated method to write data

    def read(self, key):
        if key in self.__storage:
            print( self.__storage[key]) #encapsulated method to read data
        else:
            print("DB item not available")

db = Database()

db.write("name", "Nandan")
db.write("age", 25,)
db.read("name")
db.read("age")
db.read("city")