from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from view.element.item import *
from view.element.graphic_view import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):

        self.graphicsView = GraphicView(self.ui.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.ui.horizontalLayout.addWidget(self.graphicsView)

        item = Item()
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.scene.addItem(item)
        item.setPos(100, 100)
