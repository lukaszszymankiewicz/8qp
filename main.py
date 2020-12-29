from itertools import permutations

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


results = []

coords_set = {
    (row, col): calculate_coords(row, col) for row in range(0, size) for col in range(0, size)
}

# ALL POSSIBLE COMBINATIONS
for rows_combination in permutations(range(size)):
    result = place_queens(rows_combination)

    if result:
        results.append(list(rows_combination))

# TRANSFORMATIONS:
def vertical_symmetry(combination):
    return combination[::-1]


def horizontal_symmetry(combination):
    return [size - number - 1 for number in combination]


def rot90(combination):
    numbers = range(8)
    result = [0] * 8
    orders = [7 - c for c in combination]

    for number, order in zip(numbers, orders):
        result[order] = number
    return result


def rot180(combination):
    return [7 - c for c in combination][::-1]


def rot270(combination):
    numbers = range(8)[::-1]
    result = [0] * 8

    for number, order in zip(numbers, combination):
        result[order] = number

    return result


def diag_symmetry(combination):
    numbers = range(8)
    result = [0] * 8

    for number, order in zip(numbers, combination):
        result[order] = number

    return result


def antidiag_symmetry(combination):
    numbers = range(8)[::-1]
    orders = [7 - c for c in combination]
    result = [0] * 8

    for number, order in zip(numbers, orders):
        result[order] = number

    return result


# DELETING REDUNDANT COMBINATIONS
transformations = [
    vertical_symmetry,
    horizontal_symmetry,
    rot90,
    rot180,
    rot270,
    antidiag_symmetry,
    diag_symmetry,
]

for combination in results:
    for transformation in transformations:
        transformed_result = transformation(combination)

        if transformed_result in results:
            results.remove(transformed_result)

for result in results:
    print(result)
