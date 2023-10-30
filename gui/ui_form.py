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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextBrowser,
    QVBoxLayout, QWidget)

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
        self.label_title = QLabel(Widget)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox_3 = QSpinBox(Widget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        font1 = QFont()
        font1.setFamilies([u"Roboto Light"])
        font1.setPointSize(12)
        self.spinBox_3.setFont(font1)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10000)
        self.spinBox_3.setValue(15)

        self.gridLayout_3.addWidget(self.spinBox_3, 2, 2, 1, 1)

        self.label_lr = QLabel(Widget)
        self.label_lr.setObjectName(u"label_lr")
        self.label_lr.setFont(font1)

        self.gridLayout_3.addWidget(self.label_lr, 1, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(Widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(0.050000000000000)
        self.doubleSpinBox.setSingleStep(0.050000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox, 1, 2, 1, 1)

        self.label_device = QLabel(Widget)
        self.label_device.setObjectName(u"label_device")
        self.label_device.setFont(font1)
        self.label_device.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.label_device, 3, 1, 1, 1)

        self.comboBox_device = QComboBox(Widget)
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.setObjectName(u"comboBox_device")

        self.gridLayout_3.addWidget(self.comboBox_device, 3, 2, 1, 1)

        self.label_batch = QLabel(Widget)
        self.label_batch.setObjectName(u"label_batch")
        self.label_batch.setFont(font1)

        self.gridLayout_3.addWidget(self.label_batch, 2, 1, 1, 1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font1)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(15)

        self.gridLayout_3.addWidget(self.spinBox, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_details = QPushButton(Widget)
        self.pushButton_details.setObjectName(u"pushButton_details")
        self.pushButton_details.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_details)

        self.textBrowser_details = QTextBrowser(Widget)
        self.textBrowser_details.setObjectName(u"textBrowser_details")
        self.textBrowser_details.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(True)
        self.textBrowser_details.setFont(font2)

        self.verticalLayout.addWidget(self.textBrowser_details)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_images = QPushButton(Widget)
        self.pushButton_images.setObjectName(u"pushButton_images")
        self.pushButton_images.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_images)

        self.verticalSpacer_3 = QSpacerItem(98, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.pushButton_done = QPushButton(Widget)
        self.pushButton_done.setObjectName(u"pushButton_done")
        font3 = QFont()
        font3.setFamilies([u"Roboto Light"])
        font3.setPointSize(16)
        self.pushButton_done.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_done, 2, 4, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_weights = QLineEdit(Widget)
        self.lineEdit_weights.setObjectName(u"lineEdit_weights")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_weights.sizePolicy().hasHeightForWidth())
        self.lineEdit_weights.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.lineEdit_weights, 4, 2, 1, 1)

        self.pushButton_selectFolder = QPushButton(Widget)
        self.pushButton_selectFolder.setObjectName(u"pushButton_selectFolder")
        self.pushButton_selectFolder.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_selectFolder, 0, 1, 1, 1)

        self.pushButton_store = QPushButton(Widget)
        self.pushButton_store.setObjectName(u"pushButton_store")
        self.pushButton_store.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_store, 5, 1, 1, 1)

        self.comboBox_model = QComboBox(Widget)
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem(u"resnet50")
        self.comboBox_model.addItem(u"mobilenet_v3_large")
        self.comboBox_model.addItem(u"vgg16")
        self.comboBox_model.addItem(u"vgg19")
        self.comboBox_model.setObjectName(u"comboBox_model")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_model.sizePolicy().hasHeightForWidth())
        self.comboBox_model.setSizePolicy(sizePolicy2)
        self.comboBox_model.setFont(font1)

        self.gridLayout_2.addWidget(self.comboBox_model, 1, 2, 1, 1)

        self.checkBox_pretrained = QCheckBox(Widget)
        self.checkBox_pretrained.setObjectName(u"checkBox_pretrained")
        self.checkBox_pretrained.setFont(font1)
        self.checkBox_pretrained.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_pretrained, 2, 2, 1, 1)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_model = QLabel(Widget)
        self.label_model.setObjectName(u"label_model")
        self.label_model.setFont(font1)
        self.label_model.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_model, 1, 1, 1, 1)

        self.pushButton_weights = QPushButton(Widget)
        self.pushButton_weights.setObjectName(u"pushButton_weights")
        self.pushButton_weights.setFont(font1)

        self.gridLayout_2.addWidget(self.pushButton_weights, 4, 1, 1, 1)

        self.lineEdit_store = QLineEdit(Widget)
        self.lineEdit_store.setObjectName(u"lineEdit_store")

        self.gridLayout_2.addWidget(self.lineEdit_store, 5, 2, 1, 1)

        self.comboBox_optimizer = QComboBox(Widget)
        self.comboBox_optimizer.addItem("")
        self.comboBox_optimizer.addItem("")
        self.comboBox_optimizer.addItem("")
        self.comboBox_optimizer.setObjectName(u"comboBox_optimizer")
        self.comboBox_optimizer.setFont(font1)

        self.gridLayout_2.addWidget(self.comboBox_optimizer, 7, 2, 1, 1)

        self.lineEdit_path = QLineEdit(Widget)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_path.setSizePolicy(sizePolicy3)
        self.lineEdit_path.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit_path, 0, 2, 1, 1)

        self.label_optimizer = QLabel(Widget)
        self.label_optimizer.setObjectName(u"label_optimizer")
        self.label_optimizer.setFont(font1)
        self.label_optimizer.setTextFormat(Qt.PlainText)

        self.gridLayout_2.addWidget(self.label_optimizer, 7, 1, 1, 1)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 3, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(5, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_title.setText(QCoreApplication.translate("Widget", u"No Code ML", None))
        self.label_lr.setText(QCoreApplication.translate("Widget", u"Learning Rate", None))
        self.label_device.setText(QCoreApplication.translate("Widget", u"Device", None))
        self.comboBox_device.setItemText(0, QCoreApplication.translate("Widget", u"...", None))
        self.comboBox_device.setItemText(1, QCoreApplication.translate("Widget", u"CPU", None))
        self.comboBox_device.setItemText(2, QCoreApplication.translate("Widget", u"GPU", None))

        self.label_batch.setText(QCoreApplication.translate("Widget", u"Batch Size", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Number of Epochs", None))
        self.pushButton_details.setText(QCoreApplication.translate("Widget", u"Display Details", None))
        self.pushButton_images.setText(QCoreApplication.translate("Widget", u"Display Image Samples", None))
        self.pushButton_done.setText(QCoreApplication.translate("Widget", u"Train", None))
        self.pushButton_selectFolder.setText(QCoreApplication.translate("Widget", u"Select Folder", None))
        self.pushButton_store.setText(QCoreApplication.translate("Widget", u"Store Weights ", None))
        self.comboBox_model.setItemText(0, QCoreApplication.translate("Widget", u"...", None))

        self.checkBox_pretrained.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"Default Weights", None))
        self.label_model.setText(QCoreApplication.translate("Widget", u"Model:", None))
        self.pushButton_weights.setText(QCoreApplication.translate("Widget", u"Load Weights", None))
        self.comboBox_optimizer.setItemText(0, QCoreApplication.translate("Widget", u"...", None))
        self.comboBox_optimizer.setItemText(1, QCoreApplication.translate("Widget", u"Adam", None))
        self.comboBox_optimizer.setItemText(2, QCoreApplication.translate("Widget", u"SDG", None))

#if QT_CONFIG(whatsthis)
        self.lineEdit_path.setWhatsThis(QCoreApplication.translate("Widget", u"Select folder containing images. Expected Format:", None))
#endif // QT_CONFIG(whatsthis)
        self.label_optimizer.setText(QCoreApplication.translate("Widget", u"Optimizer", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Custom", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u" Weights", None))
    # retranslateUi

