#functions swapNumbers to swap two variables values

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 7, 2, 9, 5]))


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python Interview"))



