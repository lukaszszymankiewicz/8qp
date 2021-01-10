from typing import List

import numpy as np
import png

from .constants import (BG_COLOR, BLACK_COLOR, DTYPE, FIELD_PX_SIZE,
                        GREY_COLOR, SIZE, WHITE_COLOR)
from .file_paths import queen_path

IMAGE_AS_ARRAY = np.ndarray


def _create_hash_board(
    light_field: np.ndarray,
    dark_field: np.ndarray,
    n_elements: int,
) -> IMAGE_AS_ARRAY:
    """
    Creates image of hashboard (chessboard-alike) combining dark and white squares.

    Args:
        light_field: numpy image representing white field,
        dark_field: numpy image representing dark field,
        n_elements: number of elements in each hash row.

    Returns:
        numpy image with hashboard.

    """
    block_a = np.concatenate([light_field, dark_field], axis=-1)
    block_b = np.concatenate([dark_field, light_field], axis=-1)

    pattern_a = np.tile(block_a, n_elements // 2)
    pattern_b = np.tile(block_b, n_elements // 2)

    full_row = np.concatenate([pattern_a, pattern_b], axis=0)
    field = np.tile(full_row, reps=(n_elements // 2, 1))

    return field


def _create_full_colored_field(color: int, px_size: int) -> IMAGE_AS_ARRAY:
    """
    Creates numpy image containing fully-colored square.

    Args:
        color: numpy uint8 number representig grey-scaled color of a square,
        px_size: square size in pixels.

    Returns:
        Numpy image containing square
    """
    return np.ones((px_size, px_size), dtype=DTYPE) * color


def _create_board(
    field_px_size: int,
    n_fields: int,
    dark_color: int,
    light_color: int,
) -> IMAGE_AS_ARRAY:
    """
    Creates numpy image representig chessboard.

    Args:
        field_px_size: integer number representig size of one single field of chessboard,
        n_fields: integer number representig number of fields in every row and column,
        dark_color: numpy uint8 number representing dark field color,
        light_color: numpy uint8 number representing light field color,

    Returns:
        numpy image representing empty chessboard.
    """
    big_grey_field = _create_full_colored_field(dark_color, field_px_size)
    big_white_field = _create_full_colored_field(light_color, field_px_size)

    full_board = _create_hash_board(big_white_field, big_grey_field, n_elements=n_fields)

    return full_board


def _read_queen_array() -> IMAGE_AS_ARRAY:
    """
    Reads predefined queen image and converts it into numpy array.
    """
    raw_file = png.Reader(filename=queen_path).asDirect()[2]
    return np.vstack(map(DTYPE, raw_file))


def _place_queen_on_board(
    row: int, col: int, board: np.ndarray, queen: np.ndarray
) -> IMAGE_AS_ARRAY:
    """
    Places queen image on board image according to its position on chessboard.

    Args:
        row: y-coordinate of queen on a chessboard,
        col: x-coordinate of queen on a chessboard,
        board: numpy image representig chessboard,
        queen: numpy image representig queen.

    Returns:
        numpy image representig chessboard with queen placed in right place.
    """
    rows = slice(row * FIELD_PX_SIZE, row * FIELD_PX_SIZE + FIELD_PX_SIZE)
    cols = slice(col * FIELD_PX_SIZE, col * FIELD_PX_SIZE + FIELD_PX_SIZE)
    board[rows, cols] = np.where(queen != BG_COLOR, queen, board[rows, cols])

    return board


def draw_solution(solution: List[int], path: str) -> None:
    """
    Converts solution to eight queen problem into its png representation.

    Args:
        solution: List of integers. Each integer represents row in which queen is placed, and
            numbers position on a list represents column of a chessboard.
        path: place where png file will be saved.

    Returns:
        None
    """
    board = _create_board(
        field_px_size=FIELD_PX_SIZE,
        n_fields=SIZE,
        dark_color=GREY_COLOR,
        light_color=WHITE_COLOR,
    )

    queen = _read_queen_array()

    for row, col in enumerate(solution):
        board = _place_queen_on_board(row, col, board, queen)

    # this will give image nice black border around it
    board = np.pad(board, pad_width=3, mode="constant", constant_values=BLACK_COLOR)

    png.from_array(board, mode="L").save(path)
