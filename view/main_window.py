from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from view.element.node import *
from view.element.tmp_link import *
from view.element.node_tree import *
from view.element.add_node_dialog import *
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
        self.ui.action_open.triggered.connect(self.action_open)
        self.ui.action_save.triggered.connect(self.action_save)
        self.ui.action_attach.triggered.connect(self.action_attach)
        self.ui.action_add_node.triggered.connect(self.action_add_node)
        
    
    @Slot()
    def action_open(self):
        dialog = QFileDialog()
        last_path = g.config.data['last_project']
        filename,_ext = dialog.getOpenFileName(self,"Open file",last_path,"json(*.json)")
        if filename == "":
            return
        self.graphicsView.load_file(file_name = filename)
    
    @Slot()
    def action_save(self):
        if self.graphicsView.file_name is None:
            dialog = QFileDialog()
            last_path = g.config.data['last_project']
            filename,_ext = dialog.getSaveFileName(self, "Save file",last_path,"json(*.json)")
            if filename == "":
                return
            self.graphicsView.save_file(file_name = filename)
        else:
            self.graphicsView.save_file()

    @Slot()
    def action_add_node(self):
        dialog = AddNodeDialog()
        dialog.exec_()
        self.node_tree.update_tree()
        
    def action_attach(self):
        print("do action attach")