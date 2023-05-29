# -*- coding: cp1251 -*-1

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import networkx as nx
import sys
import matplotlib.pyplot as plt
import random


class QTableViewM(QTableView):
    def __init__(self):
        super().__init__()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers or
                             QAbstractItemView.DoubleClicked)

    def keyPressEvent(self, event=QKeyEventTransition):  # Reimplement the event here, in your case, do nothing
        super().keyPressEvent(event)
        if event.key() == 16777220: self.enterPressEvent(event)

    def enterPressEvent(self, event=QKeyEventTransition):
        pass


class Table(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.items = []
        self.namev = []
        self.nameh = []

    def columnCount(self, parent=None, *args, **kwargs):
        if len(self.items) == 0:
            return 0
        else:
            return len(self.items[0])

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole and role != Qt.EditRole:
            return QVariant()
        return QVariant(str(self.items[index.row()][index.column()]))

    def clear(self):

        self.beginResetModel()
        self.items = []
        self.nameh = []
        self.namev = []
        self.endResetModel()

    def append_sqr(self):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.beginInsertColumns(QModelIndex(), self.rowCount(), self.rowCount())

        if len(self.items) != 0:
            for i in range(len(self.items)):
                self.items[i].append(0)
            self.items.append([0] * len(self.items[0]))

            self.nameh.append(str(self.columnCount()))
            self.namev.append(str(self.rowCount()))

        else:
            self.items = [[0]]
            self.nameh.append(str(self.columnCount()))
            self.namev.append(str(self.rowCount()))

        self.endInsertRows()
        self.endInsertColumns()

    def del_sqr(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.beginRemoveColumns(QModelIndex(), self.rowCount(), self.rowCount())

        if len(self.items) != 0:
            for i in range(len(self.items) - 1):
                self.items[i].pop(-1)
            self.items.pop(-1)
            self.namev.pop(-1)
            self.nameh.pop(-1)

        else:
            pass

        self.endRemoveRows()
        self.endRemoveColumns()
        self.endResetModel()

    def append(self, item, name):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.items.append(item)
        self.endInsertRows()
        self.nameh.append(name)

    def appendname(self, name=[]):
        for i in name:
            self.beginInsertColumns(QModelIndex(), self.rowCount(), self.rowCount())
            self.namev.append(i)
            self.endInsertColumns()

    def headerData(self, index, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.namev[index])
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(self.nameh[index])
        return QVariant()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, QModelIndex, Any, p_int=None):
        self.beginResetModel()

        self.items[QModelIndex.row()][QModelIndex.column()] = Any
        self.items[QModelIndex.column()][QModelIndex.row()] = Any
        self.endResetModel()
        return False

    def setIData(self, column, row, data):
        self.beginResetModel()
        self.items[row][column] = data
        self.items[column][row] = data
        self.endResetModel()

    def getItems(self):
        items = []
        k = -1
        for i in self.items:
            k += 1
            items.append([])
            for j in self.items[k]:
                items[k].append(j)
        return items


class Item(QObject):
    def __init__(self, name=None, sex=None):
        super().__init__()
        self.name = name
        self.sex = sex

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return (self.name == other.name and self.sex == other.sex)



def graph_color(graph=nx.Graph):
    colors = ["blue", "green", "red", "grey", "purple", "pink",
              "orange", "black", "brown", "magenta", "cyan", "fuchsia",
              "indigo", "springgreen", "olive", "lime"]
    coloris = ["black"] * (len(graph.nodes()))
    colored = []
    graph_degs = sorted(graph.degree(), key=lambda x: x[1], reverse=True)
    for i in graph_degs:
        node = i[0]
        nei_node = [n for n in graph.neighbors(node)]
        flag = False
        for i in range(len(colored)):
            if not set(nei_node) & set(colored[i]):
                colored[i].append(node)
                flag = True
                coloris[node - 1] = (colors[i])
                break
        if not flag:
            colored.append([node])
            coloris[node - 1] = (colors[len(colored) - 1])
    nx.draw(graph, nx.circular_layout(graph), node_color=coloris, with_labels=True)
    plt.show()


class mainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.__initUI()

    def __initUI(self):

        self.table = QTableViewM()
        self.model = Table()
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.grid = QGridLayout()

        self.grid.addWidget(self.table, 0, 0, 9, 4)

        self.button_add = QPushButton()
        self.button_add.setText("add")
        self.grid.addWidget(self.button_add, 0, 4)
        self.button_add.clicked.connect(self.but_add)

        self.button_del = QPushButton()
        self.button_del.setText("del")
        self.grid.addWidget(self.button_del, 1, 4)
        self.button_del.clicked.connect(self.but_del)

        self.button_default = QPushButton()
        self.button_default.setText("Побудувати граф за замовчуванням")
        self.grid.addWidget(self.button_default, 2, 4)
        self.button_default.clicked.connect(self.default)

        self.button_custom = QPushButton()
        self.button_custom.setText("Побудувати граф за таблицею")
        self.grid.addWidget(self.button_custom, 3, 4)
        self.button_custom.clicked.connect(self.custom)

        self.button_clear = QPushButton()
        self.button_clear.setText("Очистити таблицю")
        self.grid.addWidget(self.button_clear, 4, 4)
        self.button_clear.clicked.connect(self.clear)

        self.button_random = QPushButton()
        self.button_random.setText("Випадково згенерувати")
        self.grid.addWidget(self.button_random, 5, 4)
        self.button_random.clicked.connect(self.random)

        self.setLayout(self.grid)

        self.setGeometry(323, 323, 623, 373)
        self.setWindowTitle("Лабораторна робота 4")
        self.show()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def but_add(self):
        self.model.append_sqr()

    def but_del(self):
        self.model.del_sqr()

    def default(self):
        graph = nx.Graph()
        graph.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        graph.add_edges_from([{1, 2}, {1, 6}, {2, 3},
                              {2, 6}, {2, 7}, {3, 4},
                              {3, 7}, {3, 9}, {4, 5},
                              {7, 8}, {8, 9}, {8, 10}, {5, 10}])

        graph_color(graph)

    def custom(self):
        graph = nx.Graph()
        items = self.model.getItems()
        lenn = len(items)
        nodes = list(range(1, lenn + 1))
        edges = self.edges(items)
        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges)
        graph_color(graph)

    def edges(self, matrix):
        edges = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] and matrix[i][j] != "0" and matrix[i][j] == matrix[j][i] and i < j:
                    edges.append({i + 1, j + 1})
        return edges

    def clear(self):
        self.model.clear()

    def random(self):
        if len(self.model.items) in [0, 1]:
            print(self.model.items)
            return None
        self.model.clear()
        i = random.randrange(int(len((self.model.items)) * (len(self.model.items) - 1) / 2 + 1))
        for i in range(i):
            j = random.randrange(len(self.model.items))
            k = random.randrange(len(self.model.items))
            if k != j:
                self.model.setIData(column=j, row=k, data=1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())