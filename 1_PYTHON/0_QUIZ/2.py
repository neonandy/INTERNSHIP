#operator precedence
def tricky(a,b):

    return a//b+a%b*a**b

print (tricky(5, 2))

#cheatsheet
"""
Python does NOT calculate left to right blindly.
It follows precedence order:

** (Power)

*, /, //, %

+, -

output = (5//2) + ((5%2 * 5**2)) = 27

"""
