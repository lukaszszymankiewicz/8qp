import pytest
from app.src.transformations import (antidiag_symmetry, diag_symmetry,
                                     horizontal_symmetry, rot90, rot180,
                                     rot270, vertical_symmetry)


@pytest.mark.parametrize(
    "transformation, expected_combination",
    [
        (vertical_symmetry, [2, 6, 1, 7, 5, 3, 0, 4]),
        (horizontal_symmetry, [3, 7, 4, 2, 0, 6, 1, 5]),
        (rot90, [4, 6, 3, 0, 2, 7, 5, 1]),
        (rot180, [5, 1, 6, 0, 2, 4, 7, 3]),
        (rot270, [6, 2, 0, 5, 7, 4, 1, 3]),
        (antidiag_symmetry, [3, 1, 4, 7, 5, 0, 2, 6]),
        (diag_symmetry, [1, 5, 7, 2, 0, 3, 6, 4]),
    ],
)
def test_transformation_returns_proper_results(transformation, expected_combination):
    # GIVEN
    base_combination = [4, 0, 3, 5, 7, 1, 6, 2]

    # WHEN
    transformed_combination = transformation(base_combination)

    # THEN
    assert sorted(transformed_combination) == list(range(8))
    assert transformed_combination == expected_combination
