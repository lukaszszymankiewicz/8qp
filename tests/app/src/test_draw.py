import numpy as np
from app.src.draw import (_create_board, _create_full_colored_field,
                          _create_hash_board, _place_queen_on_board,
                          _read_queen_array)


def test_create_full_colored_field_works_properly():
    # GIVEN
    sample_color = 4
    sample_px_size = 5
    expected_dtype = np.uint8

    # WHEN
    full_colored_field = _create_full_colored_field(sample_color, sample_px_size)

    # THEN
    assert np.all(full_colored_field == sample_color)
    assert full_colored_field.shape == (sample_px_size, sample_px_size)
    assert full_colored_field.dtype == expected_dtype


def test_create_hash_board_works_properly():
    # GIVEN
    sample_light_color = 69
    sample_dark_color = 13
    sample_light_field = np.ones((1, 1), dtype=np.uint8) * sample_light_color
    sample_dark_field = np.ones((1, 1), dtype=np.uint8) * sample_dark_color
    sample_n_elements = 2
    expected_dtype = np.uint8

    # WHEN
    hash_board = _create_hash_board(sample_light_field, sample_dark_field, sample_n_elements)

    # THEN
    assert hash_board.shape == (sample_n_elements, sample_n_elements)
    assert hash_board.dtype == expected_dtype

    assert hash_board[0][0] == sample_light_color
    assert hash_board[0][1] == sample_dark_color
    assert hash_board[1][0] == sample_dark_color
    assert hash_board[1][1] == sample_light_color


def test_create_board_works_properly():
    # GIVEN
    sample_light_color = 69
    sample_dark_color = 13
    sample_n_elements = 2
    sample_px_size = 2
    expected_dtype = np.uint8

    # WHEN
    board = _create_board(
        field_px_size=sample_px_size,
        n_fields=sample_n_elements,
        dark_color=sample_light_color,
        light_color=sample_dark_color,
    )

    # THEN
    assert board.shape == (sample_n_elements * sample_px_size, sample_n_elements * sample_px_size)
    assert board.dtype == expected_dtype

    assert board[0][0] == sample_dark_color
    assert board[0][1] == sample_dark_color
    assert board[0][2] == sample_light_color
    assert board[0][3] == sample_light_color

    assert board[1][0] == sample_dark_color
    assert board[1][1] == sample_dark_color
    assert board[1][2] == sample_light_color
    assert board[1][3] == sample_light_color


def test_read_queen_array_works_properly():
    # GIVEN
    sample_px_size = 100
    expected_dtype = np.uint8

    # WHEN
    queen_array = _read_queen_array()

    # THEN
    assert queen_array.shape == (sample_px_size, sample_px_size)
    assert queen_array.dtype == expected_dtype


def test_place_queen_on_board_works_properly():
    # GIVEN
    sample_row = 0
    sample_col = 0
    sample_board = np.ones(10, 10)
    sample_n_elements = 2
    queen: np.ndarray
