from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6
import weakref
import uuid

class QNode(QGraphicsItem):
    def __init__(self, parent=None, node_name =  "") -> None:
        super(QNode, self).__init__(parent)
        self.name = "Action"
        self.__width = 100
        self.__height = 40
        if node_name != "Root":
            self.GUID = str(uuid.uuid4())
        else:
            self.GUID = "0"

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                     QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    def itemChange(self, change, value):
        print(change, value)
        return value
    def boundingRect(self) -> QRectF:
        rect = QRectF(0, 0, self.__width, self.__height)
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        bg_rect = self.boundingRect()
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawRect(bg_rect)
        if self.isSelected():
            painter.fillRect(bg_rect, QColor(0, 120, 230))
        else:
            painter.fillRect(bg_rect, QColor(0, 180, 180))
        painter.drawText(50, 15, self.name)


    # def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
    #     if event.button() == Qt.MouseButton.RightButton:
    #         print("xxxxxxxxxxxx")
    #         self.startPos = event.pos()
    #
    #     return super().mousePressEvent(event)
    #
    # def mouseMoveEvent(self, event):
    #     if self.startPos is not None:
    #         delta = self.startPos - event.pos()
    #         print(delta)
    #
    # def mouseReleaseEvent(self, event):
    #     self.startPos = None
    #     print("end mouse")
    #     super(Node, self).mouseReleaseEvent(event)
