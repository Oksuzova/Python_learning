from PyQt6.QtCore import QObject, pyqtSignal, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from storage import SetManager
import sets

import re


class SecondaryWindow(QWidget):
    def __init__(self):
        super(SecondaryWindow, self).__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def show(self):
        self.setFocus()
        super().show()


class Window2(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window2")


class Window3(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window3")


class Window4(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window4")


class Window5(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window5")

    def show(self):
        self.setFocus()
        super().show()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Window1")
        self.set_manager = SetManager("setA", "setB", "setC", "setU")

        self.set_horiz_layout_win_buts()
        self.set_hor_layout_row1()
        self.set_hor_layout_row2()
        self.set_hor_layout_row3()
        self.set_hor_layout_row4()
        self.set_hor_layout_row5()
        self.set_main_layout()

        self.le_a_set.textChanged.connect(self.on_form_update)
        self.le_b_set.textChanged.connect(self.on_form_update)
        self.le_c_set.textChanged.connect(self.on_form_update)
        self.le_uniset_to.textChanged.connect(self.on_form_update)
        self.le_uniset_from.textChanged.connect(self.on_form_update)

        self.set_manager.value_changed.connect(self.on_value_changed)
        self.set_manager.range_changed.connect(self.on_range_changed)

    def create_win_buts(self):
        self.window2 = Window2()
        self.window3 = Window3()
        self.window4 = Window4()
        self.window5 = Window5()
        self.bt_win2 = QPushButton(self.window2.windowTitle())
        self.bt_win3 = QPushButton(self.window3.windowTitle())
        self.bt_win4 = QPushButton(self.window4.windowTitle())
        self.bt_win5 = QPushButton(self.window5.windowTitle())

        self.bt_win2.clicked.connect(self.window2.show)
        self.bt_win3.clicked.connect(self.window3.show)
        self.bt_win4.clicked.connect(self.window4.show)
        self.bt_win5.clicked.connect(self.window5.show)

    def set_horiz_layout_win_buts(self):
        self.create_win_buts()
        self.layout_win_buts = QHBoxLayout()
        self.layout_win_buts.addWidget(self.bt_win2)
        self.layout_win_buts.addWidget(self.bt_win3)
        self.layout_win_buts.addWidget(self.bt_win4)
        self.layout_win_buts.addWidget(self.bt_win5)

    def rb_for_create_set_labels(self):
        self.rb_random = QRadioButton("Random")
        self.rb_random.setChecked(True)
        self.rb_random.label_for_setA = "Enter power A"
        self.rb_random.label_for_setB = "Enter power B"
        self.rb_random.label_for_setC = "Enter power C"
        self.rb_random.label_for_setU = "Enter range from 0 to 255"
        self.rb_random.toggled.connect(self.form_change)

        self.rb_by_hand = QRadioButton("By hand")
        self.rb_by_hand.label_for_setA = "Enter set A"
        self.rb_by_hand.label_for_setB = "Enter set B"
        self.rb_by_hand.label_for_setC = "Enter set C"
        self.rb_by_hand.label_for_setU = ""
        self.rb_by_hand.toggled.connect(self.form_change)

    def set_hor_layout_row1(self):
        self.layout_row1 = QHBoxLayout()
        self.layout_row1.addWidget(QLabel(sets.var()))
        self.gen_but = QPushButton("Generate")
        self.gen_but.setDisabled(True)
        self.gen_but.clicked.connect(self.create_set)

        self.rb_for_create_set_labels()

        self.layout_row1.addWidget(self.rb_random)
        self.layout_row1.addWidget(self.rb_by_hand)
        self.layout_row1.addWidget(self.gen_but)

    def set_hor_layout_row2(self):
        self.layout_row2 = QHBoxLayout()

        self.label_A = QLabel("Enter power A")
        self.layout_row2.addWidget(self.label_A)

        self.le_a_set = QLineEdit()
        self.le_a_set.setObjectName('setA')

        self.layout_row2.addWidget(QLabel(":"))
        self.layout_row2.addWidget(self.le_a_set)

        self.label_setA = QLabel("some set will be here")
        self.label_setA.setObjectName('setA')
        self.layout_row2.addWidget(self.label_setA)

    def set_hor_layout_row3(self):
        self.layout_row3 = QHBoxLayout()
        self.label_B = QLabel("Enter power B")
        self.layout_row3.addWidget(self.label_B)

        self.le_b_set = QLineEdit()
        self.le_b_set.setObjectName('setB')
        self.layout_row3.addWidget(QLabel(":"))
        self.layout_row3.addWidget(self.le_b_set)

        self.label_setB = QLabel("some set will be here")
        self.label_setB.setObjectName('setB')
        self.layout_row3.addWidget(self.label_setB)

    def set_hor_layout_row4(self):
        self.layout_row4 = QHBoxLayout()
        self.label_C = QLabel("Enter power C")
        self.layout_row4.addWidget(self.label_C)

        self.le_c_set = QLineEdit()
        self.le_c_set.setObjectName('setC')
        self.layout_row4.addWidget(QLabel(":"))
        self.layout_row4.addWidget(self.le_c_set)

        self.label_setC = QLabel("some set will be here")
        self.label_setC.setObjectName('setC')
        self.layout_row4.addWidget(self.label_setC)

    def set_hor_layout_row5(self):
        self.layout_row5 = QHBoxLayout()
        self.label_U = QLabel("Enter range from 0 to 255")
        self.layout_row5.addWidget(self.label_U)

        self.le_uniset_from = QLineEdit()
        self.le_uniset_from.setObjectName('setU_min')
        self.layout_row5.addWidget(self.le_uniset_from)

        self.le_uniset_to = QLineEdit()
        self.le_uniset_to.setObjectName('setU_max')
        self.layout_row5.addWidget(self.le_uniset_to)

        self.label_setU = QLabel("some set will be here")
        self.label_setU.setObjectName('setU')
        self.layout_row5.addWidget(self.label_setU)

    def set_main_layout(self):
        main_layout_for_win1 = QVBoxLayout()

        main_layout_for_win1.addLayout(self.layout_row1)
        main_layout_for_win1.addLayout(self.layout_row2)
        main_layout_for_win1.addLayout(self.layout_row3)
        main_layout_for_win1.addLayout(self.layout_row4)
        main_layout_for_win1.addLayout(self.layout_row5)
        main_layout_for_win1.addLayout(self.layout_win_buts)

        self.mw = QWidget()
        self.mw.setLayout(main_layout_for_win1)
        self.setCentralWidget(self.mw)

    # slots
    # form
    def _state_of_generate(self):
        if self.rb_by_hand.isChecked():
            if self.le_a_set.text() and \
                    self.le_b_set.text() and \
                    self.le_c_set.text():
                self.gen_but.setDisabled(False)

            else:
                self.gen_but.setDisabled(True)
        elif self.rb_random.isChecked():
            if self.le_a_set.text() and \
                    self.le_b_set.text() and \
                    self.le_c_set.text() and \
                    self.le_uniset_to.text() and \
                    self.le_uniset_from.text():
                self.gen_but.setDisabled(False)

            else:
                self.gen_but.setDisabled(True)

    def form_change(self):
        radioButton = self.sender()
        radioButton.objectName()
        self.le_a_set.clear()
        self.le_b_set.clear()
        self.le_c_set.clear()
        self.le_uniset_to.clear()
        self.le_uniset_from.clear()

        self.label_A.setText(radioButton.label_for_setA)
        self.label_B.setText(radioButton.label_for_setB)
        self.label_C.setText(radioButton.label_for_setC)
        self.label_U.setText(radioButton.label_for_setU)

        if radioButton == self.rb_by_hand:
            self.le_uniset_to.setDisabled(True)
            self.le_uniset_from.setDisabled(True)
        else:
            self.le_uniset_to.setDisabled(False)
            self.le_uniset_from.setDisabled(False)

    def on_form_update(self):
        self._state_of_generate()
        line_edit = self.sender()
        if self.rb_by_hand.isChecked() and "U" not in line_edit.objectName():
            self.set_manager.set_value_from_str(line_edit.objectName(), line_edit.text())
        elif self.rb_random.isChecked():
            self.set_manager.set_range(line_edit.objectName(), line_edit.text())

    def on_value_changed(self, v):
        # if self.rb_by_hand.isChecked():
        control = self.findChild(QLabel,  v)
        if storage_value := self.set_manager.get_value(v):
            string = f'{v}: {{{storage_value}}}'
        else:
            string = f'{v} is empty'

        control.setText(string)

    def on_range_changed(self, v):
        control = self.findChild(QLabel, v)
        control.setText("Value be seted after generate")

    def create_set(self):
        if self.rb_by_hand.isChecked():
            self.set_manager.gen_by_hand_sets()
        else:
            self.set_manager.gen_random_sets()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
