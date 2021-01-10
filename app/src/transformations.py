from typing import List

from .constants import SIZE, SIZE_RANGE

"""
Here are all transformations functions. Every each of them is taking proper solution
expresed as list of integer numbers and transforms it (resulting same format result).
"""


def vertical_symmetry(combination: List[int]) -> List[int]:
    return combination[::-1]


def horizontal_symmetry(combination: List[int]) -> List[int]:
    return [SIZE - number - 1 for number in combination]


def rot90(combination: List[int]) -> List[int]:
    numbers = SIZE_RANGE
    result = [0] * SIZE
    orders = [SIZE - 1 - c for c in combination]

    for number, order in zip(numbers, orders):
        result[order] = number

    return result


def rot180(combination: List[int]) -> List[int]:
    return [SIZE - 1 - c for c in combination][::-1]


def rot270(combination: List[int]) -> List[int]:
    numbers = SIZE_RANGE[::-1]
    result = [0] * SIZE

    for number, order in zip(numbers, combination):
        result[order] = number

    return result


def diag_symmetry(combination: List[int]) -> List[int]:
    numbers = SIZE_RANGE
    result = [0] * SIZE

    for number, order in zip(numbers, combination):
        result[order] = number

    return result


def antidiag_symmetry(combination: List[int]) -> List[int]:
    numbers = SIZE_RANGE[::-1]
    orders = [SIZE - 1 - c for c in combination]
    result = [0] * SIZE

    for number, order in zip(numbers, orders):
        result[order] = number

    return result


all_transformations = [
    vertical_symmetry,
    horizontal_symmetry,
    rot90,
    rot180,
    rot270,
    antidiag_symmetry,
    diag_symmetry,
]
