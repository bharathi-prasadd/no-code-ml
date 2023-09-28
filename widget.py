# This Python file uses the following encoding: utf-8

import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Slot

from ui_form import Ui_Widget
import util


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_selectFolder.clicked.connect(self.get_dir)
        self.ui.pushButton_details.clicked.connect(self.details)

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
            util.details(self.ui.lineEdit_Path.text(), self.ui.textBrowser_details)
        except FileNotFoundError:
            # If no directory is selected, show a message to the user
            QMessageBox.critical(
                self,
                "Error",
                "Choose the directory first",
                QMessageBox.Ok,
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
