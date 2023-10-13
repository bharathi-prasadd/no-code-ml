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
            self.ui.lineEdit_Path.setText(dir_path)

    @Slot()
    def details(self):
        try:
            self.ui.textBrowser_details.clear()
            util.details(self.ui.lineEdit_Path.text(), self.ui.textBrowser_details)
        except FileNotFoundError:
            # If no directory is selected, show a message to the user
            self.file_error()

    @Slot()
    def display(self):
        try:
            imgsample = ImageSample()
            path: str = self.ui.lineEdit_Path.text()
            dirs: list[str] = os.listdir(path)
            for dir in dirs:
                with os.scandir(os.path.join(path, dir)) as enteries:
                    for entry in enteries:
                        imgsample.disp_image(dir, entry.path)
                        break
            imgsample.setup_ui()
        except FileNotFoundError:
            self.file_error()

    def file_error(self):
        QMessageBox.critical(
            self,
            "Error",
            "Choose proper directory",
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
