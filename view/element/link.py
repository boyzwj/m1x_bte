from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6
import weakref
import uuid

from view.element.node import QNode


class Link(QGraphicsPathItem):
    def __init__(self, start_node: QNode, end_node: QNode):
        super(Link, self).__init__()
        self.start_node = start_node
        self.end_node = end_node
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(188, 66, 245))
        self.setPen(pen)
        self.up()

    def get_bezier_path(self):
        start_pos = self.start_node.link_start_pos()
        end_pos = self.end_node.link_end_pos()
        path = QPainterPath(start_pos)
        dx = end_pos.x() - start_pos.x()
        dy = end_pos.y() - start_pos.y()
        p1 = QPointF(start_pos.x() + dx/2, start_pos.y())
        p2 = QPointF(start_pos.x() + dx/2, start_pos.y() + dy)
        path.cubicTo(p1, p2, end_pos)
        return path

    def up(self):
        path = self.get_bezier_path()
        self.setPath(path)
        self.update()



