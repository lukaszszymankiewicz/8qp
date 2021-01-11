import glob
import os
from typing import List


def get_all_files_in_path(path: str) -> List[str]:
    """
    Find paths of all files in given path.

    Args:
        path: folder in which function will look into.

    Returns:
        List of path of all files in given directory.
    """
    return glob.glob(path + "*")


def delete_all_files(path: str) -> None:
    """
    Function for cleaning files from once generated soultions. Each request to main page should
    generate puzzle results from the scratch.

    Args:
        path: folder in which function will look into.
    """
    for file in get_all_files_in_path(path):
        os.remove(file)


def create_folder(path: str) -> None:
    try:
        os.mkdir(path)
    except OSError:
        pass


def delete_folder(path: str) -> None:
    try:
        delete_all_files(path)
        os.rmdir(path)
    except OSError:
        pass
