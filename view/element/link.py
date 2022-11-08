from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6
import weakref
import uuid
from view.element.node import *

class QLink(QGraphicsItem):
    def __init__(self, start_node: QNode = None, end_node: QNode = None):
        QGraphicsItem.__init__(self)
        self.start_node = start_node
        self.end_node = end_node
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        self.__width = 100
        self.__height = 100


    def boundingRect(self) -> QRectF:
        rect = QRectF(0, 0, self.__width, self.__height)
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing, True)
        pen = QPen(Qt.black, 1)
        painter.setPen(pen)
        painter.drawLine(self.start_node.pos(), self.end_node.pos())


