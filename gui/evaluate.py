from PySide6.QtWidgets import (
    QDialog,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QLabel,
    QSizePolicy,
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Slot, QFile
from QtToTorch import QtToTorch


class EvalPopUp(QDialog):
    def __init__(self, torch: QtToTorch):
        super().__init__()
        self.layout = QGridLayout()
        self.font = QFont()
        self.font.setFamilies(["Roboto Light"])
        self.font.setPointSize(12)
        self.torch: QtToTorch = torch

    def setUpPopUp(self):
        self.pushButton_image = QPushButton(self)
        self.pushButton_image.setFont(self.font)
        self.pushButton_image.setText("Choose image")
        self.pushButton_image.clicked.connect(self.set_image)
        self.layout.addWidget(self.pushButton_image, 0, 0, 1, 1)

        self.lineEdit_path = QLineEdit(self)
        self.lineEdit_path.setReadOnly(True)
        self.lineEdit_path.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(self.lineEdit_path, 0, 1, 1, 1)
        self.setLayout(self.layout)
        self.exec()

    @Slot()
    def set_image(self):
        options = QFileDialog.ReadOnly
        img_path, _ = QFileDialog.getOpenFileName(
            self, "Select Weights", "", options=options
        )

        if img_path:
            self.lineEdit_path.setText(img_path)
            self.img = QLabel(self)
            pixmap = QPixmap(img_path)
            pixmap = pixmap.scaled(256, 256)
            self.img.setPixmap(pixmap)
            self.img.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.layout.addWidget(self.img, 1, 0, 1, 2)
            self.torch.eval()
