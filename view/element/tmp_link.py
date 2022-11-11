from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6
import weakref
import uuid
from view.element.node import *


class TmpLink(QGraphicsPathItem):
    def __init__(self, line):
        super(TmpLink, self).__init__()
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges, False)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(188, 66, 245))
        self.setPen(pen)
        self.start_position: QPointF = self.scenePos()
        self.end_position: QPointF = self.scenePos()
        self.set_line(line)

    def set_line(self, line: QLineF):
        self.start_position = line.p1()
        self.end_position = line.p2()
        path = self.get_bezier_path()
        self.setPath(path)
        self.update()

    def get_bezier_path(self):
        path = QPainterPath(self.start_position)
        dx = self.end_position.x() - self.start_position.x()
        dy = self.end_position.y() - self.start_position.y()
        p1 = QPointF(self.start_position.x() + dx/2, self.start_position.y())
        p2 = QPointF(self.start_position.x() + dx/2, self.start_position.y() + dy)
        path.cubicTo(p1, p2, self.end_position)
        return path

    # def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
    #     if self.start_position is not None and self.end_position is not None:
    #         painter.save()
    #         pen = QPen()
    #         pen.setWidth(2)
    #         pen.setColor(QColor(188, 66, 245))
    #         painter.setPen(pen)
    #         path = self.get_bezier_path()
    #         painter.drawPath(path)
    #         painter.restore()

