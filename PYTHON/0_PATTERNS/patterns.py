
# ─────────────────────────────────────────────
#  HARD PATTERNS  (22–25)
# ─────────────────────────────────────────────

def x_pattern(size):
    """Pattern 22: X shape along both diagonals."""
    last_index = size - 1
    for row in range(size):
        cells = ''
        for col in range(size):
            is_main_diagonal  = (col == row)
            is_anti_diagonal  = (col == last_index - row)
            cells += '*' if (is_main_diagonal or is_anti_diagonal) else ' '
        print(cells)


def plus_pattern(size):
    """Pattern 23: Plus (+) shape through the center."""
    mid = size // 2
    for row in range(size):
        cells = ''
        for col in range(size):
            is_center_row = (row == mid)
            is_center_col = (col == mid)
            cells += '*' if (is_center_row or is_center_col) else ' '
        print(cells)


def hollow_diamond(num_rows):
    """Pattern 24: Diamond with only its border drawn."""
    for row in range(1, num_rows + 1):
        leading_spaces = ' ' * (num_rows - row)
        if row == 1:
            print(leading_spaces + '*')
        else:
            inner_gap = ' ' * (2 * row - 3)
            print(leading_spaces + '*' + inner_gap + '*')
    for row in range(num_rows - 1, 0, -1):
        leading_spaces = ' ' * (num_rows - row)
        if row == 1:
            print(leading_spaces + '*')
        else:
            inner_gap = ' ' * (2 * row - 3)
            print(leading_spaces + '*' + inner_gap + '*')


def fibonacci_triangle(num_rows):
    """Pattern 25: Triangle where each row extends the Fibonacci sequence."""
    fib_sequence = [1, 1]
    while len(fib_sequence) < num_rows:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    for row in range(1, num_rows + 1):
        terms = ' '.join(str(fib_sequence[i]) for i in range(row))
        print(terms)

