# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'block_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(508, 561)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color:white;\n"
"    font-family: \"Segoe UI\", \"SF Pro Display\", \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #1d1f29;\n"
"}\n"
"QMainWindow::separator {\n"
"    background: yellow;\n"
"    width: 10px; /* when vertical */\n"
"    height: 10px; /* when horizontal */\n"
"}\n"
"\n"
"QLabel#blockAppLabel {\n"
"    color: qlineargradient(x1:0, y1:0, x2:50, y2:50,\n"
"                                stop:0 #ffcc00, stop:1 #ff9d1c);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: #09ffffff;\n"
"    border: 1px solid #16ffffff;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color:gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #18ffffff;\n"
"    border: 1px solid #36ffffff;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: #09ffffff;\n"
"    border: 1px solid #16fffff"
                        "f;\n"
"\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: #b15901;\n"
"    width: 20px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTimeEdit {\n"
"    padding:5px;\n"
"    background-color: #1d1f29;\n"
"\n"
"    border-radius:5px;\n"
"    border: 1px solid #16ffffff;\n"
"}\n"
"\n"
"QTimeEdit QAbstractItemView {\n"
"    color: white;\n"
"    background-color: #1d1f29;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    padding: 5px;\n"
"    color:white;\n"
"    spacing: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 1px solid #16ffffff;\n"
"    color:white;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"\n"
"    border-radius: 5px;\n"
"}\n"
"QCheckBox::indicator::unchecked {\n"
"    background-color: #1d1f29;\n"
"}\n"
"QCheckBox::indicator::checked {\n"
"    background-color: #ff9d1c;\n"
"    border: 1px solid #ffffffff;\n"
"    color: white;\n"
"    image: url(./assets/sample.svg);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border-radius"
                        ": 16px;\n"
"    border: 1px solid #16ffffff;\n"
"    background-color: #09ffffff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 481, 321))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 230, 441, 71))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.startButton = QPushButton(self.layoutWidget)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout.addWidget(self.startButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cancelButton = QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.time_select_frame = QFrame(self.groupBox)
        self.time_select_frame.setObjectName(u"time_select_frame")
        self.time_select_frame.setGeometry(QRect(20, 115, 441, 111))
        self.time_select_frame.setMinimumSize(QSize(441, 101))
        self.time_select_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.time_select_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget1 = QWidget(self.time_select_frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 441, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftTimeFrame = QFrame(self.layoutWidget1)
        self.LeftTimeFrame.setObjectName(u"LeftTimeFrame")
        self.LeftTimeFrame.setMinimumSize(QSize(217, 69))
        self.LeftTimeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LeftTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.LeftTimeFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 201, 31))
        self.durationEdit = QTimeEdit(self.LeftTimeFrame)
        self.durationEdit.setObjectName(u"durationEdit")
        self.durationEdit.setGeometry(QRect(20, 30, 191, 31))

        self.horizontalLayout_2.addWidget(self.LeftTimeFrame)

        self.RightTimeFrame = QFrame(self.layoutWidget1)
        self.RightTimeFrame.setObjectName(u"RightTimeFrame")
        self.RightTimeFrame.setMinimumSize(QSize(216, 69))
        self.RightTimeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RightTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.set_endtime_label = QLabel(self.RightTimeFrame)
        self.set_endtime_label.setObjectName(u"set_endtime_label")
        self.set_endtime_label.setGeometry(QRect(10, 0, 191, 31))
        self.endTimeEdit = QTimeEdit(self.RightTimeFrame)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        self.endTimeEdit.setGeometry(QRect(10, 30, 191, 31))

        self.horizontalLayout_2.addWidget(self.RightTimeFrame)

        self.layoutWidget2 = QWidget(self.time_select_frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 80, 441, 22))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.selectedDurationLabel = QLabel(self.layoutWidget2)
        self.selectedDurationLabel.setObjectName(u"selectedDurationLabel")

        self.horizontalLayout_6.addWidget(self.selectedDurationLabel)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.appSelectFrame = QFrame(self.groupBox)
        self.appSelectFrame.setObjectName(u"appSelectFrame")
        self.appSelectFrame.setGeometry(QRect(20, 15, 441, 91))
        self.appSelectFrame.setMinimumSize(QSize(441, 91))
        self.appSelectFrame.setMaximumSize(QSize(16777215, 91))
        self.appSelectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.appSelectFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.blockAppLabel = QLabel(self.appSelectFrame)
        self.blockAppLabel.setObjectName(u"blockAppLabel")
        self.blockAppLabel.setGeometry(QRect(10, 10, 161, 16))
        self.layoutWidget3 = QWidget(self.appSelectFrame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 40, 441, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.discordCheck = QCheckBox(self.layoutWidget3)
        self.discordCheck.setObjectName(u"discordCheck")

        self.horizontalLayout_3.addWidget(self.discordCheck)

        self.twitterCheck = QCheckBox(self.layoutWidget3)
        self.twitterCheck.setObjectName(u"twitterCheck")

        self.horizontalLayout_3.addWidget(self.twitterCheck)

        self.youtubeCheck = QCheckBox(self.layoutWidget3)
        self.youtubeCheck.setObjectName(u"youtubeCheck")

        self.horizontalLayout_3.addWidget(self.youtubeCheck)

        self.telegramCheck = QCheckBox(self.layoutWidget3)
        self.telegramCheck.setObjectName(u"telegramCheck")

        self.horizontalLayout_3.addWidget(self.telegramCheck)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.progressGroup = QGroupBox(self.centralwidget)
        self.progressGroup.setObjectName(u"progressGroup")
        self.progressGroup.setGeometry(QRect(10, 350, 481, 151))
        self.progressFrame = QFrame(self.progressGroup)
        self.progressFrame.setObjectName(u"progressFrame")
        self.progressFrame.setGeometry(QRect(20, 20, 441, 111))
        self.progressFrame.setMinimumSize(QSize(441, 111))
        self.progressFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.progressFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.progressLabel = QLabel(self.progressFrame)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setMinimumSize(QSize(184, 20))

        self.horizontalLayout_4.addWidget(self.progressLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.progressFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(100)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 508, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Begin Blocking", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel Blocking", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Set Duration (hh:mm)", None))
        self.durationEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.set_endtime_label.setText(QCoreApplication.translate("MainWindow", u"Set End Time", None))
        self.endTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm AP", None))
        self.selectedDurationLabel.setText(QCoreApplication.translate("MainWindow", u"Blocking for a duration of: 00:00", None))
        self.blockAppLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Apps to Block", None))
        self.discordCheck.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.twitterCheck.setText(QCoreApplication.translate("MainWindow", u"Twitter", None))
        self.youtubeCheck.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.telegramCheck.setText(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.progressGroup.setTitle("")
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"Blocking Progress: 00:00 remaining", None))
    # retranslateUi

