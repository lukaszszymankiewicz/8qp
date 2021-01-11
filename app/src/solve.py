from itertools import permutations
from typing import Dict, Generator, List, Set, Tuple

from .constants import SIZE
from .transformations import all_transformations


def _get_thretening_fields_for_all_queens(
    board_size: int,
) -> Dict[Tuple[int, int], Set[Tuple[int, int]]]:
    """
    Generates dict containing all thretening fields by queen.

    Such dict containts every possible queen place on chessboards and its thretening fields. Such
    generation is done only once to save computing power and re-use every time needed.

    Args:
        board_size: integer number representing number of fields in chessboard.

    Retuns:
        dict which looks like:
            >>> {(0, 0): {(0, 0), (1, 0), (2, 0), (...)},
                {(1, 0): {(1, 0), (1, 0), (2, 0), (...)},

    """
    return {
        (row, col): _get_thretening_fields_for_single_queen(row, col, board_size)
        for row in range(board_size)
        for col in range(board_size)
    }


def _get_thretening_fields_for_single_queen(row: int, col: int, size: int) -> Set[Tuple[int, int]]:
    """
    Generates thretening fileds for on queen. Thus algorithm by definition excludes such combintaion
    which have queen on same row or column, there is no need for generating thretening fields on
    column and rows, only diagonal (and antidiagonal) fields are generated.

    Args:
        row: integer number, y-position of queen on a chessboard,
        col: integer number, x-position of queen on a chessboard,
        size: integer representing number of fields in rows and column in chessboard.

    Returns:
        Single set containing coordinates of thretening fields by one queen expressed by set of
        tuples. Each tuple is expressing coordinates of one field.
    """
    # diags
    x = range(max(0, row - col), min(size, size - (col - row)))
    y = range(max(0, col - row), min(size, size - (row - col)))
    diags = set(zip(x, y))

    # antidiags
    x = range(max(0, col + row - size + 1), min(size, col + row + 1))
    antidiags = set(zip(x, x[::-1]))

    return diags | antidiags


def _combination_is_solution(
    combination: set, thretening_fields: Dict[Tuple[int, int], Set[Tuple[int, int]]]
) -> bool:
    """
    Having single combination of rows (and column) where queens need to be put on chessboard,
    calculates if any of them are thretening each other. To do so queens, one by one, is putting on
    chessboard and checking ehter its thretening fields have any field in common.

    Args:
        combination: set of integer numbers, each number represents its y-position, while number
            position on such sets represents its x-position.
        coords_set: dict containing all thretened fields of queen by its place on chessboard, such
            dict is generated only once, and pass every time function runs.

    Returns:
        boolean indication if inputted combintaion containes two thretening queens.
    """
    coords = set()

    for row, col in enumerate(combination):
        if (row, col) in coords:
            return False
        else:
            coords |= thretening_fields[row, col]

    return True


def _get_all_possible_combinations(size: int) -> Generator:
    """
    Creates generator which will yield all queens combination on chessboard.

    Sample combination will looks like this:
        (1, 2, 5, 3, 7, 0, 4, 6)

    Each number represents y-position on chessboard, while number position in tuple represents
    x-postion on chessboard. Generating permutations of list of numbers from 1 to 8 returns in every
    possible combinations of queens.

    Args:
        size: number of following number to generate permutations from.
    """
    return permutations(range(size))


def find_all_solutions(size: int = SIZE) -> List[List[int]]:
    """
    Generates all legal solution to eight queen problem.

    Args:
        size - integer number representing number of fileds from which board is consisted.

    Returns:
        List of combinations which is a legal solution to eight queen problem. Each combination is a
        tuple of eight number. Each of this number represents y-position of a queen on a chessboard,
        while position of number on the list represents queen x-position on a chessboard.
    """
    solutions = []

    thretening_fields = _get_thretening_fields_for_all_queens(size)
    all_possible_combinations = _get_all_possible_combinations(size)

    for combination in all_possible_combinations:
        if _combination_is_solution(combination, thretening_fields):
            solutions.append(list(combination))

    return solutions


def filter_redundant_solutions(solutions: List[List[int]]) -> List[List[int]]:
    """
    Iterates by all solutions and check whether its transformations (rotation and symmetries) is
    reocurring.

    Args:
        List of lists. Each list is one legal solution to eight queen problem.

    Reutns:
        List of lists (same form ans paramter) but filtered.

    """
    for solution in solutions:
        for transformation in all_transformations:
            transformed_solution = transformation(solution)

            if transformed_solution in solutions:
                solutions.remove(transformed_solution)

    return solutions
