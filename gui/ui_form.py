# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(1287, 666)
        Widget.setAutoFillBackground(False)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 50, 1071, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_details = QPushButton(self.gridLayoutWidget)
        self.pushButton_details.setObjectName("pushButton_details")
        font = QFont()
        font.setFamilies(["Roboto Light"])
        font.setPointSize(12)
        self.pushButton_details.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_details)

        self.textBrowser_details = QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_details.setObjectName("textBrowser_details")
        font1 = QFont()
        font1.setFamilies(["Source Code Pro"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.textBrowser_details.setFont(font1)

        self.verticalLayout.addWidget(self.textBrowser_details)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_images = QPushButton(self.gridLayoutWidget)
        self.pushButton_images.setObjectName("pushButton_images")
        self.pushButton_images.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_images)

        self.verticalSpacer_3 = QSpacerItem(
            98, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout.setStretch(1, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_selectFolder = QPushButton(self.gridLayoutWidget)
        self.pushButton_selectFolder.setObjectName("pushButton_selectFolder")
        self.pushButton_selectFolder.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_selectFolder, 0, 0, 1, 1)

        self.lineEdit_Path = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Path.setObjectName("lineEdit_Path")
        self.lineEdit_Path.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_Path, 0, 1, 1, 1)

        self.label_model = QLabel(self.gridLayoutWidget)
        self.label_model.setObjectName("label_model")
        self.label_model.setFont(font)

        self.gridLayout_2.addWidget(self.label_model, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("resnet50")
        self.comboBox.addItem("mobilenet_v3_large")
        self.comboBox.addItem("vgg16")
        self.comboBox.addItem("vgg19")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName("comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Widget", None))
        self.pushButton_details.setText(
            QCoreApplication.translate("Widget", "Display Details", None)
        )
        self.pushButton_images.setText(
            QCoreApplication.translate("Widget", "Display Image Samples", None)
        )
        self.pushButton_selectFolder.setText(
            QCoreApplication.translate("Widget", "Select Folder", None)
        )
        self.label_model.setText(
            QCoreApplication.translate("Widget", "Select a model:", None)
        )
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", "...", None))

        self.comboBox_2.setItemText(
            0, QCoreApplication.translate("Widget", "...", None)
        )
        self.comboBox_2.setItemText(
            1, QCoreApplication.translate("Widget", "Adam", None)
        )
        self.comboBox_2.setItemText(
            2, QCoreApplication.translate("Widget", "SDG", None)
        )

        self.label.setText(
            QCoreApplication.translate("Widget", "Select Optimizer", None)
        )

    # retranslateUi
