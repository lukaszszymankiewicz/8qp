import glob
import os
from typing import List

from .file_paths import all_solutions_path, base_solutions_path


def get_all_files_in_path(path: str) -> List[str]:
    """
    Find paths of all files in given path.

    Args:
        path: folder in which function will look into.

    Returns:
        List of path of all files in given directory.
    """
    return glob.glob(path + "*")


def delete_all_images() -> None:
    """
    Function for cleaning files from once generated soultions. Each request to main page should
    generate puzzle results from the scratch.
    """
    for file in get_all_files_in_path(all_solutions_path):
        os.remove(file)

    for file in get_all_files_in_path(base_solutions_path):
        os.remove(file)
