# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myguiUNYWZR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 485)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(195, 176, 145, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: None;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.spinBox_5 = QSpinBox(self.centralwidget)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setStyleSheet(u"background-color: None;")
        self.spinBox_5.setMinimum(2)
        self.spinBox_5.setMaximum(105)

        self.horizontalLayout_2.addWidget(self.spinBox_5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: None;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_6 = QSpinBox(self.centralwidget)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setStyleSheet(u"background-color: None;")
        self.spinBox_6.setMinimum(2)
        self.spinBox_6.setMaximum(105)
        self.spinBox_6.setValue(3)

        self.horizontalLayout_2.addWidget(self.spinBox_6)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: None;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spinBox_7 = QSpinBox(self.centralwidget)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setStyleSheet(u"background-color: None;")
        self.spinBox_7.setMinimum(2)
        self.spinBox_7.setMaximum(105)
        self.spinBox_7.setValue(4)

        self.horizontalLayout_2.addWidget(self.spinBox_7)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bb_btn = QPushButton(self.centralwidget)
        self.bb_btn.setObjectName(u"bb_btn")
        self.bb_btn.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.bb_btn)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.ir232_btn = QPushButton(self.centralwidget)
        self.ir232_btn.setObjectName(u"ir232_btn")
        self.ir232_btn.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.ir232_btn)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.ir485_btn = QPushButton(self.centralwidget)
        self.ir485_btn.setObjectName(u"ir485_btn")
        self.ir485_btn.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.ir485_btn)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"background-color: None;")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"background-color: None;")
        self.spinBox.setMinimum(280)

        self.horizontalLayout_6.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setStyleSheet(u"background-color: None;")
        self.spinBox_2.setMinimum(345)
        self.spinBox_2.setMaximum(350)

        self.horizontalLayout_6.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setStyleSheet(u"background-color: None;")
        self.spinBox_3.setMinimum(5)
        self.spinBox_3.setMaximum(20)

        self.horizontalLayout_6.addWidget(self.spinBox_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"background-color: None;")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.csv_check = QCheckBox(self.groupBox_2)
        self.csv_check.setObjectName(u"csv_check")
        self.csv_check.setLayoutDirection(Qt.LeftToRight)
        self.csv_check.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_4.addWidget(self.csv_check)

        self.wc_noti_check = QCheckBox(self.groupBox_2)
        self.wc_noti_check.setObjectName(u"wc_noti_check")
        self.wc_noti_check.setStyleSheet(u"background-color: None;")

        self.horizontalLayout_4.addWidget(self.wc_noti_check)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: None;")
        self.label_10.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_6.addWidget(self.label_10)

        self.spinBox_4 = QSpinBox(self.groupBox_2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setStyleSheet(u"background-color: None;")
        self.spinBox_4.setMinimum(30)
        self.spinBox_4.setMaximum(300)
        self.spinBox_4.setSingleStep(10)

        self.verticalLayout_6.addWidget(self.spinBox_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(150, 20))
        self.label_11.setStyleSheet(u"background-color: None;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(150, 25))
        self.textEdit.setStyleSheet(u"background-color: None;")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.calib_btn = QPushButton(self.centralwidget)
        self.calib_btn.setObjectName(u"calib_btn")
        self.calib_btn.setStyleSheet(u"background-color: None;")

        self.verticalLayout_2.addWidget(self.calib_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"background-color: None;")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_9.addWidget(self.progressBar)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(800, 200))

        self.verticalLayout_9.addWidget(self.label_12)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Auto IR Calibrator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Black Box COM", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IR 232 COM", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IR 485 COM", None))
        self.bb_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_4.setText("")
        self.ir232_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_5.setText("")
        self.ir485_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_6.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Temperature Range", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.csv_check.setText(QCoreApplication.translate("MainWindow", u"CSV output", None))
        self.wc_noti_check.setText(QCoreApplication.translate("MainWindow", u"Workchat notification", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cool Down Temperature", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.calib_btn.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_12.setText("")
    # retranslateUi

