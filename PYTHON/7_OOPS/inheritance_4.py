#Multiple inheritance — two parents

class Phone:
    def call(self):  print("Calling...")
    def text(self):  print("Texting...")

class Camera:
    def click(self):  print("Click! Photo taken")
    def record(self): print("Recording video...")

class SmartPhone(Phone, Camera):   # inherits from BOTH
    def browse(self):
        print("Browsing internet...")

s = SmartPhone()
s.call()    # from Phone    
s.click()   # from Camera   
s.browse()  # own method    

print(SmartPhone.__mro__)
# SmartPhone → Phone → Camera → object