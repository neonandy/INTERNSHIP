# ─────────────────────────────────────────────
#  MEDIUM PATTERNS  (13–21)
# ─────────────────────────────────────────────

def centered_pyramid(num_rows):
    """Pattern 13: Centered star pyramid."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * (2 * row - 1)
        print(leading_spaces + stars)


def inverted_pyramid(num_rows):
    """Pattern 14: Inverted centered pyramid."""
    for row in range(num_rows, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * (2 * row - 1)
        print(leading_spaces + stars)


def diamond_pattern(num_rows):
    """Pattern 15: Full diamond (pyramid + inverted pyramid)."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * (2 * row - 1)
        print(leading_spaces + stars)
    for row in range(num_rows - 1, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * (2 * row - 1)
        print(leading_spaces + stars)


def hollow_square(size):
    """Pattern 16: Square with only the border filled."""
    for row in range(size):
        is_border_row = (row == 0 or row == size - 1)
        if is_border_row:
            print('*' * size)
        else:
            inner_spaces = ' ' * (size - 2)
            print('*' + inner_spaces + '*')


def hollow_triangle(num_rows):
    """Pattern 17: Triangle with only the border filled."""
    for row in range(1, num_rows + 1):
        if row == 1:
            print('*')
        elif row == num_rows:
            print('*' * num_rows)
        else:
            inner_spaces = ' ' * (row - 2)
            print('*' + inner_spaces + '*')


def butterfly_pattern(num_rows):
    """Pattern 18: Butterfly — two mirrored triangles."""
    for row in range(1, num_rows + 1):
        gap = ' ' * (2 * (num_rows - row))
        wings = '*' * row
        print(wings + gap + wings)
    for row in range(num_rows - 1, 0, -1):
        gap = ' ' * (2 * (num_rows - row))
        wings = '*' * row
        print(wings + gap + wings)


def hourglass_pattern(num_rows):
    """Pattern 19: Hourglass — inverted pyramid then pyramid."""
    for row in range(num_rows, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * (2 * row - 1)
        print(leading_spaces + stars)
    for row in range(2, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '*' * (2 * row - 1)
        print(leading_spaces + stars)


def checkerboard_pattern(size):
    """Pattern 20: Alternating star-space checkerboard."""
    for row in range(size):
        cells = ''.join('*' if (row + col) % 2 == 0 else ' ' for col in range(size))
        print(cells)


def number_pyramid(num_rows):
    """Pattern 21: Pyramid where numbers decrease then increase."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        descending = ''.join(str(num) for num in range(row, 0, -1))
        ascending  = ''.join(str(num) for num in range(2, row + 1))
        print(leading_spaces + descending + ascending)