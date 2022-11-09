from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6
import weakref
import uuid
from view.element.node import *


class QLink(QGraphicsItem):
    def __init__(self, parent=None):
        super(QLink, self).__init__(parent)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, False)
        # self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges, False)
        # self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        self.__width = 100
        self.__height = 100
        self.start_position: QPointF = self.scenePos()
        self.end_position: QPointF = self.scenePos()

    def boundingRect(self) -> QRectF:
        rect = QRectF(0, 0, self.__width, self.__height)
        return rect

    def set_end_position(self, position: QPointF):
        self.end_position = position
        self.update()

    def set_start_position(self, position: QPointF):
        self.start_position = position

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.start_position is not None and self.end_position is not None:
            print("fucking")
            painter.save()
            painter.setRenderHint(QPainter.Antialiasing, True)

            pen = QPen()
            pen.setWidth(5)
            pen.setColor(Qt.red)
            painter.setPen(pen)
            print(self.start_position)
            print(self.end_position)
            painter.drawLine(self.start_position, self.end_position)
            painter.restore()

