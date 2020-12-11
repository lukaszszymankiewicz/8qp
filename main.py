from itertools import permutations

import time

size = 8


def calculate_coords(row: int, col: int) -> set:
    # rows
    rows = {(row, y) for y in range(0, size)}

    # cols
    cols = {(x, col) for x in range(0, size)}

    # diags
    x = range(max(0, row - col), min(size, size - (col - row)))
    y = range(max(0, col - row), min(size, size - (row - col)))
    diags = set(zip(x, y))

    # antidiags
    x = range(max(0, col + row - size + 1), min(size, col + row + 1))
    antidiags = set(zip(x, x[::-1]))

    return rows | cols | diags | antidiags


def place_queens(rows: set) -> bool:
    coords = set()
    for row, col in enumerate(rows):
        if (row, col) in coords:
            return False
        else:
            coords |= coords_set[row, col]

    return True


a = set(range(size))

results = []

coords_set = {
    (row, col): calculate_coords(row, col)
    for row in range(0, size)
    for col in range(0, size)
}

for rows_combination in permutations(a):
    result = place_queens(rows_combination)

    if result:
        results.append(rows_combination)
