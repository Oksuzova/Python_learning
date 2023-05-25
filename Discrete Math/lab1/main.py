from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from storage import SetManager
import sets


class SecondaryWindow(QMainWindow, QWidget):
    def __init__(self):
        super(SecondaryWindow, self).__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.label_ready_setA = QLabel()
        self.label_ready_setB = QLabel()
        self.label_ready_setC = QLabel()
        self.label_ready_setU = QLabel()

        self.label_ready_setX = QLabel()
        self.label_ready_setY = QLabel()

        self.bt_save = QPushButton("Save")
        self.bt_save.setDisabled(True)
        self.bt_step = QPushButton("Step")


        self.step = 0

        self.created_sets = {
            "setA": 0,
            "setB": 0,
            "setC": 0,
            "setU": 0,
        }

        self.ready_sets = {
            "setA": self.label_ready_setA,
            "setB": self.label_ready_setB,
            "setC": self.label_ready_setC,
            "setU": self.label_ready_setU,
            "setX": self.label_ready_setX,
            "setY": self.label_ready_setY,
        }

    def set_storage(self, man: SetManager):
        self.db = man
        self.db.value_changed.connect(self.value_updated)

    def value_updated(self, n):
        value = self.db.get_value(n)
        for _ in self.ready_sets:
            self.ready_sets[n].setText(f"{n}: {value}")
            self.created_sets[n] = value
        self.label_ready_setX.setText(f"X: {self.db.get_value('setA')}")
        self.label_ready_setY.setText(f"Y: {self.db.get_value('setB')}")


    def show(self):
        self.setFocus()
        super().show()


class Window2(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window2")
        self.setFixedSize(500, 300)

        self.bt_step.clicked.connect(self.next_step)
        self.bt_save.clicked.connect(self.save_res)

        self.set_main_layout()

    def next_step(self):
        res1 = sets.difference_set(self.created_sets['setA'], self.created_sets['setB'])
        res2 = sets.difference_set(self.created_sets['setA'], res1)
        res3 = sets.intersection_set(self.created_sets['setA'], res2)
        self.res4 = sets.union_set(res3, self.created_sets['setC'])
        steps = [
            f"STEP 1: D = A ∩ (A / (A / B) ∪ C = {self.created_sets['setA']} ∩ ({self.created_sets['setA']} / ({self.created_sets['setA']} / {self.created_sets['setB']}) ∪ {self.created_sets['setC']}\n",
            f"STEP 2: D = A ∩ (A / (res) ∪ C = {self.created_sets['setA']} ∩ ({self.created_sets['setA']} / {res1}) ∪ {self.created_sets['setC']}\n",
            f"STEP 3: D = A ∩ (res) ∪ C = {self.created_sets['setA']} ∩ {res2} ∪ {self.created_sets['setC']}\n",
            f"STEP 4: D = (res) ∪ C = {res3} ∪ {self.created_sets['setC']}\n",
            f"STEP 5: D = {self.res4}\n",
            f"Calculations completed",
        ]
        self.textEdit.insertPlainText(steps[self.step])
        self.step += 1
        if self.step == 6:
            self.bt_step.setDisabled(True)
            self.bt_save.setDisabled(False)

    def save_res(self):
        with open("result.txt", "a") as f:
            f.write(f"setD1: {self.res4}\n")
        self.bt_save.setDisabled(True)

    def set_main_layout(self):
        self.main_layout_for_win2 = QGridLayout()
        self.setLayout(self.main_layout_for_win2)

        self.main_layout_for_win2.addWidget(QLabel("Specified expression: D = A ∩ (A / (A / B) ∪ C"), 0, 0, 1, 2)
        self.main_layout_for_win2.addWidget(self.label_ready_setA, 1, 0)
        self.main_layout_for_win2.addWidget(self.label_ready_setB, 2, 0)
        self.main_layout_for_win2.addWidget(self.label_ready_setC, 3, 0)
        self.main_layout_for_win2.addWidget(self.label_ready_setU, 4, 0)

        self.main_layout_for_win2.addWidget(self.bt_save, 1, 1, 2, 2)
        self.main_layout_for_win2.addWidget(self.bt_step, 3, 1, 2, 2)

        self.main_layout_for_win2.addWidget(QLabel("Calculations:"), 5, 1, 1, 4)

        self.textEdit = QPlainTextEdit()
        self.textEdit.setDisabled(True)
        self.main_layout_for_win2.addWidget(self.textEdit, 6, 0, 7, 4)

        self.w2 = QWidget()
        self.w2.setLayout(self.main_layout_for_win2)
        self.setCentralWidget(self.w2)

class Window3(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window3")
        self.setFixedSize(500, 300)

        self.bt_save_w3 = QPushButton("Save")
        self.bt_save_w3.setDisabled(True)
        self.bt_step_w3 = QPushButton("Step")
        self.bt_step_w3.clicked.connect(self.next_step_w3)
        self.bt_save_w3.clicked.connect(self.save_res_w3)

        self.set_main_layout()

    def save_res_w3(self):
        with open("result.txt", "a") as f:
            f.write(f"setD2: {self.res2}\n")
        self.bt_save_w3.setDisabled(True)

    def next_step_w3(self):
        res1 = sets.intersection_set(self.created_sets['setA'], self.created_sets['setB'])
        self.res2 = sets.union_set(res1, self.created_sets['setC'])
        steps = [
            f"STEP 1: D = A ∩ B ∪ C = {self.created_sets['setA']} ∩ {self.created_sets['setB']}) ∪ {self.created_sets['setC']}\n",
            f"STEP 2: D = (res) ∪ C = {res1} ∪ {self.created_sets['setC']}\n",
            f"STEP 3: D = {self.res2}\n",
            f"Calculations completed",
        ]
        self.textEdit.insertPlainText(steps[self.step])
        self.step += 1
        if self.step == 4:
            self.bt_step_w3.setDisabled(True)
            self.bt_save_w3.setDisabled(False)

    def set_main_layout(self):
        self.main_layout_for_win3 = QGridLayout()
        self.setLayout(self.main_layout_for_win3)

        self.main_layout_for_win3.addWidget(QLabel("Specified expression: D = A ∩ (A / (A / B) ∪ C"), 0, 0, 1, 2)
        self.main_layout_for_win3.addWidget(self.label_ready_setA, 1, 0)
        self.main_layout_for_win3.addWidget(self.label_ready_setB, 2, 0)

        self.main_layout_for_win3.addWidget(self.bt_save_w3, 1, 1, 2, 2)
        self.main_layout_for_win3.addWidget(self.bt_step_w3, 3, 1, 2, 2)

        self.main_layout_for_win3.addWidget(QLabel("Calculations:"), 5, 1, 1, 4)

        self.textEdit = QPlainTextEdit()
        self.textEdit.setDisabled(True)
        self.main_layout_for_win3.addWidget(self.textEdit, 6, 0, 7, 4)

        self.w3 = QWidget()
        self.w3.setLayout(self.main_layout_for_win3)
        self.setCentralWidget(self.w3)


class Window4(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window4")
        self.set_manager = SetManager()

        self.bt_calculate_w4 = QPushButton("Calculate")
        self.bt_calculate_w4.clicked.connect(self.calculate)
        self.bt_compare_w4 = QPushButton("Compare")
        self.bt_compare_w4.clicked.connect(self.compare)
        self.bt_compare_w4.setDisabled(True)

        self.bt_save_w4 = QPushButton("Save")
        self.bt_save_w4.clicked.connect(self.save_res_w4)

        self.set_main_layout()

    def save_res_w4(self):
        with open("result.txt", "a") as f:
            f.write(f"setZ1: {self.res1}\nsetZ2: {self.res2}")
        self.bt_save_w4.setDisabled(True)

    def calculate(self):
        self.res1 = sets.intersection_set(self.created_sets['setA'], self.created_sets['setB'])
        self.res2 = self.created_sets['setA'] & self.created_sets['setB']
        self.label_author_alg = QLabel(f"Z = X ∩ Y = {self.created_sets['setA']} ∩ {self.created_sets['setB']} = {self.res1}")
        self.label_built_alg = QLabel(f"Z = X ∩ Y = {self.created_sets['setA']} ∩ {self.created_sets['setB']} = {self.res2}")

        self.main_layout_for_win4.addWidget(self.label_author_alg, 6, 0, 1, 2)
        self.main_layout_for_win4.addWidget(self.label_built_alg, 7, 0, 1, 2)

        self.bt_compare_w4.setDisabled(False)
        self.bt_calculate_w4.setDisabled(True)

    def compare(self):
        self.label_compare_alg = QLabel(f"{self.res1} = {self.res2}")
        self.main_layout_for_win4.addWidget(self.label_compare_alg, 8, 0)
        self.bt_compare_w4.setDisabled(True)
        self.add_save_bt()

    def add_save_bt(self):
        self.bt_save_w4 = QPushButton("Save")
        self.bt_save_w4.clicked.connect(self.save_res_w4)
        self.main_layout_for_win4.addWidget(self.bt_save_w4, 8, 2)

    def set_main_layout(self):
        self.main_layout_for_win4 = QGridLayout()
        self.setLayout(self.main_layout_for_win4)

        self.main_layout_for_win4.addWidget(QLabel("Specified expression: Z = X ∩ Y, X = A, Y = B"), 0, 0, 1, 2)
        self.main_layout_for_win4.addWidget(self.label_ready_setX, 1, 0)
        self.main_layout_for_win4.addWidget(self.label_ready_setY, 2, 0)

        self.main_layout_for_win4.addWidget(self.bt_calculate_w4, 1, 1)
        self.main_layout_for_win4.addWidget(self.bt_compare_w4, 3, 1)

        self.main_layout_for_win4.addWidget(QLabel("Calculations:"), 5, 1, 1, 4)

        self.w4 = QWidget()
        self.w4.setLayout(self.main_layout_for_win4)
        self.setCentralWidget(self.w4)


class Window5(SecondaryWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window5")
        self.set_manager = SetManager()

        self.set_main_layout()

    def create_bts(self):
        self.bt_read_d1 = QPushButton("Read Specified Set D1:")
        self.bt_read_d2 = QPushButton("Read Simplified Set D2:")
        self.bt_read_z1 = QPushButton("Read Author Algorithm Z1:")
        self.bt_read_z2 = QPushButton("Read Built-In Algorithm Z2:")

    def reading_d1(self):
        with open("result.txt", "r") as f:
            for line in f:
                if line.startswith("setD1"):
                    self.main_layout_for_win5.addWidget(QLabel(line.rstrip()), 0, 1)

    def reading_d2(self):
        with open("result.txt", "r") as f:
            for line in f:
                if line.startswith("setD2"):
                    self.main_layout_for_win5.addWidget(QLabel(line.rstrip()), 1, 1)

    def reading_z1(self):
        with open("result.txt", "r") as f:
            for line in f:
                if line.startswith("setZ1"):
                    self.main_layout_for_win5.addWidget(QLabel(line.rstrip()), 2, 1)

    def reading_z2(self):
        with open("result.txt", "r") as f:
            for line in f:
                if line.startswith("setZ2"):
                    self.main_layout_for_win5.addWidget(QLabel(line.rstrip()), 3, 1)
            self.main_layout_for_win5.addWidget(QLabel("D1 = D2, Z1 = Z2"), 4, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

    def set_main_layout(self):
        self.main_layout_for_win5 = QGridLayout()
        self.setLayout(self.main_layout_for_win5)
        self.create_bts()

        self.main_layout_for_win5.addWidget((self.bt_read_d1), 0, 0)
        self.bt_read_d1.clicked.connect(self.reading_d1)

        self.main_layout_for_win5.addWidget((self.bt_read_d2), 1, 0)
        self.bt_read_d2.clicked.connect(self.reading_d2)

        self.main_layout_for_win5.addWidget((self.bt_read_z1), 2, 0)
        self.bt_read_z1.clicked.connect(self.reading_z1)

        self.main_layout_for_win5.addWidget((self.bt_read_z2), 3, 0)
        self.bt_read_z2.clicked.connect(self.reading_z2)

        self.w5 = QWidget()
        self.w5.setLayout(self.main_layout_for_win5)
        self.setCentralWidget(self.w5)


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

        self.window2.set_storage(self.set_manager)
        self.window3.set_storage(self.set_manager)
        self.window4.set_storage(self.set_manager)



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

        self.label_setA = QLabel()
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

        self.label_setB = QLabel()
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

        self.label_setC = QLabel()
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

        self.label_setU = QLabel()
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
        self.clear_forms()

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


    def clear_forms(self):
        self.label_setA.clear()
        self.label_setB.clear()
        self.label_setC.clear()
        self.label_setU.clear()

        self.le_a_set.clear()
        self.le_b_set.clear()
        self.le_c_set.clear()
        self.le_uniset_to.clear()
        self.le_uniset_from.clear()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
