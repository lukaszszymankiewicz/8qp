import numpy as np
import png

from .constants import BG_COLOR, GREY_COLOR, WHITE_COLOR


def _create_hash_board(
    light_field: np.ndarray,
    dark_field: np.ndarray,
    n_elements: int,
):

    block_a = np.concatenate([light_field, dark_field], axis=-1)
    block_b = np.concatenate([dark_field, light_field], axis=-1)

    pattern_a = np.tile(block_a, n_elements // 2)
    pattern_b = np.tile(block_b, n_elements // 2)

    full_row = np.concatenate([pattern_a, pattern_b], axis=0)
    field = np.tile(full_row, reps=(n_elements // 2, 1))

    return field


def _create_full_colored_field(COLOR: int, px_size: int):
    return np.ones((px_size, px_size), dtype=np.uint8) * COLOR


def _create_board(
    big_hash_px_size: int,
    big_hash_n_elements: int,
    dark_color: int,
    light_color: int,
):
    big_grey_field = _create_full_colored_field(dark_color, big_hash_px_size)
    big_white_field = _create_full_colored_field(light_color, big_hash_px_size)

    full_board = _create_hash_board(big_white_field, big_grey_field, n_elements=big_hash_n_elements)

    return full_board


def _read_queen_array():
    raw_file = png.Reader(filename="queen_sm3.png").asDirect()[2]
    return np.vstack(map(np.uint8, raw_file))


def _place_queen_on_board(row: int, col: int, board: np.ndarray, queen: np.ndarray):
    rows = slice(row * 100, row * 100 + 100)
    cols = slice(col * 100, col * 100 + 100)
    board[rows, cols] = np.where(queen != BG_COLOR, queen, board[rows, cols])
    return board


def draw_combination(combination: list, filename="sample_board.png") -> None:
    board = _create_board(
        big_hash_px_size=100,
        big_hash_n_elements=8,
        dark_color=GREY_COLOR,
        light_color=WHITE_COLOR,
    )

    queen = _read_queen_array()

    for row, col in enumerate(combination):
        board = _place_queen_on_board(row, col, board, queen)

    png.from_array(board, mode="L").save(filename)
