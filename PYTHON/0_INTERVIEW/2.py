6️⃣ Fibonacci (Loop)
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
7️⃣ Fibonacci (Recursion)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
8️⃣ Reverse a String
s = input()
print(s[::-1])
9️⃣ Palindrome Check
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
🔟 Sum of Digits
n = int(input())
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)