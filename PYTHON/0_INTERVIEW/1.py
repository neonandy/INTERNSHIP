1️⃣ Even or Odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
2️⃣ Largest of Three Numbers
a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c))
3️⃣ Check Prime Number
n = int(input())
if n < 2:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
4️⃣ Factorial (Loop)
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
5️⃣ Factorial (Recursion)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))

