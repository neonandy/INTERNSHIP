#O(log n) — Logarithmic Time

def binary_search(sorted_items: list, target: int) -> int:
    low = 0
    high = len(sorted_items) - 1

    # Each iteration cuts the search space in HALF
    # 1000 items → ~10 iterations max
    # 1,000,000 items → ~20 iterations max
    while low <= high:
        mid = (low + high) // 2         # Find the middle index

        if sorted_items[mid] == target:
            return mid                  # Found it!

        elif sorted_items[mid] < target:
            low = mid + 1               # Discard LEFT half — target is bigger

        else:
            high = mid - 1             # Discard RIGHT half — target is smaller

    return -1                           # Target not found

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(numbers, 7))    # Output: 3 (index of 7)
# Step 1: mid=11, too big → look left
# Step 2: mid=5,  too small → look right
# Step 3: mid=7,  found! ✅ — only 3 steps for 8 items