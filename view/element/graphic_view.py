from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from view.element.node import *
from view.element.tmp_link import *
from view.element.link import *
import json
from core import g
import os

class GraphicView(QGraphicsView):
    nodes = {}
    links = {}

    def __init__(self, parent: QWidget):
        super(GraphicView, self).__init__(parent)
        # hide the scrollbar
        super(GraphicView, self).setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        super(GraphicView, self).setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.file_name = None
        self.startPos = None
        self.start_link = None
        self.tmp_link = None
        self.tmp_sel_rect = None
        self.sel_start_pos = None
        self.adding_node_name = None
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setup_ui()

    def setup_ui(self):
        self.horizontalSpacing = 180
        self.verticalSpacing = 60
        self.setScene(QGraphicsScene())
        self.setMouseTracking(True)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)
        self.setAcceptDrops(True)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        self.add_node(QNode(node_name="Root"))
        self.timer_id = self.startTimer(1000, timerType=Qt.VeryCoarseTimer)
        
        
    def timerEvent(self, event):
        if g.need_save == True:
            g.need_save = False
            self.save_file()
                
    def save_file(self,file_name: str = None):
        if file_name is not None:
            self.file_name = file_name
        if self.file_name is not None:            
            g.save_file(self.nodes,self.file_name)
        
        
    def load_file(self,file_name):
        data = None
        with open(file_name) as f:
            content = f.read()
            data = json.loads(content)
            f.close()
        if data is None:
            return
        self.file_name = file_name
        g.config.data['last_project'] = self.file_name
        self.load_from_data(data)
        g.save_config()

    def upgrade_all_files(self, folder_path):
        for root, ds, fs in os.walk(folder_path):
            print(root)
            for f in fs:
                fullname = os.path.join(root, f)
                if fullname.endswith('.json'):
                    self.load_file(fullname)
                    self.save_file(fullname)
            
    def load_from_data(self, data):
        self.clear_workspace()
        for v in data['nodes']:
            guid = v['guid']
            name = v['name']
            x = v['x']
            y = v['y']
            child_GUIDS = v['children']
            parent = v['parent']
            params = v['param_values']
            node = QNode(node_name = name,guid = guid,params= params)
            node.child_GUIDS =  child_GUIDS
            node.parent_GUID = parent
            self.add_node(node,QPointF(x,y))
        for guid, v in self.nodes.items():
            for c_guid in v.child_GUIDS:
                self.add_link(v,self.nodes[c_guid])
        for node_name, v in data['default_values'].items():
            node_config = g.config.data['nodes'].get(node_name)
            if node_config is not None:
                for param_name, loaded_param_default_value in v.items():
                    param_config = node_config['params'].get(param_name)
                    if param_config is not None:
                        param_config['default_value'] = loaded_param_default_value
    
    def clear_workspace(self):
        self.scene().clear()
        self.links = {}
        self.nodes = {}
        self.file_name = None
            
            
        


    def add_node(self, node: QNode, pos: QPointF =  None):
        self.nodes[node.GUID] = node
        self.scene().addItem(node)
        if pos is not None:
            node.setPos(pos)

    def link_nodes(self, parent_node: QNode, child_node: QNode):
        if parent_node.GUID == child_node.GUID:
            return
        if parent_node.GUID in child_node.child_GUIDS:
            self.remove_link(f"{child_node.GUID}@{parent_node.GUID}")
            child_node.remove_child(parent_node.GUID)
            parent_node.parent_GUID = ""

        old_parent = self.nodes.get(child_node.parent_GUID)
        if old_parent is not None:
            self.remove_link(f"{old_parent.GUID}@{child_node.GUID}")
            old_parent.remove_child(child_node.GUID)
            child_node.parent_GUID = ""
            if old_parent.GUID != parent_node.GUID:
                parent_node.add_child(child_node)
                self.add_link(parent_node, child_node)
        else:
            parent_node.add_child(child_node)
            self.add_link(parent_node, child_node)

    def add_link(self, parent_node, child_node):
        link_id = f"{parent_node.GUID}@{child_node.GUID}"
        if self.links.get(link_id) is None:
            link_item = Link(parent_node, child_node)
            self.scene().addItem(link_item)
            self.links[link_id] = link_item

    def remove_link(self, link_id):
        if self.links.get(link_id) is not None:
            self.scene().removeItem(self.links[link_id])
            del self.links[link_id]
            
            
    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        if e.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            data = e.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(data, Qt.CopyAction, 0, 0, QModelIndex())
            self.adding_node_name = source_item.item(0, 0).text()
            if self.adding_node_name in g.config.data['nodes'].keys():
                e.acceptProposedAction()


                # return super().dragEnterEvent(e)
    def dragMoveEvent(self, e: QDragMoveEvent) -> None:
        e.accept()
                
        # return super().dragMoveEvent(e)            
            
    def dropEvent(self, e: QDropEvent) -> None:
        if self.adding_node_name in g.config.data['nodes'].keys() and self.adding_node_name != "Root":
            node = QNode(node_name=self.adding_node_name)
            self.add_node(node)
            node.setPos( self.mapToScene(e.position().toPoint()))
        else:
            self.adding_node_name = None
            

            

    def wheelEvent(self, event: QWheelEvent) -> None:
        zoom_in_factor = 1.1
        zoom_out_factor = 1 / zoom_in_factor

        # Set Anchors

        # Save the scene sda pos
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
        super(GraphicView, self).mousePressEvent(event)
        if event.button() == Qt.MouseButton.MiddleButton:
            # store the origin point
            self.startPos = event.pos()
        elif event.button() == Qt.MouseButton.RightButton:
            item = self.scene().itemAt(self.mapToScene(event.pos()), QTransform())
            if item is None:
                return
            if item.tail_position is None:
                return
            self.start_link = item
        elif event.button() == Qt.MouseButton.LeftButton:
            if len(self.scene().selectedItems()) == 0 :
                self.sel_start_pos = self.mapToScene(event.pos())
        else:
            pass
            # sup

    def mouseMoveEvent(self, event):
        if self.startPos is not None and QApplication.mouseButtons() == Qt.MouseButton.MiddleButton:
            # compute the difference between the current cursor position and the
            # previous saved origin point
            delta = self.startPos - event.pos()
            # move view
            self.move_view(delta.x(), delta.y())
            # update the new origin point to the current position
            self.startPos = event.pos()

        elif isinstance(self.start_link, QNode) and QApplication.mouseButtons() == Qt.MouseButton.RightButton:
            p1: QPointF = self.start_link.link_start_pos()
            p2: QPointF = self.mapToScene(event.pos())
            line = QLineF(p1, p2)
            if self.tmp_link is None:
                self.tmp_link = TmpLink(line)
                self.scene().addItem(self.tmp_link)
            else:
                self.tmp_link.set_line(line)
        elif QApplication.mouseButtons() == Qt.MouseButton.LeftButton:
            super(GraphicView, self).mouseMoveEvent(event)
            nodes = self.scene().selectedItems()
            if len(nodes) > 0:
                self.sel_start_pos = None
            if self.sel_start_pos is None:
                for node in nodes:
                    self.update_related_links(node)
            else:
                p1 = self.sel_start_pos
                p2 = self.mapToScene(event.pos())
                sp1 = QPointF(min(p1.x(), p2.x()), min(p1.y(), p2.y()))
                sp2 = QPointF(max(p1.x(), p2.x()), max(p1.y(), p2.y()))
                rect = QRectF(sp1, sp2)
                if self.tmp_sel_rect is None:
                    self.tmp_sel_rect = QGraphicsRectItem(rect)
                    self.tmp_sel_rect.setPen(QPen(QColor(0, 240, 0), 1, Qt.SolidLine))
                    self.scene().addItem(self.tmp_sel_rect)
                else:
                    self.tmp_sel_rect.setRect(rect)
        else:
            super(GraphicView, self).mouseMoveEvent(event)

    def update_related_links(self, node: QNode):
        if node is None:
            return
        link_guids = [f"{node.parent_GUID}@{node.GUID}"]
        for guid in node.child_GUIDS:
            if guid not in link_guids:
                link_guids.append(f"{node.GUID}@{guid}")
        for link_guid in link_guids:
            link = self.links.get(link_guid)
            if link is not None:
                link.up()

    def mouseReleaseEvent(self, event):
        if len(self.scene().selectedItems()):
            g.need_save = True
        if self.start_link is not None:
            self.scene().removeItem(self.tmp_link)
            self.tmp_link = None
            item = self.scene().itemAt(self.mapToScene(event.pos()), QTransform())
            if isinstance(item, QNode):
                if item.node_type != "Root":
                    self.link_nodes(self.start_link, item)
            self.start_link = None
        elif self.startPos is not None:
            self.startPos = None
        elif self.sel_start_pos is not None and self.tmp_sel_rect is not None:
            items = self.scene().collidingItems(self.tmp_sel_rect, Qt.ItemSelectionMode.IntersectsItemShape)
            for item in items:
                item.setSelected(True)
            self.sel_start_pos = None
            self.scene().removeItem(self.tmp_sel_rect)
            self.tmp_sel_rect = None
        super(GraphicView, self).mouseReleaseEvent(event)

    # def mouseDoubleClickEvent(self, event: QMouseEvent):
    #     if len(self.scene().selectedItems()) == 1:
    #         print("begin link")

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_W:
            print("w")
        elif event.key() == Qt.Key.Key_S:
            print("S")
        elif event.key() == Qt.Key.Key_A:
            print("A")
        elif event.key() == Qt.Key.Key_D:
            print("D")
        # elif event.key() == Qt.Key.Key_F:
            # items = self.scene().selectedItems()
            # if len(items) > 0:
            #     current_pos = self.sceneRect().center()
            #     target_pos = items[0].pos()
            #     delta = target_pos - current_pos
            #     self.move_view(delta.x(), delta.y())
            # else:
            #     self.move_view(0, 0)
        elif event.key() == Qt.Key.Key_Delete:
            self.del_selected_nodes()
        elif event.key() == Qt.Key.Key_Space:
            self.align_nodes()
        elif event.matches(QKeySequence.Copy):
            self.copy_nodes()
        elif event.matches(QKeySequence.Paste):
            self.paste_nodes()
        return super().keyPressEvent(event)


    def del_selected_nodes(self):
        items = self.scene().selectedItems()
        g.need_save = True
        for item in items:
            if item.node_type != "Root":
                self.del_node(item)

    def del_node(self, item: QNode):
        parent_node = self.nodes.get(item.parent_GUID)
        if parent_node is not None:
            parent_node.remove_child(item.GUID)
            self.remove_link(f"{parent_node.GUID}@{item.GUID}")
        for c_guid in item.child_GUIDS:
            self.nodes[c_guid].parent_GUID = ""
            self.remove_link(f"{item.GUID}@{c_guid}")
        del self.nodes[item.GUID]
        self.scene().removeItem(item)


    def align_nodes(self):
        g.need_save = True
        self.leafCount = 0
        self.depth = 0
        self.movedNodes = []
        o_pos = self.nodes['0'].pos()
        self.align_nodeX('0')
        dis = o_pos - self.nodes['0'].pos()
        for i in range(len(self.movedNodes)):
            n = self.movedNodes[i]
            n.setPos(n.pos() + dis)
            self.update_related_links(n)
        
    def align_nodeX(self, guid):
        node = self.nodes[guid]
        self.movedNodes.append(node)
        if len(node.child_GUIDS) == 0:
            self.leafCount += 1
            x = self.depth * self.horizontalSpacing
            y = self.leafCount * self.verticalSpacing
        else:
            ySum = 0
            node.child_GUIDS.sort(key=lambda i: self.nodes[i].pos().y())
            for cguid in node.child_GUIDS:
                self.depth += 1
                ySum += self.align_nodeX(cguid)
                self.depth -= 1

            x = self.depth * self.horizontalSpacing
            y = ySum / len(node.child_GUIDS)
        node.setPos(x, y)
        self.update_related_links(node)
        return y        

    def copy_nodes(self):
        items = self.scene().selectedItems()
        default_values = g.config.get_default_values()
        data = {"nodes": [], "default_values": default_values}
        for item in items:
            data['nodes'].append(
                {"guid": item.GUID, "name": item.name, "x": item.x(), "y": item.y(), "children": item.child_GUIDS, "parent": item.parent_GUID,
                 "param_values": item.params})
        bin = json.dumps(data, indent=4)
        QApplication.clipboard().setText(bin)

    def paste_nodes(self):
        copy_str = QApplication.clipboard().text()
        json_table = json.loads(copy_str)
        selections = self.try_load_from_clipboard(json_table)
        self.scene().clearSelection()
        for selection in selections:
            selection.setSelected(True)

    def try_load_from_clipboard(self, data):
        nodes = []

        nodes_guid_map = {}

        for v in data['nodes']:
            guid = v['guid']
            name = v['name']
            # 加点偏移不然完全看不出粘贴了东西
            x = v['x'] + 50
            y = v['y'] + 50
            child_GUIDS = v['children']
            parent = v['parent']
            params = v['param_values']
            node = QNode(node_name = name,params= params)
            node.child_GUIDS = child_GUIDS
            node.parent_GUID = parent
            nodes.append(node)
            self.add_node(node,QPointF(x,y))
            nodes_guid_map[guid] = node.GUID

        def get_new_guid(old_guid):
            new_guid = nodes_guid_map.get(old_guid)
            if new_guid is None:
                new_guid = old_guid
            return new_guid

        #旧guid根据映射改成新guid
        for node in nodes:
            new_child_guids = []
            for child_guid in node.child_GUIDS:
                new_child_guids.append(get_new_guid(child_guid))
            node.child_GUIDS = new_child_guids
            node.parent_GUID = get_new_guid(node.parent_GUID)

        for guid, v in self.nodes.items():
            for c_guid in v.child_GUIDS:
                self.add_link(v,self.nodes[c_guid])
        for node_name, v in data['default_values'].items():
            node_config = g.config.data['nodes'].get(node_name)
            if node_config is not None:
                for param_name, loaded_param_default_value in v.items():
                    param_config = node_config['params'].get(param_name)
                    if param_config is not None:
                        param_config['default_value'] = loaded_param_default_value
        return nodes

    def update_node_states(self, infos):
        for info in infos:
            guid = info["guid"]
            state = info["state"]
            node = self.nodes.get(guid)
            if node is not None:
                node.set_state(state)
                     
    def move_view(self, x, y):
        # get the current transformation (which is a matrix that includes the
        # scaling ratios
        transform = self.transform()
        # m11 refers to the horizontal scale, m22 to the vertical scale;
        # divide the delta by their corresponding ratio
        delta_x = x / transform.m11()
        delta_y = y / transform.m22()
        # translate the current sceneRect by the delta
        self.setSceneRect(self.sceneRect().translated(delta_x, delta_y))
        # sync the rect modification to the scrollbar
        hs = super(GraphicView, self).horizontalScrollBar()
        vs = super(GraphicView, self).verticalScrollBar()
        hs.setValue(hs.value() + x)
        vs.setValue(vs.value() + y)