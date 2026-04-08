#O(n²) — Quadratic Time
def bubble_sort(items: list) -> list:
    n = len(items)

    # Outer loop runs n times
    for i in range(n):

        # Inner loop runs ~n times for each outer iteration
        # Total iterations: n × n = n²
        for j in range(n - i - 1):

            # Compare adjacent elements
            if items[j] > items[j + 1]:
                # Swap them if they are in wrong order
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

def find_duplicate_pairs(numbers: list):
    pairs = []

    # Every element is compared with every OTHER element
    # 5 items → 25 comparisons, 100 items → 10,000 comparisons
    for i in range(len(numbers)):               # Outer loop: each element
        for j in range(i + 1, len(numbers)):    # Inner loop: every element after i
            if numbers[i] == numbers[j]:
                pairs.append((numbers[i], numbers[j]))  # Found a duplicate pair

    return pairs

numbers = [5, 3, 1, 4, 2]
print(bubble_sort(numbers))                 # [1, 2, 3, 4, 5]

data = [1, 3, 2, 3, 1, 5]
print(find_duplicate_pairs(data))           # [(1, 1), (3, 3)]