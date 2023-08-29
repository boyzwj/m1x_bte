# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'node_add.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QDialogButtonBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AddNodeDialog(object):
    def setupUi(self, AddNodeDialog):
        if not AddNodeDialog.objectName():
            AddNodeDialog.setObjectName(u"AddNodeDialog")
        AddNodeDialog.resize(633, 405)
        self.verticalLayout_2 = QVBoxLayout(AddNodeDialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(AddNodeDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 150))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 60, 71, 16))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.delButton = QPushButton(self.widget)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setGeometry(QRect(460, 10, 75, 24))
        self.iptNodeDes = QLineEdit(self.widget)
        self.iptNodeDes.setObjectName(u"iptNodeDes")
        self.iptNodeDes.setGeometry(QRect(310, 60, 113, 21))
        self.iptParamDes = QLineEdit(self.widget)
        self.iptParamDes.setObjectName(u"iptParamDes")
        self.iptParamDes.setGeometry(QRect(400, 110, 113, 21))
        self.iptParamDefaultValue = QLineEdit(self.widget)
        self.iptParamDefaultValue.setObjectName(u"iptParamDefaultValue")
        self.iptParamDefaultValue.setGeometry(QRect(320, 110, 71, 21))
        self.cbParamType = QComboBox(self.widget)
        self.cbParamType.setObjectName(u"cbParamType")
        self.cbParamType.setGeometry(QRect(220, 110, 81, 22))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 60, 91, 20))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.iptParamName = QLineEdit(self.widget)
        self.iptParamName.setObjectName(u"iptParamName")
        self.iptParamName.setGeometry(QRect(100, 110, 113, 21))
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(540, 10, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.iptNodeName = QLineEdit(self.widget)
        self.iptNodeName.setObjectName(u"iptNodeName")
        self.iptNodeName.setGeometry(QRect(100, 60, 113, 21))
        self.iptNodeName.setAutoFillBackground(True)
        self.iptNodeName.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.iptNodeName.setInputMethodHints(Qt.ImhNone)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 20))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnAdd = QPushButton(self.widget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(520, 110, 75, 24))
        self.cbNodeType = QComboBox(self.widget)
        self.cbNodeType.setObjectName(u"cbNodeType")
        self.cbNodeType.setGeometry(QRect(110, 10, 111, 21))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 71, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(AddNodeDialog)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.widget.raise_()

        self.retranslateUi(AddNodeDialog)
        self.buttonBox.accepted.connect(AddNodeDialog.accept)
        self.buttonBox.rejected.connect(AddNodeDialog.reject)

        QMetaObject.connectSlotsByName(AddNodeDialog)
    # setupUi

    def retranslateUi(self, AddNodeDialog):
        AddNodeDialog.setWindowTitle(QCoreApplication.translate("AddNodeDialog", u"Add Node", None))
        self.label_4.setText(QCoreApplication.translate("AddNodeDialog", u"Node Des", None))
        self.delButton.setText(QCoreApplication.translate("AddNodeDialog", u"\u5220\u9664", None))
        self.label_2.setText(QCoreApplication.translate("AddNodeDialog", u"Node Name", None))
        self.label.setText(QCoreApplication.translate("AddNodeDialog", u"Node Type", None))
        self.btnAdd.setText(QCoreApplication.translate("AddNodeDialog", u"Add", None))
        self.label_3.setText(QCoreApplication.translate("AddNodeDialog", u"Params", None))
    # retranslateUi

