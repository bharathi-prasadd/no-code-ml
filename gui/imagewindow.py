from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QApplication,
    QMainWindow,
    QPushButton,
    QSizePolicy,
)

from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import os
from typing import Generator, Union


class ImageWindow(QDialog):
    """
    Base class for image popups

    Attributes:
        max_cols (int) : Maximum number of images per row (default is 3) - set to 2*max_cols + 1 to account for spacers
        row (int) : current row
        col (int) : current column
        layout    : Grid layout that forms the base for the popup
    Methods:
        _add_to_layout(label,QLabel) : Adds an image to the layout according to popups specification
        disp_image(class_name,file_path) : Load in the image at file_path and display it
        setup_layout() : add layout and execute the popup
        setup_font(obj,font_size) : setup font with font_size for the object
    """

    def __init__(self, max_cols: int = 3):
        super().__init__()
        self.layout = QGridLayout()
        self.row: int = 0
        self.col: int = 0
        self.max_cols = 2 * max_cols + 1

    def _add_to_layout(self, label: QLabel, text: QLabel) -> None:
        pass

    def setup_ui(self) -> None:
        self.setLayout(self.layout)
        self.exec()

    def disp_image(self, class_name: str, file_path: str) -> None:
        """
        Loads in the image at file_path and a corresponding text label and adds it to the layout
        Raises FileNotFoundError if image is missing

        Args:
            class_name : Name of the class the image belongs to -> Used to create text label
            file_path :  path to the file
        """
        img = QLabel()
        if os.path.isfile(file_path):
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(256, 256)
            img.setPixmap(pixmap)
            img.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        else:
            raise FileNotFoundError
        text = QLabel()
        text.setAlignment(Qt.AlignCenter)
        text.setText(class_name)
        self.setup_font(text, 18)
        self._add_to_layout(img, text)

    def setup_font(self, obj, size: int = 12) -> None:
        font = QFont()
        font.setFamilies(["Roboto Light"])
        font.setPointSize(size)
        obj.setFont(font)


class ImageSample(ImageWindow):
    def __init__(self, max_cols: int = 3):
        super().__init__(max_cols)

    def _add_to_layout(self, img: QLabel, text: QLabel) -> None:
        """
        Adds img and text according to the following specification

        1. Add image and text to  a QVBoxLayout
        2. Add Vbox to the grid layout
        2. Add spacer to the grid layout
        Args:
            img : QLabel with the pixmap to be added
            text : Class name of the image to be added
        """
        vbox = QVBoxLayout()
        vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        vbox.addWidget(img)
        vbox.addWidget(text)
        vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        if self.col == 0:
            self.layout.addItem(
                QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum),
                self.row,
                self.col,
            )
            self.col += 1
        self.layout.addLayout(vbox, self.row, self.col)
        self.col += 1
        self.layout.addItem(
            QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum),
            self.row,
            self.col,
        )
        self.col += 1
        self.col %= self.max_cols
        if self.col == 0:
            self.row += 1
