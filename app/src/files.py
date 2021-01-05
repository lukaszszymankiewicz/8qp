import glob
import os


def delete_all_images() -> None:
    """
    Function for cleaning files from once generated soultions. Each request to main page should
    generate puzzle results from the scratch.
    """
    files = glob.glob("app/static/solutions/*")
    for file in files:
        os.remove(file)
