import os
from typing import Generator
from PySide6.QtWidgets import QTextBrowser, QGridLayout, QLabel
from PySide6.QtGui import QPixmap


def details(base_dir: str, textField: QTextBrowser) -> None:
    """
    Walk through a given directory and append details about
    the number of classes available and the number of images in each class"""

    dirs: list[str] = os.listdir(base_dir)

    textField.append(f"There are {len(dirs)} classses")
    n_files = 0
    try:
        for dirpath, _, filenames in os.walk(base_dir):
            if dirpath == base_dir:
                continue
            n_files += len(filenames)
            textField.append(
                f"Class {os.path.basename(dirpath)} has {len(filenames)} images"
            )
        textField.append(
            f"There are a total of {len(dirs)} classes and {n_files} images"
        )
    except Exception as e:
        raise e


def get_images(base_dir: str) -> Generator[str, None, None]:
    """
    When passed a base directory acts as a generator that gives you
    the first file in each directory"""
    dirs: list[str] = os.listdir(base_dir)

    for dir in dirs:
        with os.scandir(os.path.join(base_dir, dir)) as entries:
            for entry in entries:
                yield entry.name
                break


if __name__ == "__main__":
    for img in get_images("/home/rumi/projects/miniproject/test_imgs"):
        print(img)
