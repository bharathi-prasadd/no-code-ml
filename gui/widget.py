import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, QFile
from imagewindow import ImageDisp
from ui_form import Ui_Widget
import util
from QtToTorch import QtToTorch
from torch.utils.data import DataLoader


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.lineEdit_path.setReadOnly(True)
        self.ui.lineEdit_weights.setReadOnly(True)
        self.ui.lineEdit_store.setReadOnly(True)

        self.ui.pushButton_selectFolder.clicked.connect(self.get_dir)
        self.ui.pushButton_details.clicked.connect(self.details)
        self.ui.pushButton_images.clicked.connect(self.display)
        self.ui.pushButton_weights.clicked.connect(self.get_weights)
        self.ui.pushButton_store.clicked.connect(self.store_weights)
        self.ui.comboBox_device.currentIndexChanged.connect(self.check_cuda)
        self.ui.checkBox_pretrained.stateChanged.connect(self.checkbox)
        self.ui.pushButton_train.clicked.connect(self.train)

    @Slot()
    def get_weights(self):
        options = QFileDialog.ReadOnly
        weight_path, _ = QFileDialog.getOpenFileName(
            self, "Select Weights", "", options=options
        )
        if weight_path:
            self.ui.lineEdit_weights.setText(weight_path)
        if self.ui.checkBox_pretrained.isChecked():
            QMessageBox.warning(
                self,
                "Warning",
                "Default weights option is selected, deselecting",
                QMessageBox.Ok,
            )
            self.ui.checkBox_pretrained.setChecked(False)

    @Slot()
    def store_weights(self):
        store_path, _ = QFileDialog.getSaveFileName(
            self, "Select path to store weights"
        )
        if store_path:
            self.ui.lineEdit_store.setText(store_path)

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
            imgsample = ImageDisp()
            path: str = self.ui.lineEdit_path.text()
            dirs: list[str] = os.listdir(path)
            for dir in dirs:
                with os.scandir(os.path.join(path, dir)) as enteries:
                    for entry in enteries:
                        imgsample.disp_image(dir, entry.path)
                        break
            imgsample.setup_ui()
        except FileNotFoundError:
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

    @Slot()
    def checkbox(self):
        if self.ui.checkBox_pretrained.isChecked() and self.ui.lineEdit_weights.text():
            QMessageBox.warning(
                self,
                "Warning",
                "Weight path already provided. Clearing",
                QMessageBox.Ok,
            )
            self.ui.lineEdit_weights.setText("")

    @Slot()
    def train(self):
        model_name: str = self.ui.comboBox_model.currentText()
        pretrained: bool = (
            self.ui.checkBox_pretrained.isChecked() or self.ui.lineEdit_weights.text()
        )
        device: str = self.ui.comboBox_device.currentText()
        optim: str = self.ui.comboBox_optimizer.currentText()

        torch = QtToTorch(model_name, pretrained, device, optimizer=optim)

        lr: float = self.ui.doubleSpinBox_lr.value()
        num_classes: int = len(os.listdir(self.ui.lineEdit_path.text()))
        torch.load_model(lr, num_classes)

        batch_size: int = self.ui.spinBox_batch.value()
        train_split: float = self.ui.doubleSpinBox_train.value()
        train: DataLoader
        test: DataLoader

        train, test = torch.load_data(
            train_split, batch_size, self.ui.lineEdit_path.text()
        )

        num_epochs: int = self.ui.spinBox_epochs.value()
        save_path: str = self.ui.lineEdit_store.text()
        torch.train(train, num_epochs, save_path, num_classes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # with open("MaterialDark.qss", "r") as f:
    #     stylesheet = f.read()
    #     print("Loaded QSS file:", stylesheet)
    #     app.setStyleSheet(stylesheet)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
