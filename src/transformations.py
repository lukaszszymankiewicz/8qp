from .constants import SIZE


def vertical_symmetry(combination):
    return combination[::-1]


def horizontal_symmetry(combination):
    return [SIZE - number - 1 for number in combination]


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


all_transformations = [
    vertical_symmetry,
    horizontal_symmetry,
    rot90,
    rot180,
    rot270,
    antidiag_symmetry,
    diag_symmetry,
]
