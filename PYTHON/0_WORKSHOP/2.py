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