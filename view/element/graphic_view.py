from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from view.element.node import *
from view.element.link import *


class GraphicView(QGraphicsView):
    def __init__(self, parent: QWidget):
        super(GraphicView, self).__init__(parent)
        self.startPos = None
        self.start_link = None
        self.tmp_link = None
        self.setupUi()
    def setupUi(self):
        self.setScene(QGraphicsScene())
        self.tmp_link = QLink()
        self.scene().addItem(self.tmp_link)
    def add_node(self, node: QNode):
        self.scene().addItem(node)

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoom_in_factor = 1.1
        zoom_out_factor = 1 / zoom_in_factor

        # Set Anchors

        # Save the scene pos
        old_pos = self.mapToScene(event.position().toPoint())
        self.centerOn(old_pos)
        # Zoom
        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
        else:
            zoom_factor = zoom_out_factor
        self.scale(zoom_factor, zoom_factor)

        # Get the new position
        new_pos = self.mapToScene(event.position().toPoint())

        # Move scene to old position
        delta = new_pos - old_pos
        self.translate(delta.x(), delta.y())

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            # store the origin point
            self.startPos = event.pos()
        if event.button() == Qt.MouseButton.LeftButton:
            if QApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier:
                super(GraphicView, self).mousePressEvent(event)
                nodes = self.scene().selectedItems()
                if len(nodes) > 0:
                    self.start_link = nodes[0]
                else:
                    self.start_link = None
            else:
                super(GraphicView, self).mousePressEvent(event)
        else:
            super(GraphicView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            # compute the difference between the current cursor position and the
            # previous saved origin point
            delta = self.startPos - event.pos()
            # get the current transformation (which is a matrix that includes the
            # scaling ratios
            transform = self.transform()
            # m11 refers to the horizontal scale, m22 to the vertical scale;
            # divide the delta by their corresponding ratio
            delta_x = delta.x() / transform.m11()
            delta_y = delta.y() / transform.m22()
            # translate the current sceneRect by the delta
            self.setSceneRect(self.sceneRect().translated(delta_x, delta_y))
            # update the new origin point to the current position
            self.startPos = event.pos()
        elif self.start_link is not None and QApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier:
            print("fuck")
        else:
            super(GraphicView, self).mouseMoveEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if len(self.scene().selectedItems()) == 1:
            print("begion link")

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_W:
            print("w")
        elif event.key() == Qt.Key.Key_S:
            print("S")
        elif event.key() == Qt.Key.Key_A:
            print("A")
        elif event.key() == Qt.Key.Key_D:
            print("D")
        return super().keyPressEvent(event)

    def mouseReleaseEvent(self, event):
        self.startPos = None
        super(GraphicView, self).mouseReleaseEvent(event)
