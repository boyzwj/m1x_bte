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

    def __init__(self, parent=None, node_name="",guid: str = None,params = {}) -> None:
        super(QNode, self).__init__(parent)
        self.name = node_name
        self.__width = 110
        self.__height = 50
        self.__head_range = 10
        self.child_GUIDS = []
        self.parent_GUID = ""
        self.data =  g.config.data['nodes'][self.name]["params"]
        self.params = {}
        self.state = 0
        for k,tp in self.data.items():
            saved_value = params.get(k)
            if saved_value is None:
                if tp == "int":
                    saved_value = 0
                elif tp == "float":
                    saved_value = 0
                elif tp == "string":
                    saved_value = ""
            self.params[k] = saved_value
        if self.name == "Root":
            self.GUID = "0"
        elif guid is not None:
            self.GUID = guid
        else:
            self.GUID = str(uuid.uuid4())
        cfg_data = g.config.data['nodes'].get(self.name)
        if cfg_data is None:
            self.node_type = "Action"
        else:
            self.node_type = cfg_data["type"]
        self.pixmap = QPixmap(f"assets/{self.node_type}.svg")
        if self.node_type in ["Composite", "Decorator", "Condition", "Action"]:
            self.head_position = QPointF(-self.__width / 2 + self.__head_range, 0)
        else:
            self.head_position = None

        if self.node_type in ["Root", "Decorator", "Composite"]:
            self.tail_position = QPointF(self.__width / 2 - self.__head_range, 0)
        else:
            self.tail_position = None

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

    # def itemChange(self, change, value):
    #     print(change)
    #     return value

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
        fm = QFontMetrics(painter.font())
        tw = fm.horizontalAdvance(self.name)
        painter.drawText(-tw / 2, 0, self.name)

    def draw_bg(self, painter):
        self.draw_head(painter)
        self.draw_tail(painter)
        self.do_fill_bg(painter)

    def do_fill_bg(self, painter):
        if self.isSelected():
            painter.setPen(QPen(Qt.black, 1.5, Qt.DotLine))
            painter.drawRect(self.boundingRect())
        painter.drawPixmap(QPointF(-self.__width / 2, -self.__height / 2), self.pixmap)
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
        if len(self.params.keys()) > 0:
            dialog = NodeDialog(self)
            dialog.exec()

    def set_state(self, state):
        self.state = state
        self.update()
        
        
        
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
