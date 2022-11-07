from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from view.element.node import *
from view.element.graphic_view import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.scene = None
        self.graphicsView = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):

        self.graphicsView = GraphicView(self.ui.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.ui.horizontalLayout.addWidget(self.graphicsView)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        node1 = Node()
        self.scene.addItem(node1)
        node1.setPos(100, 100)

        node2 = Node()
        self.scene.addItem(node2)
        node2.setPos(300, 100)
