from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class GraphicView(QGraphicsView):
    def __init__(self, parent: QWidget):
        super(GraphicView, self).__init__(parent)
        self.startPos = None

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoomInFactor = 1.1
        zoomOutFactor = 1 / zoomInFactor

        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.position().toPoint())
        self.centerOn(oldPos)
        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        # Get the new position
        newPos = self.mapToScene(event.position().toPoint())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            # store the origin point
            self.startPos = event.pos()
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
            deltaX = delta.x() / transform.m11()
            deltaY = delta.y() / transform.m22()
            # translate the current sceneRect by the delta
            self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))
            # update the new origin point to the current position
            self.startPos = event.pos()
        else:
            super(GraphicView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.startPos = None
        super(GraphicView, self).mouseReleaseEvent(event)
