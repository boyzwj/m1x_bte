from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uic.ui_node_edit import *
from core import g
import json



class  NodeDialog(QDialog):
    def __init__(self,node):
        super(NodeDialog, self).__init__()
        self.node = node
        self.forms = {}
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(self.width(), self.height())
        self.initUI(node)
        
    def initUI(self,node):
        for name, tp in node.data.items():
            if tp == "int":
                ipt = QLineEdit(self)
                intValidator = QIntValidator(self)
                ipt.setValidator(intValidator)
                if name in self.node.params.keys():
                    ipt.setText(str(self.node.params[name]))
                else:
                    self.node.params[name] = 0
                    ipt.setText("0")
            elif tp == "float":
                ipt = QLineEdit(self)
                floatValidator = QDoubleValidator(self)
                ipt.setValidator(floatValidator)
                if name in self.node.params.keys():
                    ipt.setText(str(self.node.params[name]))
                else:
                    self.node.params[name] = 0
                    ipt.setText("0")
            elif tp == "string":
                ipt = QLineEdit(self)
                if name in self.node.params.keys():
                    ipt.setText(self.node.params[name])
                else:
                    self.node.params[name] = ""
                    ipt.setText("")
            self.forms[name] = ipt
            self.ui.formLayout.addRow(name,ipt)
    
    def accept(self) -> None:
        for k,ipt in self.forms.items():
            if self.node.data[k] == "int":
                self.node.params[k] = int(ipt.text())
            elif self.node.data[k] == "float":
                self.node.params[k] = float(ipt.text())
            else:
                self.node.params[k] = ipt.text()
        g.need_save = True
        return super().accept()
    
    def reject(self) -> None:
        return super().reject()
        
            