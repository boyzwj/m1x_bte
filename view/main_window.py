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
        debug_action = QAction("Debug",self)
        debug_action.setStatusTip("Debug project")  
        debug_action.triggered.connect(self.OnDebugClicked)
        debug_action.setCheckable(True)
        
        sync_action = QAction("Sync",self)
        sync_action.setStatusTip("Sync project")
        sync_action.triggered.connect(self.OnSyncClicked)
        sync_action.setCheckable(False)
        
        self.ui.toolBar.addAction(debug_action)
        self.ui.toolBar.addAction(sync_action)
            
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
        
        self.ai_list.currentIndexChanged.connect(self.on_combobox_changed)
        self.node_tree.itemDoubleClicked.connect(self.tree_item_doubleClicked)
        self.ui.action_open.triggered.connect(self.action_open)
        self.ui.action_save.triggered.connect(self.action_save)
        self.ui.action_add_node.triggered.connect(self.action_add_node)
        
        self.udpSocket = QUdpSocket(self)
        self.udpSocket.bind(QHostAddress("127.0.0.1"),0)
        self.udpSocket.readyRead.connect(self.readPendingDataGrams)
        self.timer_id = self.startTimer(3000, timerType=Qt.VeryCoarseTimer)
        self.debugID = None
        self.is_debug = False
    
    
    def OnDebugClicked(self,s):
        self.is_debug = s
        if self.is_debug:
            self.send_cmd("get_list","")
        else:
            self.debugID = None
            self.ai_list.clear()
        
    def OnSyncClicked(self,s):
        nodes = self.graphicsView.nodes
        data = []
        for k,v in nodes.items():
            data.append({"guid": k ,"name": v.name, "x": v.x(), "y": v.y(), "children": v.child_GUIDS, "parent": v.parent_GUID
                     ,"param_values": v.params})
        bin = json.dumps(data)
        self.send_cmd("sync_data",bin)
        
    def readPendingDataGrams(self):
        while self.udpSocket.hasPendingDatagrams():
            dataGram = self.udpSocket.receiveDatagram()
            self.processTheDataGram(dataGram)
        
    def processTheDataGram(self, dataGram: QNetworkDatagram):
        jsonStr = dataGram.data().toStdString()
        if jsonStr == "":
            return
        data = json.loads(jsonStr)
        cmd = data['cmd']
        content = data['content']
        match cmd:
            case "get_list":
                self.OnGetList(content)
            case "node_states":
                self.OnNodeStates(content)
            case "remote_tree_info":
                self.OnRemoteTreeInfo(content)
            case _:
                print(f"unexpected cmd : {cmd}")
                
    def OnGetList(self, content):
        data = json.loads(content)
        print(f"on get list : {data}")
        self.ai_list.clear()
        for i in range(len(data)):
            ai_id = data[i]
            self.ai_list.addItem(str(ai_id),ai_id)
        
        
    def OnNodeStates(self, content):
        data = json.loads(content)
        self.graphicsView.update_node_states(data)

    def OnRemoteTreeInfo(self, content):
        data = json.loads(content)
        self.graphicsView.load_from_data(data['nodes'])
    
    def timerEvent(self, event):
        if self.is_debug:
            self.send_cmd("heart")       
        
        
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
        filename, _ext = dialog.getOpenFileName(self,"Open file",last_path,"json(*.json)")
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
        
        
    def send_cmd(self,cmd,content = ""):
        data = {"cmd": cmd, "content": content}
        bytesData = json.dumps(data).encode("utf-8")
        self.udpSocket.writeDatagram(bytesData, QHostAddress("127.0.0.1"), 9091)
        self.udpSocket.flush()
        
        
        
    def on_combobox_changed(self, value):
        item = self.ai_list.itemData(value)
        if item is not None:
            self.debugID = item
            self.send_cmd("listen",str(item))
        else:
            self.debugID = None
        