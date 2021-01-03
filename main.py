from itertools import permutations

from .constants import SIZE
from .transformations import all_transformations


def find_solutions():
    results = []

    coords_set = _calculate_coords_set(SIZE)

    # ALL POSSIBLE COMBINATIONS
    for rows_combination in permutations(range(SIZE)):
        result = _place_queens(rows_combination, coords_set)

        if result:
            results.append(list(rows_combination))

    # DELETING REDUNDANT COMBINATIONS
    for combination in results:
        for transformation in all_transformations:
            transformed_result = transformation(combination)

            if transformed_result in results:
                results.remove(transformed_result)

    for result in results:
        print(result)


def _calculate_coords_set(SIZE: int):
    return {
        (row, col): _calculate_coords(row, col) for row in range(0, SIZE) for col in range(0, SIZE)
    }


def _calculate_coords(row: int, col: int) -> set:
    # rows
    rows = {(row, y) for y in range(0, SIZE)}

    # cols
    cols = {(x, col) for x in range(0, SIZE)}

    # diags
    x = range(max(0, row - col), min(SIZE, SIZE - (col - row)))
    y = range(max(0, col - row), min(SIZE, SIZE - (row - col)))
    diags = set(zip(x, y))

    # antidiags
    x = range(max(0, col + row - SIZE + 1), min(SIZE, col + row + 1))
    antidiags = set(zip(x, x[::-1]))

    return rows | cols | diags | antidiags


def _place_queens(rows: set, coords_set) -> bool:
    coords = set()
    for row, col in enumerate(rows):
        if (row, col) in coords:
            return False
        else:
            coords |= coords_set[row, col]

    return True
