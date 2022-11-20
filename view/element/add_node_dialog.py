from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uic.ui_node_add import *
from core import g
import json


class AddNodeDialog(QDialog):
    def __init__(self):
        super(AddNodeDialog, self).__init__()
        self.ui = Ui_AddNodeDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(self.width(), self.height())
        self.params = {}
        self.initUI()

    def initUI(self):
        self.ui.cbNodeType.addItems(["Action","Condition"])
        self.ui.cbParamType.addItems(["int","float","string"])
        self.ui.btnAdd.clicked.connect(self.add_param)
        
        
        
    def add_param(self,event):
        param_name = self.ui.iptParamName.text().strip()
        param_type = self.ui.cbParamType.currentText()
        if param_name == "":
            box = QMessageBox()
            box.critical(self,"Error","Empty Param Name !")
        else:
            # TODO 加入参数
            pass
            
            
        
    
        
        