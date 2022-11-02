from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding,
                                QSizePolicy.Expanding)

        self.infoLabel = QLabel(
            "<i>Choose a menu option, or right-click to invoke a context menu</i>",
            alignment=QtCore.Qt.AlignCenter)
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Shadow.Sunken)

        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.addWidget(topFiller)
        vbox.addWidget(self.infoLabel)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

        self.createActions()
        self.createMenus()

        self.setMinimumSize(480, 320)
        self.resize(1920, 1000)

    def contextMenuEvent(self, event):
        menu = QtGui.QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())

    def newFile(self):
        self.infoLabel.setText("Invoked <b>File|New</b>")

    def createActions(self):
        self.newAct = QtGui.QAction("&New", self, shortcut=QtGui.QKeySequence.New,
                                    statusTip="Create a new file", triggered=self.newFile)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
