file = open("C:/Users/nandan/OneDrive/Desktop/SDE-INTERN/PYTHON/11_FILE_HANDLING/notes.txt", "r")   # "r" = read mode
content = file.read()
file.close()             # must close manually!

print(content)