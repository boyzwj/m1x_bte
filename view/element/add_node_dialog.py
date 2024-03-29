from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uic.ui_node_add import *
from core import g
from enum import Enum
import json


class NodeDialogMode(Enum):
    ADD = 1
    EDIT = 2


NodeParamType = ["int", "float", "string", "float_range"]


class AddNodeDialog(QDialog):
    def __init__(self, node_name=""):
        super(AddNodeDialog, self).__init__()
        self.ui = Ui_AddNodeDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Tool)
        # self.setFixedSize(self.width(), self.height())
        self.node_name = node_name
        self.initUI()

    def initUI(self):
        data = g.config.data['nodes'].get(self.node_name)
        g.test_widget = self
        if data is not None and data:
            self.mode = NodeDialogMode.EDIT
            self.params = data.get('params', {})
            self.node_type = data.get('type')
            self.node_des = data.get('des', "")
            self.setWindowTitle("Edit Node")
            if data['type'] in ['Action', 'Condition']:
                self.ui.delButton.clicked.connect(self.do_delete)
            else:
                self.ui.delButton.hide()
        else:
            self.mode = NodeDialogMode.ADD
            self.ui.delButton.hide()
            self.params = {}
            self.node_type = "Action"
            self.node_des = ""

        self.ui.tableWidget.currentCellChanged.connect(self.on_item_selection_changed)
        self.ui.iptNodeName.setText(self.node_name)
        self.ui.iptNodeDes.setText(self.node_des)
        self.ui.cbNodeType.addItems(["Action", "Condition"])
        self.ui.cbNodeType.setCurrentText(self.node_type)
        self.ui.cbNodeType.installEventFilter(self)
        self.ui.cbParamType.addItems(NodeParamType)
        self.ui.cbParamType.installEventFilter(self)
        self.ui.iptNodeName.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.iptParamName.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.iptParamName.textEdited.connect(self.on_edit_param_name)
        self.ui.btnAdd.clicked.connect(self.add_param)
        self.update_table()
        self.update_param_editor(True)

    def on_edit_param_name(self):
        self.update_param_editor(True)

    def on_item_selection_changed(self):
        self.update_param_editor(False)

    def do_delete(self):
        if g.config.data['nodes'][self.node_name]['type'] in ['Action', 'Condition']:
            confirm = QMessageBox.question(
                self,
                'Confirmation',
                'Delete this node?',
                QMessageBox.StandardButton.Yes |
                QMessageBox.StandardButton.No
            )
            if confirm == QMessageBox.StandardButton.Yes:
                del g.config.data['nodes'][self.node_name]
                g.config.save()
                self.update_param_editor(True)
                return super().accept()

    def delete_param_item(self, event):
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Warning', 'Please select a record to delete')
        k = self.ui.tableWidget.cellWidget(current_row, 0).text()
        button = QMessageBox.question(
            self,
            'Confirmation',
            f'Are you sure that you want to delete the selected: {k} row?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if button == QMessageBox.StandardButton.Yes:
            self.ui.tableWidget.removeRow(current_row)
            del self.params[k]
            return

    def update_param_editor(self, only_update_btn):
        if not only_update_btn:
            current_row = self.ui.tableWidget.currentRow()
            param = None
            if current_row >= 0:
                current_row_item = self.ui.tableWidget.cellWidget(current_row, 0)
                if current_row_item is not None:
                    k = current_row_item.text()
                    param = self.params.get(k)

            if param is None:
                self.ui.iptParamName.setText('')
                self.ui.cbParamType.setCurrentText('')
                self.ui.iptParamDefaultValue.setText('')
                self.ui.iptParamDes.setText('')
            else:
                self.ui.iptParamName.setText(k)
                self.ui.cbParamType.setCurrentText(param.get('type'))
                self.ui.iptParamDefaultValue.setText(param.get('default_value'))
                self.ui.iptParamDes.setText(param.get('des'))

        param_name = self.ui.iptParamName.text()
        if self.params.get(param_name) is None:
            self.ui.btnAdd.setText("add")
        else:
            self.ui.btnAdd.setText("update")

    #禁用ComboBox的滚轮事件
    def eventFilter(self, target, triggered_event) -> bool:
        if triggered_event.type() == QEvent.Type.Wheel:
            return True
        return QMainWindow.eventFilter(self, target, triggered_event)

    def update_table(self):
        temp = self.ui.tableWidget.verticalScrollBar().sliderPosition()
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setRowCount(len(self.params.keys()))
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["Param Name", "Param Type", "Param Des", "DefaultValue", "Remove"])
        self.ui.tableWidget.setColumnWidth(0, 150)
        self.ui.tableWidget.setColumnWidth(2, 250)
        i = 0
        for k, v in self.params.items():
            item_index = 0
            item_name = QLineEdit()
            item_name.setText(k)
            item_name.editingFinished.connect(lambda temp_param_name=k: self.modify_param_name(temp_param_name))
            self.ui.tableWidget.setCellWidget(i, item_index, item_name)

            item_index = 1
            item_type_cb = QComboBox()
            item_type_cb.addItems(NodeParamType)
            item_type_cb.currentIndexChanged.connect(self.modify_param_type)
            item_type_cb.setCurrentText(v.get('type'))
            item_type_cb.installEventFilter(self)
            self.ui.tableWidget.setCellWidget(i, item_index, item_type_cb)

            item_index = 2
            item_des = QLineEdit()
            item_des.setText(v.get('des'))
            item_des.editingFinished.connect(self.modify_param_des)
            self.ui.tableWidget.setCellWidget(i, item_index, item_des)

            item_index = 3
            item_default_value = QLineEdit()
            item_default_value.setText(v.get('default_value'))
            item_default_value.editingFinished.connect(self.modify_param_default_value)
            self.ui.tableWidget.setCellWidget(i, item_index, item_default_value)

            item_index = 4
            del_btn = QPushButton("Delete")
            del_btn.clicked.connect(self.delete_param_item)
            self.ui.tableWidget.setCellWidget(i, item_index, del_btn)

            i = i + 1
        self.ui.tableWidget.verticalScrollBar().setSliderPosition(temp)

    def add_param(self, event):
        param_name = self.ui.iptParamName.text().strip()
        param_type = self.ui.cbParamType.currentText()
        param_des = self.ui.iptParamDes.toPlainText().strip()
        param_default_value = self.ui.iptParamDefaultValue.text().strip()
        if param_name == "":
            box = QMessageBox()
            box.critical(self, "Error", "Empty Param Name !")
        else:
            self.params[param_name] = {'type': param_type, "default_value": param_default_value, 'des': param_des}
            self.update_table()
            self.update_param_editor(True)

    def accept(self) -> None:
        if self.mode == NodeDialogMode.ADD:
            self.do_add_node()
        else:
            self.do_update_node()
        return super().accept()

    def do_add_node(self):
        node_name = self.ui.iptNodeName.text().strip()
        node_desc = self.ui.iptNodeDes.toPlainText().strip()
        node_type = self.ui.cbNodeType.currentText().strip()

        if node_name == "":
            box = QMessageBox()
            box.critical(self, "Error", "Empty Node Name !")
            return
        if node_name in g.config.data['node_type'].keys():
            box = QMessageBox()
            box.critical(self, "Error", "Node Name can not same to the node type !")
            return
        if g.config.data['nodes'].get(node_name) is not None:
            box = QMessageBox()
            box.critical(self, "Error", "Existed Node Name !")
            return

        data = {"type": node_type, "params": self.params, "des": node_desc}
        g.config.data['nodes'][node_name] = data
        g.config.save()

    def do_update_node(self):
        node_name = self.ui.iptNodeName.text().strip()
        node_desc = self.ui.iptNodeDes.toPlainText().strip()
        node_type = self.ui.cbNodeType.currentText().strip()

        if node_name == "":
            box = QMessageBox()
            box.critical(self, "Error", "Empty Node Name !")
            return
        data = {"type": node_type, "params": self.params, "des": node_desc}
        del g.config.data['nodes'][self.node_name]
        g.config.data['nodes'][node_name] = data
        g.config.save()

    def reject(self) -> None:
        return super().reject()

    def modify_param_type(self, index):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            k = self.ui.tableWidget.cellWidget(current_row, 0).text()
            self.modify_param_field(k, 'type', NodeParamType[index])

    def modify_param_name(self, old_name):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            new_name = self.ui.tableWidget.cellWidget(current_row, 0).text().strip()
            if old_name == new_name:
                return
            if new_name == "":
                box = QMessageBox()
                box.critical(self, "Error", "Empty Param Name !")
                self.update_table()
                self.update_param_editor(True)
                return
            if self.params.get(new_name) is not None:
                box = QMessageBox()
                box.critical(self, "Error", "Param name has existed!")
                self.update_table()
                self.update_param_editor(True)
                return
            self.params[new_name] = self.params[old_name]
            del self.params[old_name]
            self.update_table()
            self.update_param_editor(True)
            self.do_update_node()

    def modify_param_default_value(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            k = self.ui.tableWidget.cellWidget(current_row, 0).text()
            v = self.ui.tableWidget.cellWidget(current_row, 3).text().strip()
            self.modify_param_field(k, 'default_value', v)

    def modify_param_des(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row >= 0:
            k = self.ui.tableWidget.cellWidget(current_row, 0).text()
            v = self.ui.tableWidget.cellWidget(current_row, 2).text().strip()
            self.modify_param_field(k, 'des', v)

    def modify_param_field(self, param_name, field_key, field_value):
        if self.params[param_name].get(field_key) == field_value:
            return
        self.params[param_name][field_key] = field_value
        self.update_table()
        self.update_param_editor(True)
        self.do_update_node()
