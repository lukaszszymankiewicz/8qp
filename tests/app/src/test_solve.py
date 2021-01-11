import pytest
from app.src.solve import (_combination_is_solution,
                           _get_all_possible_combinations,
                           _get_thretening_fields_for_all_queens,
                           _get_thretening_fields_for_single_queen,
                           filter_redundant_solutions, find_all_solutions)


def test_get_all_possible_combinations_works_properly():
    # GIVEN
    expected_length = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1  # this is equvalent of 8!
    size = 8

    # WHEN
    n_combinations = len(list(_get_all_possible_combinations(size)))

    # THEN
    assert expected_length == n_combinations


def test_get_thretening_fields_for_all_queens_works_properly_for_small_chessboard():
    # GIVEN
    sample_size = 3
    expected_thretening_fields = {
        (0, 0): {(0, 0), (1, 1), (2, 2)},
        (0, 1): {(0, 1), (1, 0), (1, 2)},
        (0, 2): {(2, 0), (1, 1), (0, 2)},
        (1, 0): {(0, 1), (1, 0), (2, 1)},
        (1, 1): {(2, 0), (0, 0), (2, 2), (0, 2), (1, 1)},
        (1, 2): {(0, 1), (2, 1), (1, 2)},
        (2, 0): {(2, 0), (0, 2), (1, 1)},
        (2, 1): {(1, 2), (1, 0), (2, 1)},
        (2, 2): {(0, 0), (1, 1), (2, 2)},
    }

    # WHEN
    thretening_fields = _get_thretening_fields_for_all_queens(sample_size)

    # THEN
    assert len(expected_thretening_fields) == len(thretening_fields)
    assert thretening_fields == expected_thretening_fields


def test_get_thretening_fields_for_all_queens_works_properly_for_normal_size_chessboard():
    # GIVEN
    normal_size = 8
    expected_length = 64

    # WHEN
    thretening_fields = _get_thretening_fields_for_all_queens(normal_size)

    # THEN
    assert expected_length == len(thretening_fields)


@pytest.mark.parametrize(
    "row,col,expected_thretening_fields",
    [
        (0, 0, {(0, 0), (1, 1), (2, 2)}),
        (0, 1, {(0, 1), (1, 0), (1, 2)}),
        (0, 2, {(2, 0), (1, 1), (0, 2)}),
        (1, 0, {(0, 1), (1, 0), (2, 1)}),
        (1, 1, {(2, 0), (0, 0), (2, 2), (0, 2), (1, 1)}),
        (1, 2, {(0, 1), (2, 1), (1, 2)}),
        (2, 0, {(2, 0), (0, 2), (1, 1)}),
        (2, 1, {(1, 2), (1, 0), (2, 1)}),
        (2, 2, {(0, 0), (1, 1), (2, 2)}),
    ],
)
def test_get_thretening_fields_for_single_queen_works_properly(
    row, col, expected_thretening_fields
):
    # GIVEN
    sample_size = 3

    # WHEN
    thretening_fields = _get_thretening_fields_for_single_queen(row, col, sample_size)

    # THEN
    assert expected_thretening_fields == thretening_fields


def test_combination_is_solution_works_properly():
    # GIVEN
    proper_solution = [3, 0, 4, 7, 1, 6, 2, 5]
    nonproper_solution = [1, 2, 3, 4, 5, 6, 7]
    thretening_fields = _get_thretening_fields_for_all_queens(board_size=8)

    # THEN
    assert _combination_is_solution(proper_solution, thretening_fields) is True
    assert _combination_is_solution(nonproper_solution, thretening_fields) is False


def test_find_all_solutions_finds_all_possible_solutions():
    # GIVEN
    expected_number_of_solutions = 92  # due to wikipedia page

    # WHEN
    solutions = find_all_solutions()

    # THEN
    assert len(solutions) == expected_number_of_solutions


def test_filter_redundant_solutions():
    # GIVEN
    expeted_number_of_filtered_solutions = 12  # due to wikipedia page

    # WHEN
    solutions = find_all_solutions()
    filtered_solutions = filter_redundant_solutions(solutions)

    # THEN
    assert len(filtered_solutions) == expeted_number_of_filtered_solutions
