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
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTimeEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 490)
        MainWindow.setMinimumSize(QSize(500, 490))
        MainWindow.setMaximumSize(QSize(500, 590))
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
"QLabel#blockAppLabel, QLabel#hostLabel, QLabel#setDurLabel, QLabel#setEndLabel {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#hostFileDirectoryLabel {\n"
"    color: gray;\n"
"    font-style: italic;\n"
"\n"
"    background-color: #1d1f29;\n"
"    border-radius: 5px;\n"
"\n"
"\n"
"    padding:5px;\n"
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
"    border: 1"
                        "px solid #36ffffff;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: #09ffffff;\n"
"    border: 1px solid #16ffffff;\n"
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
"    background-color: #ff9d1c;"
                        "\n"
"    border: 1px solid #ffffffff;\n"
"    color: white;\n"
"    image: url(./assets/sample.svg);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border-radius: 16px;\n"
"    border: 1px solid #16ffffff;\n"
"    background-color: #09ffffff;\n"
"}\n"
"\n"
"QGroupBox#checkGroup {\n"
"    background-color: #1d1f29;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainGroup = QGroupBox(self.centralwidget)
        self.mainGroup.setObjectName(u"mainGroup")
        self.mainGroup.setGeometry(QRect(10, 150, 481, 291))
        self.layoutWidget = QWidget(self.mainGroup)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 240, 441, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.startButton = QPushButton(self.layoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.startButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cancelButton = QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.cancelButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.time_select_frame = QFrame(self.mainGroup)
        self.time_select_frame.setObjectName(u"time_select_frame")
        self.time_select_frame.setGeometry(QRect(20, 130, 441, 111))
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
        self.setDurLabel = QLabel(self.LeftTimeFrame)
        self.setDurLabel.setObjectName(u"setDurLabel")
        self.setDurLabel.setGeometry(QRect(20, 0, 201, 31))
        self.durationEdit = QTimeEdit(self.LeftTimeFrame)
        self.durationEdit.setObjectName(u"durationEdit")
        self.durationEdit.setGeometry(QRect(20, 30, 191, 31))

        self.horizontalLayout_2.addWidget(self.LeftTimeFrame)

        self.RightTimeFrame = QFrame(self.layoutWidget1)
        self.RightTimeFrame.setObjectName(u"RightTimeFrame")
        self.RightTimeFrame.setMinimumSize(QSize(216, 69))
        self.RightTimeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RightTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.setEndLabel = QLabel(self.RightTimeFrame)
        self.setEndLabel.setObjectName(u"setEndLabel")
        self.setEndLabel.setGeometry(QRect(10, 0, 191, 31))
        self.endTimeEdit = QTimeEdit(self.RightTimeFrame)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        self.endTimeEdit.setGeometry(QRect(10, 30, 191, 31))

        self.horizontalLayout_2.addWidget(self.RightTimeFrame)

        self.layoutWidget2 = QWidget(self.time_select_frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 70, 441, 22))
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

        self.midLine = QFrame(self.time_select_frame)
        self.midLine.setObjectName(u"midLine")
        self.midLine.setGeometry(QRect(0, 100, 441, 20))
        self.midLine.setAcceptDrops(False)
        self.midLine.setAutoFillBackground(False)
        self.midLine.setFrameShadow(QFrame.Shadow.Plain)
        self.midLine.setLineWidth(0)
        self.midLine.setMidLineWidth(0)
        self.midLine.setFrameShape(QFrame.Shape.HLine)
        self.appSelectFrame = QFrame(self.mainGroup)
        self.appSelectFrame.setObjectName(u"appSelectFrame")
        self.appSelectFrame.setGeometry(QRect(20, 10, 441, 121))
        self.appSelectFrame.setMinimumSize(QSize(0, 0))
        self.appSelectFrame.setMaximumSize(QSize(16777215, 145))
        self.appSelectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.appSelectFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.blockAppLabel = QLabel(self.appSelectFrame)
        self.blockAppLabel.setObjectName(u"blockAppLabel")
        self.blockAppLabel.setGeometry(QRect(10, 0, 161, 16))
        self.checkGroup = QGroupBox(self.appSelectFrame)
        self.checkGroup.setObjectName(u"checkGroup")
        self.checkGroup.setGeometry(QRect(0, 30, 441, 80))
        self.layoutWidget_2 = QWidget(self.checkGroup)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 40, 441, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_20)

        self.bskyCheck = QCheckBox(self.layoutWidget_2)
        self.bskyCheck.setObjectName(u"bskyCheck")

        self.horizontalLayout_5.addWidget(self.bskyCheck)

        self.facebookCheck = QCheckBox(self.layoutWidget_2)
        self.facebookCheck.setObjectName(u"facebookCheck")

        self.horizontalLayout_5.addWidget(self.facebookCheck)

        self.tiktokCheck = QCheckBox(self.layoutWidget_2)
        self.tiktokCheck.setObjectName(u"tiktokCheck")

        self.horizontalLayout_5.addWidget(self.tiktokCheck)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_21)

        self.layoutWidget3 = QWidget(self.checkGroup)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 441, 41))
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

        self.instagramCheck = QCheckBox(self.layoutWidget3)
        self.instagramCheck.setObjectName(u"instagramCheck")

        self.horizontalLayout_3.addWidget(self.instagramCheck)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.progressGroup = QGroupBox(self.centralwidget)
        self.progressGroup.setObjectName(u"progressGroup")
        self.progressGroup.setGeometry(QRect(10, 450, 481, 91))
        self.progressFrame = QFrame(self.progressGroup)
        self.progressFrame.setObjectName(u"progressFrame")
        self.progressFrame.setGeometry(QRect(20, 10, 441, 71))
        self.progressFrame.setMinimumSize(QSize(0, 0))
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

        self.hostGroup = QGroupBox(self.centralwidget)
        self.hostGroup.setObjectName(u"hostGroup")
        self.hostGroup.setGeometry(QRect(10, 80, 481, 61))
        self.hostFrame = QFrame(self.hostGroup)
        self.hostFrame.setObjectName(u"hostFrame")
        self.hostFrame.setGeometry(QRect(20, 10, 441, 41))
        self.hostFrame.setMinimumSize(QSize(0, 0))
        self.hostFrame.setMaximumSize(QSize(16777215, 145))
        self.hostFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.hostFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.hostLabel = QLabel(self.hostFrame)
        self.hostLabel.setObjectName(u"hostLabel")
        self.hostLabel.setGeometry(QRect(10, 10, 171, 21))
        self.folderButton = QPushButton(self.hostFrame)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setGeometry(QRect(410, 10, 21, 21))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.folderButton.setIcon(icon)
        self.horizontalLayoutWidget = QWidget(self.hostFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(172, 0, 231, 41))
        self.hostTextLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.hostTextLayout.setObjectName(u"hostTextLayout")
        self.hostTextLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.hostTextLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hostTextLayout.addItem(self.horizontalSpacer_10)

        self.validPathIcon = QLabel(self.horizontalLayoutWidget)
        self.validPathIcon.setObjectName(u"validPathIcon")
        self.validPathIcon.setMaximumSize(QSize(16, 16))
        self.validPathIcon.setPixmap(QPixmap(u"assets/hosts_confirm.svg"))
        self.validPathIcon.setScaledContents(True)

        self.hostTextLayout.addWidget(self.validPathIcon)

        self.hostFileDirectoryLabel = QLabel(self.horizontalLayoutWidget)
        self.hostFileDirectoryLabel.setObjectName(u"hostFileDirectoryLabel")
        self.hostFileDirectoryLabel.setMaximumSize(QSize(175, 16777215))
        self.hostFileDirectoryLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hostFileDirectoryLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.hostTextLayout.addWidget(self.hostFileDirectoryLabel)

        self.appBlockerLogo = QLabel(self.centralwidget)
        self.appBlockerLogo.setObjectName(u"appBlockerLogo")
        self.appBlockerLogo.setGeometry(QRect(160, 20, 171, 43))
        self.appBlockerLogo.setMinimumSize(QSize(171, 43))
        self.appBlockerLogo.setPixmap(QPixmap(u"assets/logo_long.png"))
        self.appBlockerLogo.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainGroup.setTitle("")
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Begin Blocking", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel Blocking", None))
        self.setDurLabel.setText(QCoreApplication.translate("MainWindow", u"Set Duration (hh:mm)", None))
        self.durationEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
        self.setEndLabel.setText(QCoreApplication.translate("MainWindow", u"Set End Time", None))
        self.endTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm AP", None))
        self.selectedDurationLabel.setText(QCoreApplication.translate("MainWindow", u"Selected for a duration of: 00:00", None))
        self.blockAppLabel.setText(QCoreApplication.translate("MainWindow", u"Choose apps to block:", None))
        self.checkGroup.setTitle("")
        self.bskyCheck.setText(QCoreApplication.translate("MainWindow", u"BlueSky", None))
        self.facebookCheck.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.tiktokCheck.setText(QCoreApplication.translate("MainWindow", u"TikTok", None))
        self.discordCheck.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.twitterCheck.setText(QCoreApplication.translate("MainWindow", u"Twitter", None))
        self.youtubeCheck.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.instagramCheck.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.progressGroup.setTitle("")
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"Blocking Progress: 00:00 remaining", None))
        self.hostGroup.setTitle("")
        self.hostLabel.setText(QCoreApplication.translate("MainWindow", u"Directory of hosts file: ", None))
        self.folderButton.setText("")
        self.validPathIcon.setText("")
        self.hostFileDirectoryLabel.setText(QCoreApplication.translate("MainWindow", u"C:WindowsSystem32driversetchosts", None))
        self.appBlockerLogo.setText("")
    # retranslateUi

