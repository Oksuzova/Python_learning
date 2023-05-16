import random
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import math
import string


class DrawNode(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.createGraphicView()

        self.greenBrush = QBrush(Qt.GlobalColor.darkCyan)
        self.grayBrush = QBrush(Qt.GlobalColor.darkGray)

        self.names = string.ascii_uppercase

        self.db = Storage()

        self.x_coord = 0
        self.y_coord = 0
        self.node_objs = {}
        self.edge_objs = {}
        self.coords = []
        self.step = [80, -80]

        self.db_edge = self.db.get_edge()

    def createGraphicView(self):
        self.pen = QPen()
        self.pen_edge = QPen()
        self.pen_edge.setColor(Qt.GlobalColor.darkRed)
        self.pen_edge.setWidth(2)
        self.scene = QGraphicsScene()

        graphicView = QGraphicsView(self.scene, self)

        graphicView.setGeometry(0, 0, 800, 665)
        graphicView.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
        graphicView.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        graphicView.setAlignment(Qt.AlignmentFlag.AlignCenter)
        graphicView.setRenderHint(QPainter.RenderHint.Antialiasing)

    def create_graph(self, num):
        for i in range(num):
            name = self.names[i]
            self.db.set_node(name)
            self.node_objs[name] = self.scene.addEllipse(self.x_coord, self.y_coord, 30, 30, self.pen, self.greenBrush)
            text = self.scene.addText(name)
            text.setPos(self.x_coord + 7, self.y_coord + 2)
            self.coords.append([self.node_objs[name].rect().x(), self.node_objs[name].rect().y()])
            self.x_coord = 0
            self.y_coord = 0
            self.set_coord()
            print(self.db.get_nodes())

    def set_coord(self):
        step_x = random.choice(self.step)
        step_y = random.choice(self.step)
        self.x_coord += step_x + random.randint(0, 20)
        self.y_coord += step_y + random.randint(0, 20)
        for i in self.coords:
            if self.x_coord in range(int(i[0]-50), int(i[0]+50)) and self.y_coord in range(int(i[1]-50), int(i[1]+50)):
                if -350 < self.x_coord > 350:
                    self.x_coord = 0
                if -280 < self.y_coord > 280:
                    self.y_coord = 0
                self.set_coord()

    def set_step(self, num):
        if num > 8:
            self.step = [100, -100]
        else:
            self.step = [130, -130]

        self.scene.clear()
        self.x_coord = 0
        self.y_coord = 0
        self.node_objs = {}
        self.coords = []

        self.create_graph(num)

    def add_node(self, name):
        if self.check_name(name):
            return
        self.set_coord()
        self.node_objs[name] = self.scene.addEllipse(self.x_coord, self.y_coord, 30, 30, self.pen, self.greenBrush)
        self.db.set_node(name)
        text = self.scene.addText(name)
        text.setPos(self.x_coord + 7, self.y_coord + 2)
        self.coords.append([self.node_objs[name].rect().x(), self.node_objs[name].rect().y()])

    def check_name(self, name):
        for i in self.node_objs:
            if name == i:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("The name is already exist")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.exec()
                return True

    def edge_coord(self, name1, name2):
        ellipse = self.node_objs[name1]
        ellipse1 = self.node_objs[name2]
        r = 15
        el_x0 = ellipse.rect().center().x()
        el_x1 = ellipse1.rect().center().x()

        el_y0 = ellipse.rect().center().y()
        el_y1 = ellipse1.rect().center().y()

        d = math.sqrt((el_x0 - el_x1) ** 2 + (el_y0 - el_y1) ** 2)

        self.x = el_x1 + (el_x0 - el_x1) / d * r
        self.y = el_y1 + (el_y0 - el_y1) / d * r

        d1 = math.sqrt((el_x1 - el_x0) ** 2 + (el_y1 - el_y0) ** 2)

        self.x1 = el_x0 + (el_x1 - el_x0) / d1 * r
        self.y1 = el_y0 + (el_y1 - el_y0) / d1 * r

    def add_edge(self, name1, name2):
        self.edge_coord(name1, name2)

        edge = self.scene.addLine(self.x, self.y, self.x1, self.y1, self.pen)
        self.edge_objs[name1] = self.edge_objs.get(name1, []) + [{name2: edge}]
        self.edge_objs[name2] = self.edge_objs.get(name2, []) + [{name1: edge}]
        self.db.set_edge(name1, name2)
        print(self.edge_objs)

    def show_path(self, name1, name2):
        db = self.db_edge
        ways = list(self.dfs(db, name1, name2))
        shortest_path = self.shortest_path(ways)

        # shortest_path = [(sh_path[i], sh_path[i + 1]) for i in range(len(sh_path) - 1)]
        #
        # for path in shortest_path:
        #     for i in self.edge_objs[path[0]]:
        #         for j in range(len(i)):
        #             i[path[1]].setPen(self.pen_edge)

        for start in shortest_path:
            for end in shortest_path:
                if start in self.edge_objs:
                    for i in self.edge_objs[start]:
                        try:
                            i[end].setPen(self.pen_edge)
                        except KeyError:
                            continue
                else:
                    continue

    def shortest_path(self, ways):
        sh_path = ways[0]
        for path in ways:
            if len(sh_path) > len(path):
                sh_path = path
        return sh_path

    def dfs(self, gr, start, goal):
        unseen = [(start, [start])]
        while unseen:
            (node, path) = unseen.pop()
            for next in gr[node] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    unseen.append((next, path + [next]))

class Storage(QObject):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.graph_data = {}

    def get_nodes(self):
        return self.graph_data.keys()

    def set_node(self, name):
        self.graph_data[name] = set()

    def get_edge(self):
        return self.graph_data

    def set_edge(self, name1, name2):
        self.graph_data[name1].add(name2)
        self.graph_data[name2].add(name1)


class MainWindow(QMainWindow):

    graph = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Window")
        self.setFixedSize(1200, 700)
        self.node1 = DrawNode()

        self.init_ui()


    def init_ui(self):
        # Set number of nodes group
        self.num_nodes_group = QGroupBox("Set number of nodes")

        self.num_nodes_le = QLineEdit()
        self.num_nodes_le.setPlaceholderText("Enter number of nodes: 5")
        self.num_nodes_le.setFocus()

        self.num_nodes_bt = QPushButton("Set")

        # Add the node group
        self.add_node_group = QGroupBox("Add the node")

        self.add_node_le = QLineEdit()
        self.add_node_le.setPlaceholderText("Enter the node: A")

        self.add_node_bt = QPushButton("Set")

        # Add the edge group
        self.add_edge_group = QGroupBox("Add the edge")

        self.from_edge_le = QLineEdit()
        self.from_edge_le.setPlaceholderText("A")
        self.to_edge_le = QLineEdit()
        self.to_edge_le.setPlaceholderText("C")

        self.add_edge_bt = QPushButton("Set")

        # Show path group
        self.path_group = QGroupBox("The shortest path")

        self.from_path_le = QLineEdit()
        self.from_path_le.setPlaceholderText("from: C")
        self.to_path_le = QLineEdit()
        self.to_path_le.setPlaceholderText("to: F")

        self.path_bt = QPushButton("Show")

        # Matrix widget
        #TODO: 1. Create matrix widget

        # Graph widget
        #TODO: 2. Create graph widget
        self.graph_group = QGroupBox()

        # self.node1.add_node()
        # self.node1.add_edge()
        self.node1.setMinimumWidth(750)
        self.node1.setMinimumHeight(600)


        # activated.connect
        #TODO: 3. Activate connections
        self.num_nodes_bt.clicked.connect(self.set_num_nodes)
        self.add_node_bt.clicked.connect(self.add_node)
        self.add_edge_bt.clicked.connect(self.add_edge)
        self.path_bt.clicked.connect(self.show_path)


        # num_nodes_layout
        self.num_nodes_layout = QGridLayout()
        self.num_nodes_layout.addWidget(self.num_nodes_le, 0, 0)
        self.num_nodes_layout.addWidget(self.num_nodes_bt, 0, 1)
        self.num_nodes_group.setLayout(self.num_nodes_layout)

        # add_node_layout
        self.add_node_layout = QGridLayout()
        self.add_node_layout.addWidget(self.add_node_le, 0, 0)
        self.add_node_layout.addWidget(self.add_node_bt, 0, 1)
        self.add_node_group.setLayout(self.add_node_layout)

        # add_edge_layout
        self.add_edge_layout = QGridLayout()
        self.add_edge_layout.addWidget(self.from_edge_le, 0, 0)
        self.add_edge_layout.addWidget(self.to_edge_le, 0, 1)
        self.add_edge_layout.addWidget(self.add_edge_bt, 0, 2)
        self.add_edge_group.setLayout(self.add_edge_layout)

        # path_group_layout
        self.path_group_layout = QGridLayout()
        self.path_group_layout.addWidget(self.from_path_le, 0, 0)
        self.path_group_layout.addWidget(self.to_path_le, 0, 1)
        self.path_group_layout.addWidget(self.path_bt, 1, 0, 1, 2)
        self.path_group.setLayout(self.path_group_layout)

        # graph_group
        self.graph_group_layout = QGridLayout()
        self.graph_group_layout.addWidget(self.node1, 0, 0, 5, 5)
        self.graph_group.setLayout(self.graph_group_layout)

        # layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.num_nodes_group, 0, 0)
        self.layout.addWidget(self.add_node_group, 1, 0)
        self.layout.addWidget(self.add_edge_group, 2, 0)
        self.layout.addWidget(self.path_group, 3, 0)


        self.layout.addWidget(self.graph_group, 0, 1, 10, 10)


        self.mw = QWidget()
        self.mw.setLayout(self.layout)
        self.setCentralWidget(self.mw)

    def set_num_nodes(self):
        num_nodes = int(self.num_nodes_le.text())
        self.num_nodes_le.clear()
        self.node1.set_step(num_nodes)

    def add_node(self):
        name_node = self.add_node_le.text().upper()
        self.add_node_le.clear()
        self.node1.add_node(name_node)

    def add_edge(self):
        name1 = self.from_edge_le.text().upper()
        self.from_edge_le.clear()
        name2 = self.to_edge_le.text().upper()
        self.to_edge_le.clear()
        self.node1.add_edge(name1, name2)

    def show_path(self):
        name1 = self.from_path_le.text().upper()
        self.from_path_le.clear()
        name2 = self.to_path_le.text().upper()
        self.to_path_le.clear()
        self.node1.show_path(name1, name2)



def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()











