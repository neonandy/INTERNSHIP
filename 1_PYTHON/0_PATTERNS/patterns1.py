# ============================================================
#    25 Star & Number Patterns (from image)
#    Clean variable and function names throughout
# ============================================================

SIZE = 5  # Default size used by all patterns


def print_section(pattern_number, title):
    """Print a neat header before each pattern."""
    print(f"\n{'='*45}")
    print(f"  Pattern {pattern_number:02d}: {title}")
    print('='*45)


# ─────────────────────────────────────────────
#  ROW 1
# ─────────────────────────────────────────────

def square_hollow_pattern(size):
    """Pattern 01: Square with hollow center — only border stars."""
    for row in range(size):
        is_border_row = (row == 0 or row == size - 1)
        if is_border_row:
            print('* ' * size)
        else:
            inner_spaces = '  ' * (size - 2)
            print('* ' + inner_spaces + '*')


def number_triangular(num_rows):
    """Pattern 02: Each row repeats its row number that many times."""
    for row in range(1, num_rows + 1):
        numbers = ' '.join(str(row) for _ in range(row))
        print(numbers)


def number_increasing_pyramid(num_rows):
    """Pattern 03: Each row prints 1 through row number."""
    for row in range(1, num_rows + 1):
        numbers = ' '.join(str(col) for col in range(1, row + 1))
        print(numbers)


def number_increasing_reverse_pyramid(num_rows):
    """Pattern 04: Inverted — row count decreases, numbers start from 1."""
    for row in range(num_rows, 0, -1):
        numbers = ' '.join(str(col) for col in range(1, row + 1))
        print(numbers)


def number_changing_pyramid(num_rows):
    """Pattern 05: Floyd's triangle — sequential numbers row by row."""
    counter = 1
    for row in range(1, num_rows + 1):
        row_values = []
        for col in range(row):
            row_values.append(str(counter))
            counter += 1
        print(' '.join(row_values))


# ─────────────────────────────────────────────
#  ROW 2
# ─────────────────────────────────────────────

def zero_one_triangle(num_rows):
    """Pattern 06: Alternating 0 and 1, starting based on row parity."""
    for row in range(num_rows):
        cells = ' '.join(str((row + col) % 2) for col in range(row + 1))
        print(cells)


def palindrome_triangular(num_rows):
    """Pattern 07: Each row is a palindrome of numbers (high to low to high)."""
    for row in range(1, num_rows + 1):
        descending = list(range(row, 0, -1))
        ascending  = list(range(2, row + 1))
        full_row   = descending + ascending
        print(' '.join(str(n) for n in full_row))


def rhombus_pattern(num_rows):
    """Pattern 08: Parallelogram / rhombus of stars."""
    for row in range(num_rows):
        leading_spaces = ' ' * (num_rows - row - 1)
        stars = '* ' * num_rows
        print(leading_spaces + stars)


def diamond_pattern(num_rows):
    """Pattern 09: Full diamond — pyramid on top, inverted on bottom."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '* ' * row
        print(leading_spaces + stars)
    for row in range(num_rows - 1, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '* ' * row
        print(leading_spaces + stars)


def butterfly_star_pattern(num_rows):
    """Pattern 10: Butterfly — two mirrored triangles meeting in center."""
    for row in range(1, num_rows + 1):
        left_wing  = '* ' * row
        gap        = '  ' * (num_rows - row)
        right_wing = '* ' * row
        print(left_wing + gap + right_wing)
    for row in range(num_rows - 1, 0, -1):
        left_wing  = '* ' * row
        gap        = '  ' * (num_rows - row)
        right_wing = '* ' * row
        print(left_wing + gap + right_wing)


# ─────────────────────────────────────────────
#  ROW 3
# ─────────────────────────────────────────────

def square_fill_pattern(size):
    """Pattern 11: Square with alternating star columns."""
    for row in range(size):
        cells = '* ' * size
        print(cells)


def right_half_pyramid(num_rows):
    """Pattern 12: Stars grow from 1 up to num_rows (left-aligned)."""
    for row in range(1, num_rows + 1):
        print('* ' * row)


def reverse_right_half_pyramid(num_rows):
    """Pattern 13: Stars shrink from num_rows down to 1 (left-aligned)."""
    for row in range(num_rows, 0, -1):
        print('* ' * row)


def left_half_pyramid(num_rows):
    """Pattern 14: Stars grow, right-aligned."""
    for row in range(1, num_rows + 1):
        leading_spaces = '  ' * (num_rows - row)
        stars = '* ' * row
        print(leading_spaces + stars)


def reverse_left_half_pyramid(num_rows):
    """Pattern 15: Stars shrink, right-aligned."""
    for row in range(num_rows, 0, -1):
        leading_spaces = '  ' * (num_rows - row)
        stars = '* ' * row
        print(leading_spaces + stars)


# ─────────────────────────────────────────────
#  ROW 4
# ─────────────────────────────────────────────

def k_pattern(num_rows):
    """Pattern 16: K-shape — vertical bar on left with diagonal arms."""
    mid = num_rows // 2
    for row in range(num_rows):
        distance_from_mid = abs(row - mid)
        stars = '* ' * (num_rows - distance_from_mid)
        print(stars)


def triangle_star_pattern(num_rows):
    """Pattern 17: Right-aligned growing triangle (centered spacing)."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        stars = '* ' * row
        print(leading_spaces + stars)


def reverse_number_triangle_pattern(num_rows):
    """Pattern 18: Numbers print from current row up to num_rows, shifting right."""
    for row in range(1, num_rows + 1):
        leading_spaces = '  ' * (row - 1)
        numbers = ' '.join(str(col) for col in range(row, num_rows + 1))
        print(leading_spaces + numbers)


def mirror_image_triangle_pattern(num_rows):
    """Pattern 19: Top-half mirror — numbers shrink then grow back."""
    for row in range(num_rows, 0, -1):
        leading_spaces = '  ' * (num_rows - row)
        numbers = ' '.join(str(col) for col in range(1, row + 1))
        print(leading_spaces + numbers)
    for row in range(2, num_rows + 1):
        leading_spaces = '  ' * (num_rows - row)
        numbers = ' '.join(str(col) for col in range(1, row + 1))
        print(leading_spaces + numbers)


def hollow_triangle_pattern(num_rows):
    """Pattern 20: Triangle with only the border printed."""
    for row in range(1, num_rows + 1):
        if row == 1:
            leading_spaces = ' ' * (num_rows - 1)
            print(leading_spaces + '*')
        elif row == num_rows:
            print('* ' * num_rows)
        else:
            leading_spaces = ' ' * (num_rows - row)
            inner_gap      = '  ' * (row - 2)
            print(leading_spaces + '* ' + inner_gap + '*')


# ─────────────────────────────────────────────
#  ROW 5
# ─────────────────────────────────────────────

def hollow_reverse_triangle_pattern(num_rows):
    """Pattern 21: Hollow inverted triangle — border stars only."""
    for row in range(num_rows, 0, -1):
        if row == num_rows:
            print('* ' * num_rows)
        elif row == 1:
            leading_spaces = ' ' * (num_rows - 1)
            print(leading_spaces + '*')
        else:
            leading_spaces = ' ' * (num_rows - row)
            inner_gap      = '  ' * (row - 2)
            print(leading_spaces + '* ' + inner_gap + '*')


def hollow_diamond_pyramid(num_rows):
    """Pattern 22: Diamond with only its border drawn."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        if row == 1:
            print(leading_spaces + '*')
        else:
            inner_gap = '   ' * (row - 2)
            print(leading_spaces + '* ' + inner_gap + ' *')
    for row in range(num_rows - 1, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        if row == 1:
            print(leading_spaces + '*')
        else:
            inner_gap = '   ' * (row - 2)
            print(leading_spaces + '* ' + inner_gap + ' *')


def hollow_hourglass_pattern(num_rows):
    """Pattern 23: Hollow hourglass — border stars only."""
    for row in range(num_rows, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        if row == num_rows:
            print(leading_spaces + '* ' * row)
        elif row == 1:
            print(leading_spaces + '*')
        else:
            inner_gap = '  ' * (row - 2)
            print(leading_spaces + '* ' + inner_gap + ' *')
    for row in range(2, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        if row == num_rows:
            print(leading_spaces + '* ' * row)
        else:
            inner_gap = '  ' * (row - 2)
            print(leading_spaces + '* ' + inner_gap + ' *')


def pascals_triangle(num_rows):
    """Pattern 24: Pascal's triangle using combinations."""
    from math import comb
    for row in range(num_rows):
        leading_spaces = ' ' * (num_rows - row - 1)
        values = ' '.join(str(comb(row, col)) for col in range(row + 1))
        print(leading_spaces + values)


def right_pascals_triangle(num_rows):
    """Pattern 25: Pascal's triangle aligned to the right."""
    from math import comb
    for row in range(num_rows):
        values = ' '.join(str(comb(row, col)) for col in range(row + 1))
        print(values)
    for row in range(num_rows - 2, -1, -1):
        values = ' '.join(str(comb(row, col)) for col in range(row + 1))
        print(values)


# ─────────────────────────────────────────────
#  MAIN — Run all 25 patterns
# ─────────────────────────────────────────────

if __name__ == '__main__':
    print_section(1,  "Square Hollow Pattern");          square_hollow_pattern(SIZE)
    print_section(2,  "Number Triangular");              number_triangular(SIZE)
    print_section(3,  "Number Increasing Pyramid");      number_increasing_pyramid(SIZE)
    print_section(4,  "Number Increasing Reverse");      number_increasing_reverse_pyramid(SIZE)
    print_section(5,  "Number Changing Pyramid");        number_changing_pyramid(SIZE)
    print_section(6,  "Zero-One Triangle");              zero_one_triangle(SIZE)
    print_section(7,  "Palindrome Triangular");          palindrome_triangular(SIZE)
    print_section(8,  "Rhombus Pattern");                rhombus_pattern(SIZE)
    print_section(9,  "Diamond Pattern");                diamond_pattern(SIZE)
    print_section(10, "Butterfly Star Pattern");         butterfly_star_pattern(SIZE)
    print_section(11, "Square Fill Pattern");            square_fill_pattern(SIZE)
    print_section(12, "Right Half Pyramid");             right_half_pyramid(SIZE)
    print_section(13, "Reverse Right Half Pyramid");     reverse_right_half_pyramid(SIZE)
    print_section(14, "Left Half Pyramid");              left_half_pyramid(SIZE)
    print_section(15, "Reverse Left Half Pyramid");      reverse_left_half_pyramid(SIZE)
    print_section(16, "K Pattern");                      k_pattern(SIZE)
    print_section(17, "Triangle Star Pattern");          triangle_star_pattern(SIZE)
    print_section(18, "Reverse Number Triangle");        reverse_number_triangle_pattern(SIZE)
    print_section(19, "Mirror Image Triangle");          mirror_image_triangle_pattern(SIZE)
    print_section(20, "Hollow Triangle Pattern");        hollow_triangle_pattern(SIZE)
    print_section(21, "Hollow Reverse Triangle");        hollow_reverse_triangle_pattern(SIZE)
    print_section(22, "Hollow Diamond Pyramid");         hollow_diamond_pyramid(SIZE)
    print_section(23, "Hollow Hourglass Pattern");       hollow_hourglass_pattern(SIZE)
    print_section(24, "Pascal's Triangle");              pascals_triangle(SIZE)
    print_section(25, "Right Pascal's Triangle");        right_pascals_triangle(SIZE)
