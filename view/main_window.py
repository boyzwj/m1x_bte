from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass
