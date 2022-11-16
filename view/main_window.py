from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from view.element.node import *
from view.element.tmp_link import *
from view.element.node_tree import *
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
        self.node_tree = NodeTree(self.ui.centralwidget)
        self.ui.horizontalLayout.addWidget(self.node_tree)
        self.graphicsView = GraphicView(self.ui.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.ui.horizontalLayout.addWidget(self.graphicsView)
        node1 = QNode(node_name="Root")
        self.graphicsView.add_node(node1)
        node1.setPos(0, 0)