from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QButtonGroup, QLabel, QVBoxLayout, QAbstractButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.rb_ok = QRadioButton('Ключ нужен')
        self.rb_fail = QRadioButton('Ключ не нужен')
        self.rb_foo = QRadioButton('Ключ, возможно, будет нужен')

        self._button_group = QButtonGroup()
        self._button_group.addButton(self.rb_ok)
        self._button_group.addButton(self.rb_fail)
        self._button_group.addButton(self.rb_foo)
        self._button_group.buttonClicked.connect(self._radio_button_select)

        self.label_result = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.rb_ok)
        layout.addWidget(self.rb_fail)
        layout.addWidget(self.rb_foo)
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def _radio_button_select(self, button: QAbstractButton):
        if self.rb_ok.isChecked():
            self.label_result.setText('Ключ НУЖЕН!')
        else:
            self.label_result.setText('Ключ... а хз!. -> ' + button.text())


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()

# from PyQt5.QtWidgets import *
# import sys
#
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#
#         radiobutton = QRadioButton("Australia")
#         radiobutton.setChecked(True)
#         radiobutton.country = "Australia"
#         radiobutton.toggled.connect(self.onClicked)
#         layout.addWidget(radiobutton, 0, 0)
#
#         radiobutton = QRadioButton("China")
#         radiobutton.country = "China"
#         radiobutton.toggled.connect(self.onClicked)
#         layout.addWidget(radiobutton, 0, 1)
#
#         radiobutton = QRadioButton("Japan")
#         radiobutton.country = "Japan"
#         radiobutton.toggled.connect(self.onClicked)
#         layout.addWidget(radiobutton, 0, 2)
#
#     def onClicked(self):
#         radioButton = self.sender()
#         if radioButton.isChecked():
#             print("Country is %s" % (radioButton.country))
#
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())



# import sys
# from random import randint
#
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )
#
#
# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent,
#     it will appear as a free-floating window.
#     """
#
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.window1 = AnotherWindow()
#         self.window2 = AnotherWindow()
#
#         l = QVBoxLayout()
#         button1 = QPushButton("Push for Window 1")
#         button1.clicked.connect(
#             lambda checked: self.toggle_window(self.window1)
#         )
#         l.addWidget(button1)
#
#         button2 = QPushButton("Push for Window 2")
#         button2.clicked.connect(
#             lambda checked: self.toggle_window(self.window2)
#         )
#         l.addWidget(button2)
#
#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)
#
#     def toggle_window(self, window):
#         if window.isVisible():
#             window.hide()
#
#         else:
#             window.show()
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()