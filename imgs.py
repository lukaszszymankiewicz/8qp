import numpy as np
import png

GREY_COLOR = 50
WHITE_COLOR = 255


def create_hash_board(
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


def create_full_colored_field(COLOR: int, px_size: int):
    return np.ones((px_size, px_size), dtype=np.uint8) * COLOR


def create_board(
    small_hash_px_size: int,
    small_hash_n_elements: int,
    big_hash_px_size: int,
    big_hash_n_elements: int,
    dark_color: int,
    light_color: int,
):
    grey_field = create_full_colored_field(dark_color, small_hash_px_size)
    white_field = create_full_colored_field(light_color, small_hash_px_size)

    big_grey_field = create_hash_board(white_field, grey_field, n_elements=small_hash_n_elements)
    big_white_field = create_full_colored_field(light_color, big_hash_px_size)

    full_board = create_hash_board(big_white_field, big_grey_field, n_elements=big_hash_n_elements)

    return full_board


a = create_board(
    small_hash_px_size=5,
    small_hash_n_elements=20,
    big_hash_px_size=100,
    big_hash_n_elements=8,
    dark_color=GREY_COLOR,
    light_color=WHITE_COLOR,
)
# png.from_array(a, mode="L").save("sample_board.png")
