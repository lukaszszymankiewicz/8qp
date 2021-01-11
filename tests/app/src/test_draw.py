import glob
import os

import numpy as np
from app.src.constants import BG_COLOR
from app.src.draw import (_create_board, _create_full_colored_field,
                          _create_hash_board, _place_queen_on_board,
                          _read_queen_array, draw_solution)


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


def test_place_queen_on_board_works_properly_case_without_background():
    # GIVEN
    sample_row = 0
    sample_col = 0
    sample_board = np.zeros((6, 6), dtype=np.uint8)
    sample_n_elements = 2
    sample_queen = np.ones((3, 3), dtype=np.uint8)

    # WHEN
    new_board = _place_queen_on_board(
        row=sample_row,
        col=sample_col,
        board=sample_board,
        queen=sample_queen,
        n_elements=sample_n_elements,
    )

    # THEN
    # "1" means queen
    assert new_board[0][0] == 1
    assert new_board[0][1] == 1
    assert new_board[0][2] == 1

    assert new_board[1][0] == 1
    assert new_board[1][1] == 1
    assert new_board[1][2] == 1

    assert new_board[2][0] == 1
    assert new_board[2][1] == 1
    assert new_board[2][2] == 1

    # "0" means empty fields
    assert np.all(new_board[3:, :] == 0)
    assert np.all(new_board[:, 3:] == 0)


def test_place_queen_on_board_works_properly_case_with_background():
    # GIVEN
    sample_row = 0
    sample_col = 0
    sample_queen_color = 69
    sample_board = np.zeros((6, 6), dtype=np.uint8)
    sample_n_elements = 2
    sample_queen = np.ones((3, 3), dtype=np.uint8) * BG_COLOR
    sample_queen[1][1] = sample_queen_color

    # WHEN
    new_board = _place_queen_on_board(
        row=sample_row,
        col=sample_col,
        board=sample_board,
        queen=sample_queen,
        n_elements=sample_n_elements,
    )

    # THEN
    # "1" means queen
    assert new_board[0][0] == 0
    assert new_board[0][1] == 0
    assert new_board[0][2] == 0

    assert new_board[1][0] == 0
    assert new_board[1][1] == sample_queen_color
    assert new_board[1][2] == 0

    assert new_board[2][0] == 0
    assert new_board[2][1] == 0
    assert new_board[2][2] == 0

    # "0" means empty fields
    assert np.all(new_board[3:, :] == 0)
    assert np.all(new_board[:, 3:] == 0)


def test_draw_solution_works_properly():
    # GIVEN
    sample_solution = [0, 1, 2, 3, 4, 5, 6, 7]
    sample_folder = "app/src/temp/"
    sample_path = sample_folder + "sample_solution.png"
    expected_n_files = 1

    # WHEN
    os.mkdir(sample_folder)  # just for convenince
    draw_solution(solution=sample_solution, path=sample_path)
    files = glob.glob(sample_folder + "*")
    n_files = len(files)

    # THEN
    assert n_files == expected_n_files
    assert files[0] == sample_path

    # CLEANING
    os.remove(sample_path)
    os.rmdir(sample_folder)
