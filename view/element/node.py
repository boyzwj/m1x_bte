from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6
import weakref
import uuid


class QNode(QGraphicsItem):
    GUID = ""
    folded = False
    child_nodes = []
    parent_node = ""
    params = {}

    def __init__(self, parent = None, node_name =  "") -> None:
        super(QNode, self).__init__(parent)
        self.name = "Action"
        self.__width = 110
        self.__height = 40
        self.__head_range = 10
        self.head_position = QPointF(-self.__width/2 + self.__head_range, 0)
        self.tail_position = QPointF(self.__width/2 - self.__head_range, 0)
        self.child_GUIDS = []
        self.parent_GUID = ""
        self.params = {}
        if node_name != "Root":
            self.GUID = str(uuid.uuid4())
        else:
            self.GUID = "0"

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                     QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def add_child(self, child):
        if child.GUID not in self.child_GUIDS and child.GUID != self.GUID:
            self.child_GUIDS.append(child.GUID)
            child.parent_GUID = self.GUID

    def remove_child(self, t_guid: str):
        for child_GUID in self.child_GUIDS:
            if child_GUID == t_guid:
                self.child_GUIDS.remove(child_GUID)
                break

    def link_start_pos(self) -> QPointF:
        return self.scenePos() + self.tail_position

    def link_end_pos(self) -> QPointF:
        return self.scenePos() + self.head_position

    def itemChange(self, change, value):
        return value

    def boundingRect(self) -> QRectF:
        x1 = -self.__width/2
        y1 = -self.__height/2
        rect = QRectF(x1, y1, self.__width, self.__height)
        return rect

    def bg_rect(self) -> QRectF:
        width = self.__width - 2 * self.__head_range
        x1 = -width/2
        y1 = -self.__height/2
        rect = QRectF(x1, y1, width, self.__height)
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        self.draw_bg(painter)
        self.draw_text(painter)

    def draw_text(self, painter):
        fm = QFontMetrics(painter.font())
        tw = fm.horizontalAdvance(self.name)
        painter.drawText(-tw/2, 0, self.name)

    def draw_bg(self, painter):
        self.draw_head(painter)
        self.draw_tail(painter)
        bg_rect = self.bg_rect()
        painter.drawRect(bg_rect)
        if self.isSelected():
            painter.fillRect(bg_rect, QColor(0, 120, 230))
        else:
            painter.fillRect(bg_rect, QColor(0, 180, 180))

    def draw_head(self, painter: QPainter):
        painter.drawEllipse(self.head_position, self.__head_range, self.__head_range)

    def draw_tail(self, painter: QPainter):
        painter.drawEllipse(self.tail_position, self.__head_range, self.__head_range)

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
