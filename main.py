import sys
from PySide6 import QtCore, QtWidgets, QtGui
from view.main_window import MainWindow
from core import g

if __name__ == "__main__":
    g.init()
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
