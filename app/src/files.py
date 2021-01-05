import glob
import os


def get_base_solutions_images():
    return glob.glob("app/static/solutions/base/*")


def get_all_solutions_images():
    return glob.glob("app/static/solutions/all/*")


def delete_all_images() -> None:
    """
    Function for cleaning files from once generated soultions. Each request to main page should
    generate puzzle results from the scratch.
    """
    for file in get_base_solutions_images():
        os.remove(file)

    for file in get_all_solutions_images():
        os.remove(file)
