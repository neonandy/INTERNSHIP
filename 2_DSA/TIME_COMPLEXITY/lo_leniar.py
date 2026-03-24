#O(n log n) — Log-linear Time

def merge_sort(items: list) -> list:
    # SPLIT phase: keeps dividing list in half → O(log n) splits
    # MERGE phase: merges sorted halves → O(n) work per level
    # Combined: O(n log n)

    if len(items) <= 1:
        return items                    # Base case — single item is already sorted

    mid = len(items) // 2              # Find midpoint

    left_half  = merge_sort(items[:mid])   # Recursively sort left half
    right_half = merge_sort(items[mid:])   # Recursively sort right half

    return merge_sorted_halves(left_half, right_half)   # Merge the two sorted halves

def merge_sorted_halves(left: list, right: list) -> list:
    merged = []
    i = 0
    j = 0

    # Compare elements from both halves one by one
    # Always pick the smaller one and move forward
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])     # Left element is smaller — take it
            i += 1
        else:
            merged.append(right[j])    # Right element is smaller — take it
            j += 1

    merged += left[i:]                 # Append any remaining left elements
    merged += right[j:]                # Append any remaining right elements
    return merged

numbers = [5, 2, 8, 1, 9, 3]
print(merge_sort(numbers))             # [1, 2, 3, 5, 8, 9]
# Split:  [5,2,8] [1,9,3] → [5,2] [8] [1,9] [3] → [5] [2] [8] [1] [9] [3]
# Merge:  [2,5] [8] [1,9] [3] → [2,5,8] [1,3,9] → [1,2,3,5,8,9] ✅