from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uic.ui_node_edit import *
import json



class  NodeDialog(QDialog):
    def __init__(self,node):
        super(NodeDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(self.width(), self.height())
        self.initUI(node)
        
    def initUI(self,node):
        pass
    
    def accept(self) -> None:
        return super().accept()
    
    def reject(self) -> None:
        return super().reject()
        
            