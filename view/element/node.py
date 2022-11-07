from PySide6.QtGui import QColor
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6


class Node(QGraphicsRectItem):
    def __init__(self, parent=None) -> None:
        super(Node, self).__init__(parent)
        self.brush: QBrush = QBrush()
        self.brush.setColor(QColor(0, 160, 230))
        self.setBrush(self.brush)
        self.setRect(0, 0, 125, 50)
        self.startPos = None
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                     QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    # def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
    #     print("fuck off")
    #     return super().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.button() == Qt.MouseButton.RightButton:
            print("xxxxxxxxxxxx")
            self.startPos = event.pos()

        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            delta = self.startPos - event.pos()
            print(delta)

    def mouseReleaseEvent(self, event):
        self.startPos = None
        print("end mouse")
        super(Node, self).mouseReleaseEvent(event)
