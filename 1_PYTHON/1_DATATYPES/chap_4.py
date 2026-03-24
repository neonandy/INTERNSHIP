#INDEXING ~ (used to access a single element)

#1.positive index (start from left side)

text = "PYTHON"
print (text[0]) #P
print (text[3]) #H

print(text[6]) #out of range error

#2.negative index (start from right side -1)

print(text[-1]) #N
print(text[-3]) #H

print(text[-7]) #out of range error

#SLICING ~ (used to extract multiple elements from a sequence)

#syntax - sequence[start: stop: step]


word = "PYTHON"
print(word[1:4])#YTH

#start
print(word[:3])#PYT
print(word[3:])#HON
#step
print(word[::2])#PTO
#reverse
print(word[::-1]) #NOHTYP


#ENCODING ~ (used to covert text (string) to bytes )

text = "Python"
encoded = text.encode("utf-8") #b'Python'
print(encoded)

decoded = encoded.decode("utf-8")
print(decoded)









