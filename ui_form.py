# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(901, 600)
        Widget.setAutoFillBackground(False)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 19, 771, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_details = QPushButton(self.gridLayoutWidget)
        self.pushButton_details.setObjectName(u"pushButton_details")

        self.verticalLayout.addWidget(self.pushButton_details)

        self.textBrowser_details = QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_details.setObjectName(u"textBrowser_details")

        self.verticalLayout.addWidget(self.textBrowser_details)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_images = QPushButton(self.gridLayoutWidget)
        self.pushButton_images.setObjectName(u"pushButton_images")

        self.verticalLayout.addWidget(self.pushButton_images)

        self.verticalSpacer_3 = QSpacerItem(98, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_selectFolder = QPushButton(self.gridLayoutWidget)
        self.pushButton_selectFolder.setObjectName(u"pushButton_selectFolder")

        self.horizontalLayout.addWidget(self.pushButton_selectFolder)

        self.lineEdit_Path = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Path.setObjectName(u"lineEdit_Path")

        self.horizontalLayout.addWidget(self.lineEdit_Path)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_details.setText(QCoreApplication.translate("Widget", u"Display Details\n"
"", None))
        self.pushButton_images.setText(QCoreApplication.translate("Widget", u"Display Image Samples", None))
        self.pushButton_selectFolder.setText(QCoreApplication.translate("Widget", u"Select Folder", None))
    # retranslateUi

