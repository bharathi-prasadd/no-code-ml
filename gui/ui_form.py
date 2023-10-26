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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1352, 767)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_details = QPushButton(Widget)
        self.pushButton_details.setObjectName(u"pushButton_details")
        font = QFont()
        font.setFamilies([u"Roboto Light"])
        font.setPointSize(12)
        self.pushButton_details.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_details)

        self.textBrowser_details = QTextBrowser(Widget)
        self.textBrowser_details.setObjectName(u"textBrowser_details")
        self.textBrowser_details.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        self.textBrowser_details.setFont(font1)

        self.verticalLayout.addWidget(self.textBrowser_details)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_images = QPushButton(Widget)
        self.pushButton_images.setObjectName(u"pushButton_images")
        self.pushButton_images.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_images)

        self.verticalSpacer_3 = QSpacerItem(98, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 5, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_model = QComboBox(Widget)
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem(u"resnet50")
        self.comboBox_model.addItem(u"mobilenet_v3_large")
        self.comboBox_model.addItem(u"vgg16")
        self.comboBox_model.addItem(u"vgg19")
        self.comboBox_model.setObjectName(u"comboBox_model")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_model.sizePolicy().hasHeightForWidth())
        self.comboBox_model.setSizePolicy(sizePolicy1)
        self.comboBox_model.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox_model, 1, 2, 1, 1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)

        self.lineEdit_path = QLineEdit(Widget)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_path.setSizePolicy(sizePolicy2)
        self.lineEdit_path.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_path, 0, 2, 1, 1)

        self.label_model = QLabel(Widget)
        self.label_model.setObjectName(u"label_model")
        self.label_model.setFont(font)

        self.gridLayout_2.addWidget(self.label_model, 1, 1, 1, 1)

        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(15)

        self.gridLayout_2.addWidget(self.spinBox, 3, 2, 1, 1)

        self.comboBox_optimizer = QComboBox(Widget)
        self.comboBox_optimizer.addItem("")
        self.comboBox_optimizer.addItem("")
        self.comboBox_optimizer.addItem("")
        self.comboBox_optimizer.setObjectName(u"comboBox_optimizer")
        self.comboBox_optimizer.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox_optimizer, 2, 2, 1, 1)

        self.label_optimizer = QLabel(Widget)
        self.label_optimizer.setObjectName(u"label_optimizer")
        self.label_optimizer.setFont(font)
        self.label_optimizer.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.label_optimizer, 2, 1, 1, 1)

        self.pushButton_selectFolder = QPushButton(Widget)
        self.pushButton_selectFolder.setObjectName(u"pushButton_selectFolder")
        self.pushButton_selectFolder.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_selectFolder, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_weights = QLineEdit(Widget)
        self.lineEdit_weights.setObjectName(u"lineEdit_weights")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_weights.sizePolicy().hasHeightForWidth())
        self.lineEdit_weights.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.lineEdit_weights, 3, 2, 1, 1)

        self.label_device = QLabel(Widget)
        self.label_device.setObjectName(u"label_device")
        self.label_device.setFont(font)
        self.label_device.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.label_device, 2, 1, 1, 1)

        self.label_batch = QLabel(Widget)
        self.label_batch.setObjectName(u"label_batch")
        self.label_batch.setFont(font)

        self.gridLayout_3.addWidget(self.label_batch, 1, 1, 1, 1)

        self.pushButton_weights = QPushButton(Widget)
        self.pushButton_weights.setObjectName(u"pushButton_weights")
        self.pushButton_weights.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_weights, 3, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(Widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(0.050000000000000)
        self.doubleSpinBox.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox, 0, 2, 1, 1)

        self.comboBox_device = QComboBox(Widget)
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.setObjectName(u"comboBox_device")

        self.gridLayout_3.addWidget(self.comboBox_device, 2, 2, 1, 1)

        self.spinBox_3 = QSpinBox(Widget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10000)
        self.spinBox_3.setValue(15)

        self.gridLayout_3.addWidget(self.spinBox_3, 1, 2, 1, 1)

        self.label_lr = QLabel(Widget)
        self.label_lr.setObjectName(u"label_lr")
        self.label_lr.setFont(font)

        self.gridLayout_3.addWidget(self.label_lr, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(5, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_details.setText(QCoreApplication.translate("Widget", u"Display Details", None))
        self.pushButton_images.setText(QCoreApplication.translate("Widget", u"Display Image Samples", None))
        self.comboBox_model.setItemText(0, QCoreApplication.translate("Widget", u"...", None))

        self.label.setText(QCoreApplication.translate("Widget", u"Number of Epochs", None))
#if QT_CONFIG(whatsthis)
        self.lineEdit_path.setWhatsThis(QCoreApplication.translate("Widget", u"Select folder containing images. Expected Format:", None))
#endif // QT_CONFIG(whatsthis)
        self.label_model.setText(QCoreApplication.translate("Widget", u"Model:", None))
        self.comboBox_optimizer.setItemText(0, QCoreApplication.translate("Widget", u"...", None))
        self.comboBox_optimizer.setItemText(1, QCoreApplication.translate("Widget", u"Adam", None))
        self.comboBox_optimizer.setItemText(2, QCoreApplication.translate("Widget", u"SDG", None))

        self.label_optimizer.setText(QCoreApplication.translate("Widget", u"Optimizer", None))
        self.pushButton_selectFolder.setText(QCoreApplication.translate("Widget", u"Select Folder", None))
        self.label_device.setText(QCoreApplication.translate("Widget", u"Device", None))
        self.label_batch.setText(QCoreApplication.translate("Widget", u"Batch Size", None))
        self.pushButton_weights.setText(QCoreApplication.translate("Widget", u"Load Weights", None))
        self.comboBox_device.setItemText(0, QCoreApplication.translate("Widget", u"...", None))
        self.comboBox_device.setItemText(1, QCoreApplication.translate("Widget", u"CPU", None))
        self.comboBox_device.setItemText(2, QCoreApplication.translate("Widget", u"GPU", None))

        self.label_lr.setText(QCoreApplication.translate("Widget", u"Learning Rate", None))
    # retranslateUi

