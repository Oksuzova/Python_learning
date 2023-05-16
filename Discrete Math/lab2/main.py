from __future__ import annotations

import random

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import math


class SecondaryWindow(QMainWindow, QWidget):
    def __init__(self):
        super(SecondaryWindow, self).__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        self.db = None


    def set_storage(self, man: SetManager):
        self.db = man
        self.on_db_set()


    def on_db_set(self):
        raise NotImplementedError

    def show(self):
        self.setFocus()
        super().show()



class Window2(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window2")
        self.set_main_layout()

    def create_listboxes(self):
        self.listbox_set1 = QListWidget()
        self.listbox_set2 = QListWidget()

        self.listbox_set1.clicked.connect(self.choosen_items)
        self.listbox_set2.clicked.connect(self.choosen_items)

    def on_db_set(self):
        self.listbox_set1.addItems(self.db.womens_names)
        self.listbox_set2.addItems(self.db.mens_names)

    def choosen_items(self):
        listbox = self.sender()
        if listbox == self.listbox_set1:
            item = self.listbox_set1.currentItem()
        else:
            item = self.listbox_set2.currentItem()
        self.add_to_choosen_set(item.text())

    def add_to_choosen_set(self, item):
        if self.rb_setA.isChecked():
            self.db.set_value("set_A", item)
            self.lb_setA.setText(f"A: {self.db.get_value('set_A')}")
        else:
            self.db.set_value("set_B", item)
            self.lb_setB.setText(f"B: {self.db.get_value('set_B')}")

    def save_sets(self):
        with open ("result.txt", "w") as f:
            f.write(f"{self.db.get_value('set_A')}\n{self.db.get_value('set_B')}")
        self.bt_save.setDisabled(True)
        self.bt_clear.setDisabled(True)
        self.db.update_graph()

    def clear_sets(self):
        self.db.set_A.clear()
        self.db.set_B.clear()
        self.lb_setA.clear()
        self.lb_setA.setText(f"A:")
        self.lb_setB.clear()
        self.lb_setB.setText(f"B:")

    def set_main_layout(self):
        main_layout_w2 = QGridLayout()

        self.lb_setA = QLabel("A: ")
        self.lb_setB = QLabel("B: ")

        self.rb_setA = QRadioButton("Set A")
        self.rb_setA.setChecked(True)
        self.rb_setB = QRadioButton("Set B")

        self.bt_save = QPushButton("Save sets")
        self.bt_save.clicked.connect(self.save_sets)
        self.bt_clear = QPushButton("Clear sets")
        self.bt_clear.clicked.connect(self.clear_sets)

        self.create_listboxes()

        main_layout_w2.addWidget(QLabel("Select which set to add elements to:"), 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        main_layout_w2.addWidget(self.rb_setA, 2, 0)
        main_layout_w2.addWidget(self.rb_setB, 2, 1)

        main_layout_w2.addWidget(QLabel("Women`s names:"), 3, 0)
        main_layout_w2.addWidget(self.listbox_set1, 4, 0)
        main_layout_w2.addWidget(QLabel("Men`s names:"), 3, 1)
        main_layout_w2.addWidget(self.listbox_set2, 4, 1)

        main_layout_w2.addWidget(self.lb_setA, 5, 0, 1, 2)
        main_layout_w2.addWidget(self.lb_setB, 6, 0, 1, 2)

        main_layout_w2.addWidget(self.bt_save, 7, 0)
        main_layout_w2.addWidget(self.bt_clear, 7, 1)

        self.w2 = QWidget()
        self.w2.setLayout(main_layout_w2)
        self.setCentralWidget(self.w2)

class Window3(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window3")

        self.setGeometry(700, 200, 450, 650)

        self.lb_setA_w3 = QLabel("A:")
        self.lb_setB_w3 = QLabel("B:")

        self.gr = DrawGraph()
        self.gr2 = DrawGraph()

        self.set_main_layout()

    def update_labels(self):
        setA_lab = list(self.db.get_value("set_A"))
        setB_lab = list(self.db.get_value("set_B"))
        self.gr.labels(setA_lab, setB_lab)
        self.gr2.labels(setA_lab, setB_lab)
        self.gr.set_relation(self.db.is_father)
        self.gr2.set_relation(self.db.is_husband)

    def on_db_set(self):
        self.db.add_item_to_set.connect(self.set_labels)

    def set_labels(self):
        self.lb_setA_w3.setText(f"A: {self.db.get_value('set_A')}")
        self.lb_setB_w3.setText(f"B: {self.db.get_value('set_B')}")

    def set_main_layout(self):
        self.main_layout = QVBoxLayout()

        self.lay_set_a = QHBoxLayout()
        self.lay_set_a.addWidget(self.lb_setA_w3)
        self.frame_set_a = QGroupBox(self)
        self.frame_set_a.setTitle("Set A")
        self.frame_set_a.setLayout(self.lay_set_a)

        self.lay_set_b = QHBoxLayout()
        self.lay_set_b.addWidget(self.lb_setB_w3)
        self.frame_set_b = QGroupBox(self)
        self.frame_set_b.setTitle("Set B")
        self.frame_set_b.setLayout(self.lay_set_b)

        self.main_layout.addWidget(self.frame_set_a)
        self.main_layout.addWidget(self.frame_set_b)

        self.main_layout.addWidget(QLabel("Set aSb, if A father B:"))

        self.main_layout.addWidget(self.gr)

        self.main_layout.addWidget(QLabel("Set aRb, if A husband B:"))

        self.main_layout.addWidget(self.gr2)

        self.w3 = QWidget()
        self.w3.setLayout(self.main_layout)
        self.setCentralWidget(self.w3)


class Window4(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window4")
        self.setGeometry(300, 300, 400, 280)

        self.gr = DrawGraph()
        self.set_main_layout()


    def on_db_set(self):
        pass

    def create_buts(self):
        self.union_but = QPushButton("R \u222A S")
        self.intersection_but = QPushButton("R \u2229 S")
        self.dif_but = QPushButton("R \ S")
        self.dif_uniset_but = QPushButton("U \ R")
        self.reverse_but = QPushButton("S⁻¹")

        self.union_but.clicked.connect(self.action_union)
        self.intersection_but.clicked.connect(self.action_intersection)
        self.dif_but.clicked.connect(self.action_dif)
        self.dif_uniset_but.clicked.connect(self.action_dif_uniset)
        self.reverse_but.clicked.connect(self.action_reverse)

        self.buts_layout = QVBoxLayout()

        self.buts_layout.addWidget(self.union_but)
        self.buts_layout.addWidget(self.intersection_but)
        self.buts_layout.addWidget(self.dif_but)
        self.buts_layout.addWidget(self.dif_uniset_but)
        self.buts_layout.addWidget(self.reverse_but)

    def action_union(self):
        self.gr.set_reverse(False)
        self.gr.set_relation(self.db.union_sets)

    def action_intersection(self):
        self.gr.set_reverse(False)
        self.gr.set_relation(self.db.intersection_sets)

    def action_dif(self):
        self.gr.set_reverse(False)
        self.gr.set_relation(self.db.dif_sets)

    def action_dif_uniset(self):
        self.gr.set_reverse(False)
        self.gr.set_relation(self.db.dif_uniset_sets)

    def action_reverse(self):
        self.gr.set_reverse(True)
        self.gr.set_relation(self.db.is_father)

    def update_labels(self):
        setA_lab = list(self.db.get_value("set_A"))
        setB_lab = list(self.db.get_value("set_B"))
        self.gr.labels(setA_lab, setB_lab)

    def set_main_layout(self):
        main_layout = QHBoxLayout()

        self.create_buts()

        graph_layout = QVBoxLayout()
        graph_layout.addWidget(QLabel("Operations on relations"))
        graph_layout.addWidget(self.gr)

        main_layout.addLayout(self.buts_layout)
        main_layout.addLayout(graph_layout)

        self.w4 = QWidget()
        self.w4.setLayout(main_layout)
        self.setCentralWidget(self.w4)

class DrawGraph(QLabel):
    def __init__(self):
        super().__init__()

        self.top1_line = QHBoxLayout()
        self.bot1_line = QHBoxLayout()
        self.top2_line = QHBoxLayout()
        self.bot2_line = QHBoxLayout()

        self.relation = []
        self.lb_set_A = []
        self.lb_set_B = []

        self.reverse = False

        self.set_layout()

    def set_layout(self):
        self.main_layout = QVBoxLayout()

        self.main_layout.addLayout(self.top1_line)
        self.main_layout.addWidget(QLabel(""))
        self.main_layout.addWidget(QLabel(""))
        self.main_layout.addWidget(QLabel(""))
        self.main_layout.addLayout(self.bot1_line)

        self.setLayout(self.main_layout)

    def _splash_text(self, painter):
        if not self.lb_set_A and not self.lb_set_B:
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, 'No data for show')
            return
        if not self.lb_set_A and not self.lb_set_B:
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, 'No relations for show')

    def labels(self, setA_lab, setB_lab):

        for i in setA_lab:
            label = QDLabel(i)
            self.lb_set_A.append(label)
            self.top1_line.addWidget(label)

        for i in setB_lab:
            label = QDLabel(i)
            label.color = Qt.GlobalColor.black
            self.lb_set_B.append(label)
            self.bot1_line.addWidget(label)

    def set_relation(self, relation):
        self.relation = relation
        self.update()

    def set_reverse(self, state):
        self.reverse = state

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(Qt.GlobalColor.black)
        painter.setPen(Qt.GlobalColor.black)

        self._splash_text(painter)
        for i in self.relation:
            if not self.reverse:
                self.draw_arrow(painter, self.lb_set_A[i[0]], self.lb_set_B[i[1]])
            else:
                self.draw_arrow(painter, self.lb_set_B[i[1]], self.lb_set_A[i[0]])

    def draw_arrow(self, paint: QPainter, frm: QDLabel, to: QDLabel):
        arrowSize = 12
        line = frm.path_to(to).toLineF()
        angle = math.atan2(-line.dy(), line.dx())

        arrowP1 = line.p1() + QPointF(math.sin(angle + math.pi / 3) * arrowSize,
                                      math.cos(angle + math.pi / 3) * arrowSize)

        arrowP2 = line.p1() + QPointF(math.sin(angle + math.pi - math.pi / 3) * arrowSize,
                                      math.cos(angle + math.pi - math.pi / 3) * arrowSize)
        arrowHead = QPolygonF()

        arrowHead.append(line.p1())
        arrowHead.append(arrowP1)
        arrowHead.append(arrowP2)

        paint.drawLine(line)

        paint.drawPolygon(arrowHead)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Window1")
        self.set_manager = SetManager("setA", "setB")

        self.set_main_layout()

    def var(self):
        g = 21
        n = 8
        m = "ІО"
        if m == "ІО": n += 2
        var = (n + g % 60) % 30 + 1
        return f"Oksuzova T. E.\n" \
               f"My group: {m}-z{g}\n" \
               f"My number in group: {n - 2}\n" \
               f"My variant: {var}"

    def create_win_bt(self):
        self.window2 = Window2()
        self.window3 = Window3()
        self.window4 = Window4()

        self.window2.set_storage(self.set_manager)
        self.window3.set_storage(self.set_manager)
        self.window4.set_storage(self.set_manager)

        self.bt_window2 = QPushButton(self.window2.windowTitle())
        self.bt_window3 = QPushButton(self.window3.windowTitle())
        self.bt_window4 = QPushButton(self.window4.windowTitle())

        self.bt_window2.clicked.connect(self.window2.show)
        self.bt_window3.clicked.connect(self.window3.show)
        self.bt_window4.clicked.connect(self.window4.show)

        self.window2.bt_save.clicked.connect(self.window3.update_labels)
        self.window2.bt_save.clicked.connect(self.window4.update_labels)

    def set_main_layout(self):
        main_layout_for_win1 = QGridLayout()

        self.create_win_bt()

        self.var_label = QLabel(self.var())

        main_layout_for_win1.addWidget(self.var_label, 0, 0, 2, 2)
        main_layout_for_win1.addWidget(self.bt_window2, 2, 0)
        main_layout_for_win1.addWidget(self.bt_window3, 2, 1)
        main_layout_for_win1.addWidget(self.bt_window4, 2, 2)

        self.mw = QWidget()
        self.mw.setLayout(main_layout_for_win1)
        self.setCentralWidget(self.mw)

class SetManager(QObject):

    add_item_to_set = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.womens_names = ['Anastasia', 'Zoya', 'Irina', 'Olena', 'Martha', 'Julia', 'Darina', 'Oksana', 'Olga', 'Maria',
                      'Sofia', 'Diana', 'Alina']
        self.mens_names = ['Vitaliy', 'Dmitro', 'Artem', 'Arsen', 'Maxim', 'Sergey', 'Oleg', 'Petro', 'Vasil', 'Fedir',
                      'Bogdan', 'Vladislav', 'Viktor']

        self._store = {i: [] for i in args}

    def update_graph(self):
        self.is_father = self.is_father()
        self.is_husband = self.is_husband()
        self.union_sets = self.union_sets()
        self.intersection_sets = self.intersection_sets()
        self.dif_sets = self.dif_sets()
        self.dif_uniset_sets = self.dif_uniset_sets()

    def is_father(self):
        set_a = list(self.get_value("set_A"))
        father_set_a = []
        child_set_b = []
        set_b = list(self.get_value("set_B"))
        item_f = []
        item_ch = []

        for i in set_a:
            if i in self.mens_names:
                father_set_a.append(set_a.index(i))
                item_f = random.choices(father_set_a, k=len(father_set_a))
        for i in set_b:
            child_set_b.append(set_b.index(i))
            item_ch = random.sample(child_set_b, int(len(child_set_b) // 1.5))


        self.fathers_relation = list(zip(item_f, item_ch))
        return self.fathers_relation

    def is_husband(self):
        set_a = list(self.get_value("set_A"))
        husband_set_a = []
        set_b = list(self.get_value("set_B"))
        wife_set_b = []
        item_h = []
        item_w = []

        for i in set_a:
            if i in self.mens_names:
                husband_set_a.append(set_a.index(i))
                item_h = random.sample(husband_set_a, k=len(husband_set_a))

        for i in set_b:
            if i in self.womens_names:
                wife_set_b.append(set_b.index(i))
                item_w = random.sample(wife_set_b, k=len(wife_set_b))

        marital_relation = set(zip(item_h, item_w))
        marital_relation -= set(self.fathers_relation)
        return list(marital_relation)

    def union_sets(self):
        return list(set(self.is_father) | set(self.is_husband))

    def intersection_sets(self):
        return list(set(self.is_father) & set(self.is_husband))

    def dif_sets(self):
        return list(set(self.is_husband) - set(self.is_father))

    def dif_uniset_sets(self):
        return list(set(self.union_sets) - set(self.is_husband))

    def get_value(self, name: str):
        return self._store.get(name)

    def set_value(self, name: str, value: set):
        self._store[name] = self._store.get(name, []) + [value]
        self.add_item_to_set.emit()

class QDLabel(QWidget):
    def __init__(self, text, circle=11, *args, **kwargs):
        super(QDLabel, self).__init__(*args, **kwargs)
        self._text = text
        self._circle = circle
        self._color = self.palette().color(self.backgroundRole())
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, v):
        self._text = v

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: QColor):
        self._color = color

    @property
    def parent_top(self):
        return self.mapToParent(QPoint(self.rect().center())).y() > self.parent().rect().center().y()

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setPen(self.palette().color(self.foregroundRole()))
        painter.setBrush(self._color)
        painter.drawEllipse(self._circle_center(self._circle), self._circle, self._circle)
        painter.setPen(self.palette().color(self.foregroundRole()))
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text)

    def _circle_center(self, circle):
        return self.rect().center() - QPoint(0, circle * 2) if self.parent_top else self.rect().center() + QPoint(0, circle  * 2)

    def sizeHint(self) -> QSize:
        fm = QFontMetrics(self.font())
        text_size = fm.boundingRect(self.text)
        return QSize(text_size.width() +self._circle * 2 + 4, text_size.height() + self._circle * 4 + 10)

    def start_y(self):
        return self.mapToParent(self.rect().topLeft()).y()

    def get_top_point(self) -> QPoint:
        return self.mapToParent(QPoint(self.rect().center().x(), self.rect().topLeft().y()))

    def get_bottom_point(self) -> QPoint:
        return self.mapToParent(QPoint(self.rect().center().x(), self.rect().bottomLeft().y()))

    def get_center(self) -> QPoint:
        return self.mapToParent(self.rect().center())

    def path_to(self, item: QDLabel) -> QLine:

        if self.start_y() > item.start_y():
            return QLine(item.get_bottom_point(), self.get_top_point())
        else:
            return QLine(item.get_top_point(), self.get_bottom_point())



def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()