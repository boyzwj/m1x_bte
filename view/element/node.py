from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6


class Node(QGraphicsRectItem):
    def __init__(self, parent=None) -> None:
        super(Node, self).__init__(parent)
        self.setBrush(QBrush(QColor(0, 160, 230)))
        self.setRect(0, 0, 100, 100)
        self.startPos = None
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                     QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    # def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
    #     print("fuck off")
    #     return super().mouseDoubleClickEvent(event)

    # def mousePressEvent(self, event: PySide6.QtWidgets.QGraphicsSceneMouseEvent) -> None:

    #     if event.button() == Qt.MouseButton.MiddleButton:
    #         print("xxxxxxxxxxxx")
    #         self.startPos = event.pos()

    #     return super().mousePressEvent(event)

    # def mouseMoveEvent(self, event):
    #     if self.startPos is not None and event.button() == Qt.MouseButton.RightButton:
    #         delta = self.startPos - event.pos()
    #         self.pos += delta

    # def mouseReleaseEvent(self, event):
    #     self.startPos = None
    #     super(Node, self).mouseReleaseEvent(event)
