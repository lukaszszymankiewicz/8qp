import ctypes
from typing import List

from .constants import SIZE, SOLUTIONS
from .transformations import all_transformations


def filter_redundant_solutions(solutions: List[List[int]]) -> List[List[int]]:
    """
    Iterates by all solutions and check whether its transformations (rotation and symmetries) is
    reocurring.

    Args:
        List of lists. Each list is one legal solution to eight queen problem.

    Reutns:
        List of lists (same form ans paramter) but filtered.

    """
    result = []

    for solution in solutions:
        transformed_solutions = [transformation(solution) for transformation in all_transformations]

        if not any(
            [transformed_solution in result for transformed_solution in transformed_solutions]
        ):
            result.append(solution)

    return result


def find_all_solutions() -> List[List[int]]:
    """
    Generates all legal solution to eight queen problem. This algorithm is using custom function
    wrote in C.

    Args:
        None.

    Returns:
        List of combinations which is a legal solution to eight queen problem. Each combination is a
        tuple of eight number. Each of this number represents y-position of a queen on a chessboard,
        while position of number on the list represents queen x-position on a chessboard.
    """

    alg = ctypes.CDLL("./app/src/alg.so")
    alg.solve.restype = ctypes.POINTER(ctypes.c_int)
    solutions_pointer = alg.solve()
    solutions = [[solutions_pointer[i + j] for i in range(SIZE)] for j in range(SOLUTIONS)]

    print(solutions)
    return solutions
