# Running the given recursive function
def mystery(n):
    if n <= 0:
        return 1
    return n * mystery(n - 2)

print(mystery(5))


#cheatsheet
"""
mystery(5)
= 5 * mystery(3)
= 5 * (3 * mystery(1))
= 5 * (3 * (1 * mystery(-1)))
= 5 * 3 * 1 * 1

= 15

"""