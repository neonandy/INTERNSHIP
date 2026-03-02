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

1️⃣1️⃣ Sum of Digits (Recursion)
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

n = int(input())
print(sum_digits(n))
1️⃣2️⃣ Count Vowels in String
s = input().lower()
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)
1️⃣3️⃣ Find Largest Element in List
lst = list(map(int, input().split()))
print(max(lst))
1️⃣4️⃣ Remove Duplicates from List
lst = list(map(int, input().split()))
print(list(set(lst)))
1️⃣5️⃣ Print Numbers 1 to N (Recursion)
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)

n = int(input())
print_numbers(n)
1️⃣6️⃣ GCD of Two Numbers (Recursion)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input())
b = int(input())
print(gcd(a, b))
1️⃣7️⃣ Power of a Number (Recursion)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

a = int(input())
b = int(input())
print(power(a, b))
1️⃣8️⃣ Count Digits (Recursion)
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

n = int(input())
print(count_digits(n))