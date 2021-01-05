from itertools import permutations

from .constants import SIZE, SIZE_RANGE
from .transformations import all_transformations


def _calculate_coords_set():
    return {(row, col): _calculate_coords(row, col) for row in SIZE_RANGE for col in SIZE_RANGE}


def _calculate_coords(row: int, col: int) -> set:
    # rows
    rows = {(row, y) for y in SIZE_RANGE}

    # cols
    cols = {(x, col) for x in SIZE_RANGE}

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


def solve():
    results = []
    coords_set = _calculate_coords_set()

    # ALL POSSIBLE COMBINATIONS
    for rows_combination in permutations(SIZE_RANGE):
        result = _place_queens(rows_combination, coords_set)

        if result:
            results.append(list(rows_combination))

    # DELETING REDUNDANT COMBINATIONS
    for combination in results:
        for transformation in all_transformations:
            transformed_result = transformation(combination)

            if transformed_result in results:
                results.remove(transformed_result)

    return results
