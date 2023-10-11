from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import uuid
import PySide6
import weakref
from core import g
from view.element.node_dialog import NodeDialog


class QNode(QGraphicsItem):
    GUID = ""
    folded = False
    child_nodes = []
    parent_node = ""
    params = {}

    def __init__(self, parent=None, node_name="", guid: str = None, params={}) -> None:
        super(QNode, self).__init__(parent)
        self.name = node_name
        self.__height = 50
        self.__head_range = 10
        self.child_GUIDS = []
        self.parent_GUID = ""
        cfg_data = g.config.data['nodes'].get(self.name)
        self.has_config = cfg_data is not None
        self.params = params
        self.state = 0

        if self.name == "Root":
            self.GUID = "0"
        elif guid is not None:
            self.GUID = guid
        else:
            self.GUID = str(uuid.uuid4())

        if not self.has_config:
            self.data = None
            self.node_type = "Action"
        else:
            self.data = cfg_data.get("params")
            # for k, tp in self.data.items():
            #     saved_value = params.get(k)
            #     if saved_value is None:
            #         if tp == "int":
            #             saved_value = "0"
            #         elif tp == "float":
            #             saved_value = "0"
            #         elif tp == "string":
            #             saved_value = ""
            #     self.params[k] = saved_value

            self.node_type = cfg_data["type"]

        if self.node_type == "Root":
            self.__width = 80
        elif self.node_type == "Composite":
            self.__width = 150
        else:
            self.__width = 160

        if self.node_type in ["Composite", "Decorator", "Condition", "Action"]:
            self.head_position = QPointF(-self.__width / 2 + self.__head_range, 0)
        else:
            self.head_position = None

        if self.node_type in ["Root", "Decorator", "Composite"]:
            self.tail_position = QPointF(self.__width / 2 - self.__head_range, 0)
        else:
            self.tail_position = None

        if self.has_config:
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                         QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def add_child(self, child):
        if child.GUID not in self.child_GUIDS and child.GUID != self.GUID:
            self.child_GUIDS.append(child.GUID)
            child.parent_GUID = self.GUID
            g.need_save = True

    def remove_child(self, t_guid: str):
        g.need_save = True
        for child_GUID in self.child_GUIDS:
            if child_GUID == t_guid:
                self.child_GUIDS.remove(child_GUID)
                break

    def link_start_pos(self) -> QPointF:
        return self.scenePos() + QPointF(self.__width / 2, 0)

    def link_end_pos(self) -> QPointF:
        return self.scenePos() + QPointF(-self.__width / 2, 0)

    def boundingRect(self) -> QRectF:
        x1 = -self.__width / 2
        y1 = -self.__height / 2
        rect = QRectF(x1, y1, self.__width, self.__height)
        return rect

    def bg_rect(self) -> QRectF:
        width = self.__width - 2 * self.__head_range
        x1 = -width / 2
        y1 = -self.__height / 2
        rect = QRectF(x1, y1, width, self.__height)
        return rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        self.draw_bg(painter)
        self.draw_text(painter)

    def draw_text(self, painter):
        label = self.name
        if not self.has_config:
            label += "(Error:ReadFailed)"
        fm = QFontMetrics(painter.font())
        tw = fm.horizontalAdvance(label)
        painter.drawText(-tw / 2, 0, label)

    def draw_bg(self, painter):
        self.draw_head(painter)
        self.draw_tail(painter)
        self.do_fill_bg(painter)

    def do_fill_bg(self, painter):
        if self.isSelected():
            painter.setPen(QPen(Qt.black, 1, Qt.DotLine))
            painter.drawRect(self.boundingRect())
        bg_color = None
        if not self.has_config:
            bg_color = QColor(255, 0, 0)
        else:
            if self.node_type == "Root":
                bg_color = QColor(247, 143, 191)
            elif self.node_type == "Composite":
                bg_color = QColor(168, 229, 148)
            elif self.node_type == "Decorator":
                bg_color = QColor(172, 78, 197)
            elif self.node_type == "Condition":
                bg_color = QColor(154, 220, 245)
            elif self.node_type == "Action":
                bg_color = QColor(255, 255, 255)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(bg_color))

        if self.node_type == "Root":
            painter.drawEllipse(QPointF(0, 0), self.__width / 2 - self.__head_range, 25)
        elif self.node_type == "Composite":
            points = QPolygonF([
                QPointF(-self.__width / 2 + self.__head_range, 0),
                QPointF(-self.__width / 4, self.__height / 2),
                QPointF(self.__width / 4, self.__height / 2),
                QPointF(self.__width / 2 - self.__head_range, 0),
                QPointF(self.__width / 4, -self.__height / 2),
                QPointF(-self.__width / 4, -self.__height / 2),
            ])
            painter.drawPolygon(points)
        elif self.node_type == "Decorator":
            points = QPolygonF([
                QPointF(-self.__width / 2 + self.__head_range, 0),
                QPointF(0, self.__height / 2),
                QPointF(self.__width / 2 - self.__head_range, 0),
                QPointF(0, -self.__height / 2),
            ])
            painter.drawPolygon(points)
        elif self.node_type == "Condition":
            points = QPolygonF([
                QPointF(-self.__width / 2 + self.__head_range, 0),
                QPointF(-self.__width / 4, self.__height / 2),
                QPointF(self.__width / 2, self.__height / 2),
                QPointF(self.__width / 2, -self.__height / 2),
                QPointF(-self.__width / 4, -self.__height / 2),
            ])
            painter.drawPolygon(points)
        elif self.node_type == "Action":
            rect = QRectF(-self.__width / 2 + self.__head_range, -self.__height / 2, self.__width - self.__head_range,
                          self.__height)
            painter.drawRoundedRect(rect, 10, 10)
        else:
            rect = QRectF(-self.__width / 2 + self.__head_range, -self.__height / 2, self.__width - self.__head_range,
                          self.__height)
            painter.drawRect(rect)
        pen = QPen()
        color = None
        # ready
        if self.state == 0:
            color = QColor(0, 0, 0)
        if self.state == 1:
            color = QColor(255, 215, 0)
        elif self.state == 2:
            color = QColor(34, 139, 34)
        elif self.state == 3:
            color = QColor(178, 34, 34)
        pen.setColor(color)
        painter.setPen(pen)

    def draw_head(self, painter: QPainter):
        if self.head_position is not None:
            painter.drawEllipse(self.head_position, self.__head_range, self.__head_range)

    def draw_tail(self, painter: QPainter):
        if self.tail_position is not None:
            painter.drawEllipse(self.tail_position, self.__head_range, self.__head_range)

    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if not self.has_config:
            return
        dialog = NodeDialog(self)
        dialog.exec()

    def set_state(self, state):
        self.state = state
        self.update()
