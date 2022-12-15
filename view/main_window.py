from uic.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtNetwork import *
from view.element.node import *
from view.element.tmp_link import *
from view.element.node_tree import *
from view.element.add_node_dialog import *
from view.element.graphic_view import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.scene = None
        self.graphicsView = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.sideWidget = QWidget(self.ui.centralwidget)   
        vBox  = QVBoxLayout(self.sideWidget)
        self.ai_list = QComboBox(self.sideWidget)
        vBox.addWidget(self.ai_list)
        
        self.node_tree = NodeTree(self.sideWidget)
        vBox.addWidget(self.node_tree)
        
        self.ui.horizontalLayout.addWidget(self.sideWidget)
        
        self.graphicsView = GraphicView(self.ui.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.ui.horizontalLayout.addWidget(self.graphicsView)
        
        
        self.node_tree.itemDoubleClicked.connect(self.tree_item_doubleClicked)
        self.ui.action_open.triggered.connect(self.action_open)
        self.ui.action_save.triggered.connect(self.action_save)
        self.ui.action_attach.triggered.connect(self.action_attach)
        self.ui.action_add_node.triggered.connect(self.action_add_node)
        
        self.udpSocket = QUdpSocket(self)
        self.udpSocket.bind(QHostAddress("127.0.0.1"),0)
        self.udpSocket.readyRead.connect(self.readPendingDatagrams)
    
        
    def readPendingDatagrams(self):
        while self.udpSocket.hasPendingDatagrams():
            datagram = self.udpSocket.receiveDatagram()
            self.processTheDatagram(datagram)
        
    def processTheDatagram(self, dataGram: QNetworkDatagram):
        jsonStr = dataGram.data().toStdString()
        data = json.loads(jsonStr)
        cmd = data['cmd']
        content = data['content']
        match cmd:
            case "get_list":
                self.OnGetList(content)
            case "node_states":
                self.OnNodeStates(content)
            case _:
                print(f"unexpected cmd : {cmd}")
                
    def OnGetList(self, content):
        data = json.loads(content)
        print(f"on get list : {data}")
        
        
        
        
    @Slot()
    def tree_item_doubleClicked(self,e: QTreeWidgetItem):
        node_name = e.text(0)
        if node_name in g.config.data['nodes'].keys():
            dialog = AddNodeDialog(node_name)
            result = dialog.exec_()
            if result == 1:
                self.node_tree.update_tree()

    
    @Slot()
    def action_open(self):
        dialog = QFileDialog()
        last_path = g.config.data['last_project']
        filename,_ext = dialog.getOpenFileName(self,"Open file",last_path,"json(*.json)")
        if filename == "":
            return
        self.graphicsView.load_file(file_name = filename)
    
    @Slot()
    def action_save(self):
        if self.graphicsView.file_name is None:
            dialog = QFileDialog()
            last_path = g.config.data['last_project']
            filename,_ext = dialog.getSaveFileName(self, "Save file",last_path,"json(*.json)")
            if filename == "":
                return
            self.graphicsView.save_file(file_name = filename)
        else:
            self.graphicsView.save_file()

    @Slot()
    def action_add_node(self):
        dialog = AddNodeDialog()
        result = dialog.exec_()
        if result == 1:
            self.node_tree.update_tree()
        
    def action_attach(self):
        self.send_cmd("get_list","")
        
    def send_cmd(self,cmd,content = ""):
        data = {"cmd": cmd, "content": content}
        bytesData = json.dumps(data).encode("utf-8")
        self.udpSocket.writeDatagram(bytesData, QHostAddress("127.0.0.1"), 9091)
        self.udpSocket.flush()
        
        
        
        