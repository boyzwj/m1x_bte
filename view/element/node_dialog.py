from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uic.ui_node_edit import *
from core import g


class NodeDialog(QDialog):
    def __init__(self, node):
        super(NodeDialog, self).__init__()
        self.node = node
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Tool)
        self.update_table()

    def accept(self) -> None:
        cfg_data = g.config.data['nodes'][self.node.name]["params"]
        table_widget = self.ui.tableWidget
        count = table_widget.rowCount()
        i = 0
        self.node.params.clear()
        while i < count:
            param_name = table_widget.item(i, 0).text()
            param_value = table_widget.cellWidget(i, 4).text()
            current_value = cfg_data[param_name]["default_value"]
            if param_value != current_value:
                self.node.params[param_name] = param_value
            i += 1

        g.need_save = True
        return super().accept()

    def reject(self) -> None:
        return super().reject()

    def update_table(self):
        cfg_data = g.config.data['nodes'][self.node.name]
        table_widget = self.ui.tableWidget
        table_widget.clear()
        table_widget.setColumnCount(5)
        table_widget.setRowCount(len(cfg_data["params"].keys()))
        table_widget.setHorizontalHeaderLabels(
            ["Param Name", "Param Type", "Param Des",  "DefaultValue", "CurrentValue"])
        table_widget.setColumnWidth(0, 150)
        table_widget.setColumnWidth(2, 250)

        i = 0
        for k, v in cfg_data["params"].items():
            item_index = 0
            item_name = QTableWidgetItem(k)
            item_name.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            table_widget.setItem(i, item_index, item_name)

            item_index = 1
            item_type_cb = QTableWidgetItem(v.get("type"))
            item_type_cb.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            table_widget.setItem(i, item_index, item_type_cb)

            item_index = 2
            item_des = QTableWidgetItem(v.get("des"))
            item_des.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            table_widget.setItem(i, item_index, item_des)

            item_index = 3
            item_default_value = QTableWidgetItem(v.get("default_value"))
            item_default_value.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            table_widget.setItem(i, item_index, item_default_value)

            item_index = 4
            item_current_value = QLineEdit()
            current_value = self.node.params.get(k)
            current_value = current_value if current_value is not None else v.get('default_value')
            item_current_value.setText(str(current_value))
            table_widget.setCellWidget(i, item_index, item_current_value)

            i = i + 1
