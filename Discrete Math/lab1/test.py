from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("QTextEdit")
                self.resize(300,270)

                self.textEdit = QTextEdit()
                self.btnPress1 = QPushButton("Button 1")
                self.btnPress2 = QPushButton("Button 2")

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                layout.addWidget(self.btnPress1)
                layout.addWidget(self.btnPress2)
                self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)
                self.btnPress2.clicked.connect(self.btnPress2_Clicked)

        def btnPress1_Clicked(self):
                self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

        def btnPress2_Clicked(self):
                self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())




# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout
# from PyQt6.QtCore import Qt
#
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.setWindowTitle('Login Form')
#
#         # set the grid layout
#         layout = QGridLayout()
#         self.setLayout(layout)
#
#         # username
#         layout.addWidget(QLabel('Username:'), 0, 0)
#         layout.addWidget(QLineEdit(), 0, 1)
#
#         # password
#         layout.addWidget(QLabel('Password:'), 1, 0)
#         layout.addWidget(QLineEdit(echoMode=QLineEdit.EchoMode.Password), 1, 1)
#
#         # buttons
#         layout.addWidget(QPushButton('Log in'), 2, 0,
#                          alignment=Qt.AlignmentFlag.AlignRight)
#         layout.addWidget(QPushButton('Close'), 2, 1,
#                          alignment=Qt.AlignmentFlag.AlignRight)
#
#         # show the window
#         self.show()

        # self.window2.ready_sets[v].setText(string)
        # self.sets_for_w2()

        # def sets_for_w2(self):
        #     dif_setAB = sets.difference_set(self.set_manager.get_value('setA'), self.set_manager.get_value('setB'))
        #     self.step1 = QLabel(
        #         f"D = A ∩ (A / (A / B) ∪ C = {self.set_manager.get_value('setA')} ∩ ({self.set_manager.get_value('setA')}\
        #          / ({self.set_manager.get_value('setA')} / {self.set_manager.get_value('setB')}) \
        #          ∪ {self.set_manager.get_value('setC')}")
        #     self.step2 = QLabel(
        #         f"D = A ∩ (A / (res) ∪ C = {self.set_manager.get_value('setA')} ∩ ({self.set_manager.get_value('setA')}\
        #                  / ({dif_setAB}) ∪ {self.set_manager.get_value('setC')}")
        #     self.step3 = QLabel(
        #         f"D = A ∩ (res) ∪ C = {self.set_manager.get_value('setA')} ∩ ({self.window2.ready_setA}\
        #                  / ({self.window2.ready_setA} / {self.window2.ready_setB}) ∪ {self.window2.ready_setC}")
        #     self.step4 = QLabel(
        #         f"D = (res) ∪ C = {self.set_manager.get_value('setA')} ∩ ({self.window2.ready_setA}\
        #                  / ({self.window2.ready_setA} / {self.window2.ready_setB}) ∪ {self.window2.ready_setC}")
        #
        #
        #     self.window2.main_layout_for_win2.addWidget(self.step1, 10, 0)
        #     self.window2.main_layout_for_win2.addWidget(self.step2, 11, 0)

#
#         self.ready_sets = {
#             "setA": self.ready_setA,
#             "setB": self.ready_setB,
#             "setC": self.ready_setC,
#             "setU": self.ready_setU,
#         }
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())