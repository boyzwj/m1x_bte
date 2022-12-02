from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import uuid
import PySide6
import weakref
from core import g


class NodeTree(QTreeWidget):
    def __init__(self, parent=None):
        super(NodeTree, self).__init__(parent)
        self.node_types = {}
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setup_ui()
    
    def setup_ui(self):
        self.update_tree()
                
    def update_tree(self):
        self.clear()
        head_item = QTreeWidgetItem()
        head_item.setText(0, "Nodes")
        self.setHeaderItem(head_item)
        for node_type in g.config.node_type.keys():
            if node_type != "Root":
                item = QTreeWidgetItem()
                item.setText(0, node_type)
                self.addTopLevelItem(item)
                self.node_types[node_type] =  item
                
        for node_name in g.config.nodes.keys():
            if node_name != "Root":
                node_type_name = g.config.nodes[node_name]["type"]
                parent = self.node_types[node_type_name]
                item = QTreeWidgetItem(parent)
                item.setText(0, node_name)
        
        
