from PySide6.QtWidgets import QDialog, QGridLayout, QPushButton


class EvalPopUp(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.font = QFont()
        self.font.setFamilies(["Roboto Light"])
        self.font.setPointSize(12)

    def setUpPopUp(self):
        self.pushButton_image = QPushButton(self)
        self.pushButton_image.setObjectName("pushButton_image")
        self.pushButton_image.setFont(self.font)
        self.QGridLayout.addWidget(self.pushButton_image, 0, 0, 1, 1)
