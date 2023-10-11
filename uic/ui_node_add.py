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
        AddNodeDialog.resize(800, 500)
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
        self.label_4.setGeometry(QRect(210, 20, 71, 16))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.delButton = QPushButton(self.widget)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setGeometry(QRect(450, 20, 81, 31))
        self.iptNodeDes = QLineEdit(self.widget)
        self.iptNodeDes.setObjectName(u"iptNodeDes")
        self.iptNodeDes.setGeometry(QRect(290, 20, 151, 21))
        self.iptParamDes = QLineEdit(self.widget)
        self.iptParamDes.setObjectName(u"iptParamDes")
        self.iptParamDes.setGeometry(QRect(280, 100, 161, 21))
        self.iptParamDefaultValue = QLineEdit(self.widget)
        self.iptParamDefaultValue.setObjectName(u"iptParamDefaultValue")
        self.iptParamDefaultValue.setGeometry(QRect(540, 100, 71, 21))
        self.cbParamType = QComboBox(self.widget)
        self.cbParamType.setObjectName(u"cbParamType")
        self.cbParamType.setGeometry(QRect(190, 100, 51, 22))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 50, 91, 20))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.iptParamName = QLineEdit(self.widget)
        self.iptParamName.setObjectName(u"iptParamName")
        self.iptParamName.setGeometry(QRect(50, 100, 91, 21))
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(710, 10, 81, 81))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.iptNodeName = QLineEdit(self.widget)
        self.iptNodeName.setObjectName(u"iptNodeName")
        self.iptNodeName.setGeometry(QRect(100, 50, 113, 21))
        self.iptNodeName.setAutoFillBackground(True)
        self.iptNodeName.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.iptNodeName.setInputMethodHints(Qt.ImhNone)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 81, 20))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btnAdd = QPushButton(self.widget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(630, 100, 75, 24))
        self.cbNodeType = QComboBox(self.widget)
        self.cbNodeType.setObjectName(u"cbNodeType")
        self.cbNodeType.setGeometry(QRect(100, 20, 111, 21))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 100, 41, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 100, 31, 21))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 100, 31, 21))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 100, 81, 21))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 80, 81, 20))
        self.label_8.setTextFormat(Qt.RichText)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 81, 16))
        self.label_9.setTextFormat(Qt.RichText)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 130, 81, 20))
        self.label_10.setTextFormat(Qt.RichText)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(AddNodeDialog)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(AddNodeDialog)
        self.buttonBox.accepted.connect(AddNodeDialog.accept)
        self.buttonBox.rejected.connect(AddNodeDialog.reject)

        QMetaObject.connectSlotsByName(AddNodeDialog)
    # setupUi

    def retranslateUi(self, AddNodeDialog):
        AddNodeDialog.setWindowTitle(QCoreApplication.translate("AddNodeDialog", u"Add Node", None))
        self.label_4.setText(QCoreApplication.translate("AddNodeDialog", u"Node Des", None))
        self.delButton.setText(QCoreApplication.translate("AddNodeDialog", u"\u5220\u9664\u8be5\u8282\u70b9", None))
        self.label_2.setText(QCoreApplication.translate("AddNodeDialog", u"Node Name", None))
        self.label.setText(QCoreApplication.translate("AddNodeDialog", u"Node Type", None))
        self.btnAdd.setText(QCoreApplication.translate("AddNodeDialog", u"Add", None))
        self.label_3.setText(QCoreApplication.translate("AddNodeDialog", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("AddNodeDialog", u"Type", None))
        self.label_6.setText(QCoreApplication.translate("AddNodeDialog", u"Des", None))
        self.label_7.setText(QCoreApplication.translate("AddNodeDialog", u"DefaultValue", None))
        self.label_8.setText(QCoreApplication.translate("AddNodeDialog", u"<span style=\" font-size:10pt; font-weight:600; color:#000000;\">\u53c2\u6570\u7f16\u8f91</span>", None))
        self.label_9.setText(QCoreApplication.translate("AddNodeDialog", u"<span style=\" font-size:10pt; font-weight:600; color:#000000;\">\u8282\u70b9\u7f16\u8f91</span>", None))
        self.label_10.setText(QCoreApplication.translate("AddNodeDialog", u"<span style=\" font-size:10pt; font-weight:600; color:#000000;\">\u53c2\u6570\u5217\u8868</span>", None))
    # retranslateUi

