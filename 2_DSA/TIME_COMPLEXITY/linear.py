#O(n) — Linear Time

def find_maximum(numbers: list) -> int:
    # Must visit EVERY element at least once
    # No way to skip — max could be anywhere
    # 10 items → 10 steps, 1000 items → 1000 steps
    current_max = numbers[0]            # Assume first is max

    for num in numbers:                 # Visit each element once
        if num > current_max:
            current_max = num           # Update max if bigger found

    return current_max

def linear_search(items: list, target: int) -> int:
    # Check one by one from the start
    # Worst case: target is at the end or not present
    for index, item in enumerate(items):    # One pass through entire list
        if item == target:
            return index                    # Found — return position
    return -1                               # Not found

numbers = [3, 7, 1, 9, 2, 5]
print(find_maximum(numbers))            # 9  → checked all 6 items
print(linear_search(numbers, 9))        # 3  → checked 4 items to find it