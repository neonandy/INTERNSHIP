a = int(input("A:"))
b = int(input("B:"))

try:
    print(a/b)
except Exception as e:
    print(f"Error barthide guru {e}")
    b = int(input("Mathe try maaadu -- B:"))
    print(a/b)
else: 
    print("Enu error barlilla")
    
finally:
    print("i dont fkkng care if error comes or not!")