SIZE = 5  # Default grid size used by all patterns


# ─────────────────────────────────────────────
#  EASY PATTERNS  (1–12)
# ─────────────────────────────────────────────

def right_angle_triangle(num_rows):
    """Pattern 1: Right-angle triangle growing downward."""
    for row in range(1, num_rows + 1):
        print('*' * row)


def inverted_right_triangle(num_rows):
    """Pattern 2: Right-angle triangle shrinking downward."""
    for row in range(num_rows, 0, -1):
        print('*' * row)


def square_pattern(size):
    """Pattern 3: Solid square of stars."""
    for row in range(size):
        print('*' * size)


def right_aligned_triangle(num_rows):
    """Pattern 4: Triangle aligned to the right side."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * row
        print(leading_spaces + stars)


def number_triangle(num_rows):
    """Pattern 5: Triangle filled with incrementing numbers."""
    for row in range(1, num_rows + 1):
        digits = ''.join(str(col) for col in range(1, row + 1))
        print(digits)


def same_number_rows(num_rows):
    """Pattern 6: Each row repeats its own row number."""
    for row in range(1, num_rows + 1):
        print(str(row) * row)


def floyds_triangle(num_rows):
    """Pattern 7: Floyd's triangle with sequential numbers."""
    counter = 1
    for row in range(1, num_rows + 1):
        row_values = []
        for col in range(row):
            row_values.append(str(counter))
            counter += 1
        print(' '.join(row_values))


def alphabet_triangle(num_rows):
    """Pattern 8: Triangle filled with letters A, B, C..."""
    for row in range(1, num_rows + 1):
        letters = ''.join(chr(ord('A') + col) for col in range(row))
        print(letters)


def inverted_triangle(num_rows):
    """Pattern 9: Inverted right-angle triangle."""
    for row in range(num_rows, 0, -1):
        print('*' * row)


def mirrored_right_triangle(num_rows):
    """Pattern 10: Stars grow from right, pointing left."""
    for row in range(num_rows, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * row
        print(leading_spaces + stars)


def binary_triangle(num_rows):
    """Pattern 11: Triangle alternating 0 and 1."""
    for row in range(1, num_rows + 1):
        cells = ''.join(str((row + col) % 2) for col in range(row))
        print(cells)


def counting_triangle(num_rows):
    """Pattern 12: Each row prints 1 through row_number."""
    for row in range(1, num_rows + 1):
        numbers = ' '.join(str(col) for col in range(1, row + 1))
        print(numbers)


counting_triangle(6)