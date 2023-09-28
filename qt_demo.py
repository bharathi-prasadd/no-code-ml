import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot


@Slot()
def say_hello():
    label.setVisible(button.isChecked())


app = QApplication()
button = QPushButton("Click here")
button.setCheckable(True)
button.clicked.connect(say_hello)
button.show()
label = QLabel("Hello there!")
label.show()
app.exec()
