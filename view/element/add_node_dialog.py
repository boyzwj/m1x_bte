from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uic.ui_node_add import *
from core import g
import json


class AddNodeDialog(QDialog):
    def __init__(self,node_name=""):
        super(AddNodeDialog, self).__init__()
        self.ui = Ui_AddNodeDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(self.width(), self.height())
        self.node_name = node_name
        self.initUI()

    def initUI(self):
        data = g.config.data['nodes'].get(self.node_name)
        if data is not None and data:
            self.params = data.get('params',{})
            self.node_type = data.get('type')
            self.setWindowTitle("Edit Node")
            if data['type'] in ['Action','Condition']:
                self.ui.delButton.clicked.connect(self.do_delete)
            else:
                self.ui.delButton.hide()
        else:
            self.ui.delButton.hide()
            self.params = {}
            self.node_type = "Action"
        
        self.ui.iptNodeName.setText(self.node_name)
        self.ui.cbNodeType.setCurrentText(self.node_type)
        self.ui.cbNodeType.addItems(["Action","Condition"])
        self.ui.cbParamType.addItems(["int","float","string"])
        self.ui.iptNodeName.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.iptParamName.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.btnAdd.clicked.connect(self.add_param)
        self.update_table()

    
    def do_delete(self):
        if g.config.data['nodes'][self.node_name]['type'] in ['Action','Condition']:
            del g.config.data['nodes'][self.node_name]
            g.config.save()
            return super().accept()            
        
    def delete_item(self,event):
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
             return QMessageBox.warning(self, 'Warning','Please select a record to delete')
        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            k = self.ui.tableWidget.itemAt(current_row,0).text()
            self.ui.tableWidget.removeRow(current_row)
            del self.params[k]
            return super().accept()
            
    def update_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(len(self.params.keys()))
        self.ui.tableWidget.setHorizontalHeaderLabels({"Param Name","Param Type","Remove"})
        i = 0
        for k,v in self.params.items():
            item1 = QTableWidgetItem(k)
            item1.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidget.setItem(i,0,item1)
            item2 = QTableWidgetItem(v)
            item2.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.ui.tableWidget.setItem(i,1,item2)
            delBtn =  QPushButton("Delete")
            delBtn.clicked.connect(self.delete_item)
            self.ui.tableWidget.setCellWidget(i,2,delBtn)
            i = i + 1
            
    def add_param(self,event):
        param_name = self.ui.iptParamName.text().strip()
        param_type = self.ui.cbParamType.currentText()
        if param_name == "":
            box = QMessageBox()
            box.critical(self,"Error","Empty Param Name !")
        else:
            self.params[param_name] = param_type
            self.update_table()
            
            
    def accept(self) -> None:
        node_name = self.ui.iptNodeName.text().strip()
        if node_name == "":
            box = QMessageBox()
            box.critical(self,"Error","Empty Node Name !")
            return
        if node_name in g.config.data['node_type'].keys():
            box = QMessageBox()
            box.critical(self,"Error","Node Name can not same to the node type !")
            return
        if g.config.data['nodes'].get(node_name) is not None:
            box = QMessageBox()
            box.critical(self,"Error","Existed Node Name !")
            return
        node_type = self.ui.cbNodeType.currentText().strip()
        data = {"type": node_type, "params": self.params}
        g.config.data['nodes'][node_name] = data
        g.config.save()
        return super().accept()

    def reject(self) -> None:
        print("reject")
        return super().reject()
    
            
            
        
    
        
        