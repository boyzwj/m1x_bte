from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import *
from PySide6.QtGui import *


class Item(QGraphicsRectItem):
    def __init__(self, parent=None) -> None:
        super(Item, self).__init__(parent)
        self.setBrush(QBrush(QColor(0, 160, 230)))
        self.setRect(0, 0, 100, 100)
        