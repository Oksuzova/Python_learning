from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
import func
import re


class Window2(QWidget):

    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle("Window2")


class Window3(QWidget):

    def __init__(self):
        super(Window3, self).__init__()
        self.setWindowTitle("Window3")


class Window4(QWidget):

    def __init__(self):
        super(Window4, self).__init__()
        self.setWindowTitle("Window4")


class Window5(QWidget):

    def __init__(self):
        super(Window5, self).__init__()
        self.setWindowTitle("Window5")

class SetManager(QObject):

    value_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setA = {}
        self.setB = {}
        self.setC = {}
        self.setU = {}

    def set_value(self, value, set_name):
        if set_name == "setA":
            self.setA = set(re.split(r"[,:; \s]", str(value())))
            self.setA.discard("")
            set_name = f"A: {self.setA}"
        elif set_name == "setB":
            self.setB = set(re.split(r"[,:; \s]", str(value())))
            self.setB.discard("")
            set_name = f"B: {self.setB}"
        elif set_name == "setC":
            self.setC = set(re.split(r"[,:; \s]", str(value())))
            self.setB.discard("")
            set_name = f"C: {self.setC}"

        self.value_changed.emit(set_name)


    def set_range(self, value, set_name):
        if set_name == "setA":
            self.power_setA = value()
            print(self.power_setA)
        elif set_name == "setB":
            self.power_setB = value()
        elif set_name == "setC":
            self.power_setC = value()
        elif set_name == "uniset_to":
            self.len_uniset_to = value()
        elif set_name == "uniset_from":
            self.len_uniset_from = value()

        self.value_changed.emit(set_name)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Window1")
        self.set_manager = SetManager()

        self.set_horiz_layout_win_buts()
        self.set_hor_layout_row1()
        self.set_hor_layout_row2()
        self.set_hor_layout_row3()
        self.set_hor_layout_row4()
        self.set_hor_layout_row5()
        self.set_main_layout()

        self.le_a_set.textChanged.connect(self.disable_gen_but)
        self.le_b_set.textChanged.connect(self.disable_gen_but)
        self.le_c_set.textChanged.connect(self.disable_gen_but)
        self.le_uniset_to.textChanged.connect(self.disable_gen_but)
        self.le_uniset_from.textChanged.connect(self.disable_gen_but)




    def slot_set_label(self, name):
        self.set_manager.value_changed.connect(lambda x: self.label_setA.setText(x))

    def create_win_buts(self):
        self.window2 = Window2()
        self.window3 = Window3()
        self.window4 = Window4()
        self.window5 = Window5()
        self.bt_win2 = QPushButton(self.window2.windowTitle())
        self.bt_win3 = QPushButton(self.window3.windowTitle())
        self.bt_win4 = QPushButton(self.window4.windowTitle())
        self.bt_win5 = QPushButton(self.window5.windowTitle())

        self.bt_win2.clicked.connect(self.show_win2)
        self.bt_win3.clicked.connect(self.show_win3)
        self.bt_win4.clicked.connect(self.show_win4)
        self.bt_win5.clicked.connect(self.show_win5)

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
        self.rb_random.toggled.connect(self.on_clicked)

        self.rb_by_hand = QRadioButton("By hand")
        self.rb_by_hand.label_for_setA = "Enter set A"
        self.rb_by_hand.label_for_setB = "Enter set B"
        self.rb_by_hand.label_for_setC = "Enter set C"
        self.rb_by_hand.label_for_setU = ""
        self.rb_by_hand.toggled.connect(self.on_clicked)

    def set_hor_layout_row1(self):
        self.layout_row1 = QHBoxLayout()
        self.layout_row1.addWidget(QLabel(func.var()))
        self.gen_but = QPushButton("Generate")
        self.gen_but.setDisabled(True)
        self.bt_win2.clicked.connect(self.generate_sets)

        self.rb_for_create_set_labels()

        self.layout_row1.addWidget(self.rb_random)
        self.layout_row1.addWidget(self.rb_by_hand)
        self.layout_row1.addWidget(self.gen_but)

    def set_hor_layout_row2(self):
        self.layout_row2 = QHBoxLayout()

        self.label_A = QLabel("Enter power A")
        self.layout_row2.addWidget(self.label_A)

        self.le_a_set = QLineEdit()

        self.layout_row2.addWidget(QLabel(":"))
        self.layout_row2.addWidget(self.le_a_set)

        self.label_setA = QLabel("some set will be here")
        self.layout_row2.addWidget(self.label_setA)

        self.le_a_set.textEdited.connect(self.label_setA.setText)


    def set_hor_layout_row3(self):
        self.layout_row3 = QHBoxLayout()
        self.label_B = QLabel("Enter power B")
        self.layout_row3.addWidget(self.label_B)

        self.le_b_set = QLineEdit()
        self.layout_row3.addWidget(QLabel(":"))
        self.layout_row3.addWidget(self.le_b_set)

        self.label_setB = QLabel("some set will be here")
        self.layout_row3.addWidget(self.label_setB)

        self.le_b_set.textEdited.connect(self.label_setB.setText)


    def set_hor_layout_row4(self):
        self.layout_row4 = QHBoxLayout()
        self.label_C = QLabel("Enter power C")
        self.layout_row4.addWidget(self.label_C)

        self.le_c_set = QLineEdit()
        self.layout_row4.addWidget(QLabel(":"))
        self.layout_row4.addWidget(self.le_c_set)

        self.label_setC = QLabel("some set will be here")
        self.layout_row4.addWidget(self.label_setC)

        self.le_c_set.textEdited.connect(self.label_setC.setText)

    def set_hor_layout_row5(self):
        self.layout_row5 = QHBoxLayout()
        self.label_U = QLabel("Enter range from 0 to 255")
        self.layout_row5.addWidget(self.label_U)

        self.le_uniset_from = QLineEdit()
        self.layout_row5.addWidget(self.le_uniset_from)

        self.le_uniset_to = QLineEdit()
        self.layout_row5.addWidget(self.le_uniset_to)

        self.label_setU = QLabel("some set will be here")
        self.layout_row5.addWidget(self.label_setU)

        self.le_uniset_from.textEdited.connect(self.label_setU.setText)
        self.le_uniset_to.textEdited.connect(self.label_setU.setText)

    def set_main_layout(self):
        main_layout_for_win1 = QVBoxLayout()

        main_layout_for_win1.addLayout(self.layout_row1)
        main_layout_for_win1.addLayout(self.layout_row2)
        main_layout_for_win1.addLayout(self.layout_row3)
        main_layout_for_win1.addLayout(self.layout_row4)
        main_layout_for_win1.addLayout(self.layout_row5)
        main_layout_for_win1.addLayout(self.layout_win_buts)
        # main_layout_for_win1.addWidget(QPushButton("Name"))

        widget = QWidget()
        widget.setLayout(main_layout_for_win1)
        self.setCentralWidget(widget)

    def show_win2(self):
        self.window2.show()
        self.window2.setFocus()

    def show_win3(self):
        self.window3.show()
        self.window3.setFocus()

    def show_win4(self):
        self.window4.show()
        self.window4.setFocus()

    def show_win5(self):
        self.window5.show()
        self.window5.setFocus()

    def on_clicked(self):
        radioButton = self.sender()
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

    def disable_gen_but(self):
        if self.le_a_set.text() and self.le_b_set.text() and self.le_c_set.text() and \
        self.le_uniset_to.text() and self.le_uniset_from:
            self.gen_but.setDisabled(False)
        else:
            self.gen_but.setDisabled(True)
        line_edit = self.sender()
        if line_edit == self.le_a_set:
            self.set_manager.set_value(self.le_a_set.text, "setA") if self.rb_by_hand.isChecked() \
                else self.set_manager.set_range(self.le_a_set.text, "setA")
        elif line_edit == self.le_b_set:
            self.set_manager.set_value(self.le_b_set.text, "setB") if self.rb_by_hand.isChecked() \
                else self.set_manager.set_range(self.le_b_set.text, "setB")
        elif line_edit == self.le_c_set:
            self.set_manager.set_value(self.le_c_set.text, "setC") if self.rb_by_hand.isChecked() \
                else self.set_manager.set_range(self.le_c_set.text, "setC")
        elif line_edit == self.le_uniset_to:
            self.set_manager.set_value(self.le_uniset_to.text, "uniset_to") if self.rb_by_hand.isChecked() \
                else self.set_manager.set_range(self.le_uniset_to.text, "uniset_to")
        else:
            self.set_manager.set_value(self.le_uniset_from.text, "uniset_from") if self.rb_by_hand.isChecked() \
                else self.set_manager.set_range(self.le_uniset_from, "uniset_from")




    def generate_sets(self):
        pass





def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()