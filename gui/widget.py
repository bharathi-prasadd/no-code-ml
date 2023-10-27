import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, QFile
from imagewindow import ImageSample

from ui_form import Ui_Widget
import util


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_selectFolder.clicked.connect(self.get_dir)
        self.ui.pushButton_details.clicked.connect(self.details)
        self.ui.pushButton_images.clicked.connect(self.display)
        self.ui.lineEdit_path.setReadOnly(True)
        self.ui.lineEdit_weights.setReadOnly(True)
        self.ui.pushButton_weights.clicked.connect(self.get_weights)
        self.ui.comboBox_device.currentIndexChanged.connect(self.check_cuda)

    @Slot()
    def get_weights(self):
        options = QFileDialog.ReadOnly
        weight_path, _ = QFileDialog.getOpenFileName(
            self, "Select Weights", "", options=options
        )
        if weight_path:
            self.ui.lineEdit_weights.setText(weight_path)

    @Slot()
    def get_dir(self):
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "Select Data Folder",
            "",
            options=QFileDialog.Option.ShowDirsOnly
            | QFileDialog.Option.DontResolveSymlinks,
        )
        if dir_path:
            self.ui.lineEdit_path.setText(dir_path)

    @Slot()
    def details(self):
        try:
            self.ui.textBrowser_details.clear()
            util.details(self.ui.lineEdit_path.text(), self.ui.textBrowser_details)
        except FileNotFoundError:
            # If no directory is selected, show a message to the user
            QMessageBox.critical(
                self,
                "Error",
                "Choose proper directory",
                QMessageBox.Ok,
            )

    @Slot()
    def display(self):
        try:
            imgsample = ImageSample()
            path: str = self.ui.lineEdit_path.text()
            dirs: list[str] = os.listdir(path)
            for dir in dirs:
                with os.scandir(os.path.join(path, dir)) as enteries:
                    for entry in enteries:
                        imgsample.disp_image(dir, entry.path)
                        break
            imgsample.setup_ui()
        except FileNotFoundError:
            util.file_error()
            QMessageBox.critical(
                self,
                "Error",
                "Choose proper directory",
                QMessageBox.Ok,
            )

    @Slot()
    def check_cuda(self):
        if self.ui.comboBox_device.currentText() == "GPU":
            if not util.check_cuda():
                self.ui.comboBox_device.setCurrentText("CPU")
                QMessageBox.critical(
                    self,
                    "Error",
                    "GPU not available,Defaulting to CPU",
                    QMessageBox.Ok,
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # with open("MaterialDark.qss", "r") as f:
    #     stylesheet = f.read()
    #     print("Loaded QSS file:", stylesheet)
    #     app.setStyleSheet(stylesheet)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
