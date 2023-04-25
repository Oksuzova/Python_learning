from __future__ import annotations
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class SecondaryWindow(QMainWindow, QWidget):
    def __init__(self):
        super(SecondaryWindow, self).__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.set_manager = SetManager()

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

        self.listbox_set1.addItems(self.set_manager.womens_names)
        self.listbox_set2.addItems(self.set_manager.mens_names)

        self.listbox_set1.clicked.connect(self.choosen_items)
        self.listbox_set2.clicked.connect(self.choosen_items)

    def choosen_items(self):
        listbox = self.sender()
        if listbox == self.listbox_set1:
            item = self.listbox_set1.currentItem()
        else:
            item = self.listbox_set2.currentItem()
        self.add_to_choosen_set(item.text())

    def add_to_choosen_set(self, item):
        if self.rb_setA.isChecked():
            self.set_manager.set_A.add(item)
            self.lb_setA.setText(f"A: {self.set_manager.set_A}")
        else:
            self.set_manager.set_B.add(item)
            self.lb_setB.setText(f"B: {self.set_manager.set_B}")

    def save_sets(self):
        with open ("result.txt", "w") as f:
            f.write(f"{self.set_manager.set_A}\n {self.set_manager.set_B}")
        self.bt_save.setDisabled(True)
        self.bt_clear.setDisabled(True)

    def clear_sets(self):
        self.set_manager.set_A.clear()
        self.set_manager.set_B.clear()
        self.lb_setA.clear()
        self.lb_setA.setText(f"A:")
        self.lb_setB.clear()
        self.lb_setB.setText(f"B:")

    def set_main_layout(self):
        main_layout_w2 = QGridLayout()

        self.rb_setA = QRadioButton("Set A")
        self.rb_setA.setChecked(True)
        self.rb_setB = QRadioButton("Set B")

        self.lb_setA = QLabel("A: ")
        self.lb_setB = QLabel("B: ")

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

class Window4(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window4")

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Window1")

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

        self.bt_window2 = QPushButton(self.window2.windowTitle())
        self.bt_window3 = QPushButton(self.window3.windowTitle())
        self.bt_window4 = QPushButton(self.window4.windowTitle())

        self.bt_window2.clicked.connect(self.window2.show)
        self.bt_window3.clicked.connect(self.window3.show)
        self.bt_window4.clicked.connect(self.window4.show)


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

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.womens_names = ['Настя', 'Зоя', 'Ірина', 'Олена', 'Марта', 'Юлія', 'Дарина', 'Оксана', 'Ольга', 'Марія',
                      'Софія', 'Діана', 'Аліна']
        self.mens_names = ['Віталій', 'Дмитро', 'Артем', 'Арсен', 'Максим', 'Сергій', 'Олег', 'Петро', 'Василь', 'Федір',
                      'Богдан', 'Владислав', 'Віктор']

        self.set_A = set()
        self.set_B = set()


def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()