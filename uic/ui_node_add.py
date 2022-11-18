# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'node_add.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AddNodeDialog(object):
    def setupUi(self, AddNodeDialog):
        if not AddNodeDialog.objectName():
            AddNodeDialog.setObjectName(u"AddNodeDialog")
        AddNodeDialog.resize(522, 392)
        self.buttonBox = QDialogButtonBox(AddNodeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(400, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.cbNodeType = QComboBox(AddNodeDialog)
        self.cbNodeType.setObjectName(u"cbNodeType")
        self.cbNodeType.setGeometry(QRect(130, 30, 111, 21))
        self.label = QLabel(AddNodeDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 91, 20))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(AddNodeDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(22, 70, 91, 20))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.iptNodeName = QLineEdit(AddNodeDialog)
        self.iptNodeName.setObjectName(u"iptNodeName")
        self.iptNodeName.setGeometry(QRect(130, 70, 113, 21))
        self.label_3 = QLabel(AddNodeDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 71, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.iptParamName = QLineEdit(AddNodeDialog)
        self.iptParamName.setObjectName(u"iptParamName")
        self.iptParamName.setGeometry(QRect(130, 110, 113, 21))
        self.cbParamType = QComboBox(AddNodeDialog)
        self.cbParamType.setObjectName(u"cbParamType")
        self.cbParamType.setGeometry(QRect(260, 110, 81, 22))
        self.verticalLayoutWidget = QWidget(AddNodeDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 150, 331, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(AddNodeDialog)
        self.buttonBox.accepted.connect(AddNodeDialog.accept)
        self.buttonBox.rejected.connect(AddNodeDialog.reject)

        QMetaObject.connectSlotsByName(AddNodeDialog)
    # setupUi

    def retranslateUi(self, AddNodeDialog):
        AddNodeDialog.setWindowTitle(QCoreApplication.translate("AddNodeDialog", u"Add Node", None))
        self.label.setText(QCoreApplication.translate("AddNodeDialog", u"Node Type", None))
        self.label_2.setText(QCoreApplication.translate("AddNodeDialog", u"Node Name", None))
        self.label_3.setText(QCoreApplication.translate("AddNodeDialog", u"Params", None))
    # retranslateUi

