# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 707)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(True)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_attach = QAction(MainWindow)
        self.action_attach.setObjectName(u"action_attach")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1020, 665))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuDebug = QMenu(self.menubar)
        self.menuDebug.setObjectName(u"menuDebug")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menuDebug.addAction(self.action_attach)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"M1x BTE", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"open", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"save", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_attach.setText(QCoreApplication.translate("MainWindow", u"attach", None))
#if QT_CONFIG(shortcut)
        self.action_attach.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDebug.setTitle(QCoreApplication.translate("MainWindow", u"Debug", None))
    # retranslateUi

