# from PyQt5.QtCore    import *
# from PyQt5.QtGui     import *
# from PyQt5.QtWidgets import *
# from random import randint
#
# class playingField(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setAutoFillBackground(True)
#         appearance = self.palette()
#         appearance.setColor(QPalette.Normal, QPalette.Window, QColor("purple"))
#         self.setPalette(appearance)
#         self.lenForms = 0
#
#         timer = QTimer(self, timeout=self.changeWidget, interval=2000)
#         timer.start()
#
#     def set_layout(self, forms):                  # + forms - список маленьких виджетов
#         self.lenForms = len(forms)
#         self.layout = QHBoxLayout(self)
#         for w in forms:
#             self.layout.addWidget(w)
#
#     # тут я даже подумал заменять маленькие виджеты, продолжайте думать :)
#     def changeWidget(self):
#         f = randint(0, self.lenForms-1)
#         t = randint(0, self.lenForms-2)
#         while f == t:
#             t = randint(0, self.lenForms-2)
#
#         wFrom = self.layout.itemAt(f).widget()
#         wTo   = self.layout.itemAt(t).widget()
#         wReplace = self.layout.replaceWidget(wFrom, wTo)
#
#         if not wReplace is None:
#             n = randint(0, self.layout.count()-1)
#             self.layout.insertWidget(n, wReplace.widget())
#         else:
#             self.layout.addWidget(wTo)
#
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication([])
#
#     w = playingField()
#     w.set_layout( (QPushButton("111", w, minimumSize=QSize(70, 70), maximumSize=QSize(70, 70)),
#             QPushButton("222", w, minimumSize=QSize(70, 70), maximumSize=QSize(70, 70),
#                         styleSheet="background-color:green;"),
#             QPushButton("333", w, minimumSize=QSize(70, 70), maximumSize=QSize(70, 70),
#                         styleSheet="background-color:yellow;"),
#             QPushButton("444", w, minimumSize=QSize(70, 70), maximumSize=QSize(70, 70),
#                         styleSheet="background-color:red;"),
#             QPushButton("555", w, minimumSize=QSize(70, 70), maximumSize=QSize(70, 70),
#                         styleSheet="background-color:blue;"),) )
#
#     w.show()
#     sys.exit(app.exec_())

# from PyQt6.QtWidgets import QWidget, QApplication
# from PyQt6.QtGui import QPainter
# from PyQt6.QtCore import *
# import sys, random
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.setMinimumSize(50, 50)
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle('Points')
#         self.show()
#
#
#     def paintEvent(self, e):
#
#         qp = QPainter()
#         qp.begin(self)
#         self.drawPoints(qp)
#         qp.end()
#
#
#     def drawPoints(self, qp):
#
#         qp.setPen(Qt.GlobalColor.red)
#         size = self.size()
#
#         canvas = self.label.pixmap()
#         painter = QPainter(canvas)
#
#         painter.drawEllipse(QPoint(100, 100), 10, 10)
#
#
# def main():
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
#
#
# if __name__ == '__main__':
#     main()





from __future__ import annotations
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import math


class QDLabel(QWidget):
    def __init__(self, *args, **kwargs):
        super(QDLabel, self).__init__(*args, **kwargs)
        # self.setStyleSheet("QLabel {"
        #                    "border-radius: 4px;"
        #                    "padding: 2px 2px 2px 2px;"
        #                    "border-style: solid;"
        #                    "border-width: 1px;"
        #                    "border-color: black; "
        #                    "}")
        self.setMinimumSize(20, 20)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        # self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setToolTip(f'Size: {self.rect()}\nCenter global: {self.get_center()}')

    def paintEvent(self, a0):
        self.circle = 10
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(Qt.GlobalColor.black)
        painter.setPen(Qt.GlobalColor.black)
        painter.drawEllipse(self._circle_center(self.circle - 1), self.circle - 1, self.circle - 1)
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawEllipse(self._circle_center(self.circle), self.circle, self.circle)
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text())

    def _circle_center(self, circle):
        return self.rect().center() - QPoint(0, circle) if self.parent_top else self.rect().center() + QPoint(0, circle)

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


class SecondaryWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        f_lay = QHBoxLayout()
        s_lay = QHBoxLayout()
        self.labels_1 = []
        self.labels_2 = []

        for i in range(10):
            self.labels_1.append(QDLabel())
            f_lay.addWidget(self.labels_1[i])
            self.labels_2.append(QDLabel())
            s_lay.addWidget(self.labels_2[i])

        main_l = QVBoxLayout()
        main_l.addLayout(f_lay, 1)
        main_l.addSpacing(20)
        main_l.addStretch(4)
        main_l.addLayout(s_lay, 1)
        self.setLayout(main_l)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(Qt.GlobalColor.black)
        painter.setPen(Qt.GlobalColor.black)
        self.draw_arrow(painter, self.labels_1[1], self.labels_2[1])
        self.draw_arrow(painter, self.labels_2[2], self.labels_1[2])
        self.draw_arrow(painter, self.labels_2[3], self.labels_1[4])
        self.draw_arrow(painter, self.labels_2[3], self.labels_1[5])
        self.draw_arrow(painter, self.labels_1[5], self.labels_2[6])
        self.draw_arrow(painter, self.labels_1[5], self.labels_2[7])
        self.draw_arrow(painter, self.labels_1[8], self.labels_2[8])
        self.draw_arrow(painter, self.labels_2[8], self.labels_1[8])
        # self.draw_arrow(painter, self.labels_1[7], self.labels_1[7])
        # self.draw_arrow(painter, self.labels_1[4], self.labels_2[4])

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


class Window2(SecondaryWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Window2")

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.mw = SecondaryWindow()

        self.setCentralWidget(self.mw)

def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    app.exec()


if __name__ == '__main__':
    main()

#
#
#
#
#
#
#
#
#
#
#
# # import copy
# # import random
# # from tkinter import *
# #
# #
# # class Main:
# #     def __init__(self, main):
# #         self.tescha = None
# #         self.main = main
# #         main.title('Window 1')
# #         main.geometry('300x150')
# #         self.set_A = ['Настя', 'Зоя', 'Ірина', 'Олена', 'Марта', 'Юлія', 'Дарина', 'Оксана', 'Ольга', 'Марія',
# #                       'Софія', 'Діана', 'Аліна']
# #         self.set_B = ['Віталій', 'Дмитро', 'Артем', 'Арсен', 'Максим', 'Сергій', 'Олег', 'Петро', 'Василь', 'Федір',
# #                       'Богдан', 'Владислав', 'Віктор']
# #
# #         self.frame_main = Frame(main, bd=10)
# #         self.frame_main.pack()
# #         self.name = Label(self.frame_main, text="Катревич Олександр\nГрупа ІО-01\nНомер у списку - 11\nНомер варіанту "
# #                                                 "- 14",
# #                           font=('Arial', 16), justify=LEFT)
# #         self.name.grid(row=0, columnspan=2)
# #         self.btn_win2 = Button(self.frame_main, text='Window 2', font=('Arial', 12), command=self.window2)
# #         self.btn_win2.grid(row=1, column=0)
# #         self.btn_win3 = Button(self.frame_main, text='Window 3', font=('Arial', 12), command=self.window3)
# #         self.btn_win3.grid(row=1, column=1)
# #         self.btn_win4 = Button(self.frame_main, text='Window 4', font=('Arial', 12), command=self.window4)
# #         self.btn_win4.grid(row=1, column=2)
# #
# #     def window2(self):
# #         self.win2 = Toplevel(self.main)
# #         self.win2.title('Window 2')
# #         self.var = IntVar()
# #         self.var.set(0)
# #         self.a = set()
# #         self.b = set()
# #
# #         def add_women(event):
# #             if self.var.get() == 0:
# #                 self.a.add(self.set_A[event.widget.curselection()[0]])
# #             if self.var.get() == 1:
# #                 self.b.add(self.set_A[event.widget.curselection()[0]])
# #             self.lbl_a['text'] = 'A = {}'.format(self.a)
# #             self.lbl_b['text'] = 'B = {}'.format(self.b)
# #
# #         def add_men(event):
# #             if self.var.get() == 0:
# #                 self.a.add(self.set_B[event.widget.curselection()[0]])
# #             if self.var.get() == 1:
# #                 self.b.add(self.set_B[event.widget.curselection()[0]])
# #             self.lbl_b['text'] = 'B = {}'.format(self.b)
# #             self.lbl_a['text'] = 'A = {}'.format(self.a)
# #
# #         def save():
# #             with open('Результат.txt', 'w') as f:
# #                 f.write(str(self.a))
# #                 f.write('\n')
# #                 f.write(str(self.b))
# #                 f.write('\n')
# #             self.save_btn.config(state=DISABLED)
# #
# #         def del_set():
# #             self.a = set()
# #             self.b = set()
# #             self.lbl_a['text'] = 'A = {}'.format(self.a)
# #             self.lbl_b['text'] = 'B = {}'.format(self.b)
# #             self.save_btn.config(state=NORMAL)
# #             with open('Результат.txt', 'w') as f:
# #                 f.write('')
# #
# #         self.frm_win2 = Frame(self.win2)
# #         self.frm_win2.pack()
# #         self.choose_set = Label(self.frm_win2, text='Оберіть до якої множини додавати елементи:', font=('Garamond', 14))
# #         self.choose_set.grid(row=0, columnspan=3)
# #         self.radiobtn_A = Radiobutton(self.frm_win2, text='Множина А', font=('Arial', 12), variable=self.var,
# #                                       value=0)
# #         self.radiobtn_A.grid(row=1, column=0)
# #         self.radiobtn_B = Radiobutton(self.frm_win2, text='Множина B', font=('Arial', 12), variable=self.var,
# #                                       value=1)
# #         self.radiobtn_B.grid(row=1, column=2)
# #         self.lbl_fr1 = LabelFrame(self.frm_win2, text='Жіночі імена', font=('Arial', 12))
# #         self.lbl_fr1.grid(row=2, column=0)
# #         self.lst1 = Listbox(self.lbl_fr1, font=('Arial', 14), selectmode=EXTENDED)
# #         self.lst1.bind("<<ListboxSelect>>", add_women)
# #         self.lst1.grid(row=2, column=0)
# #         self.lbl_fr2 = LabelFrame(self.frm_win2, text='Чоловічі імена', font=('Arial', 12))
# #         self.lbl_fr2.grid(row=2, column=2)
# #         self.lst2 = Listbox(self.lbl_fr2, font=('Arial', 14), selectmode=EXTENDED)
# #         self.lst2.bind("<<ListboxSelect>>", add_men)
# #         self.lst2.grid(row=2, column=2)
# #         for i in self.set_A:
# #             self.lst1.insert(END, i)
# #         for i in self.set_B:
# #             self.lst2.insert(END, i)
# #         self.lbl_a = Label(self.frm_win2, text='A =', font=('Arial', 14))
# #         self.lbl_a.grid(row=3, columnspan=3, sticky='w')
# #         self.lbl_b = Label(self.frm_win2, text='B =', font=('Arial', 14))
# #         self.lbl_b.grid(row=4, columnspan=3, sticky='w')
# #         self.save_btn = Button(self.frm_win2, text='Зберегти множини', font=('Arial', 12), command=save)
# #         self.save_btn.grid(row=5, column=0)
# #         self.del_btn = Button(self.frm_win2, text='Очистити множини', font=('Arial', 12), command=del_set)
# #         self.del_btn.grid(row=5, column=2)
# #
# #     def window3(self):
# #
# #         self.win3 = Toplevel(self.main)
# #         self.win3.title('Window 3')
# #         self.frm_win3 = Frame(self.win3)
# #         self.frm_win3.pack()
# #         self.lbl_fr3 = LabelFrame(self.frm_win3, text='A', font=('Arial', 14))
# #         self.lbl_fr3.grid(row=0, column=0)
# #         self.lbl_fr4 = LabelFrame(self.frm_win3, text='B', font=('Arial', 14))
# #         self.lbl_fr4.grid(row=1, column=0)
# #         self.list_a = Label(self.lbl_fr3, text=self.a, font=('Arial', 14), justify=LEFT)
# #         self.list_a.grid(row=0, column=0)
# #         self.list_b = Label(self.lbl_fr4, text=self.b, font=('Arial', 14), justify=LEFT)
# #         self.list_b.grid(row=1, column=0)
# #
# #         def a_tescha_b():
# #             A = set()
# #             for i in self.a:
# #                 if i in self.set_A:
# #                     A.add(i)
# #             B = set()
# #             for i in self.b:
# #                 if i in self.set_B:
# #                     B.add(i)
# #             S = []
# #             self.tescha = list()
# #             count = 0
# #             while count < len(A) and len(B) != 0:
# #                 p = random.choice(list(A))
# #                 q = random.choice(list(B))
# #                 number_tescha = 0
# #                 numberGrand = 0
# #                 for j in range(len(self.tescha)):
# #                     if p in self.tescha[j]:
# #                         number_tescha += 1
# #                     if q in self.tescha[j]:
# #                         numberGrand += 1
# #                 if p != q and numberGrand < 3 and number_tescha < 3:
# #                     S.append([p, q])
# #                     self.tescha.append(p + q)
# #                     count += 1
# #                     B.remove(q)
# #             return S
# #
# #         def a_druzina_b():
# #             A = set()
# #             for i in self.a:
# #                 if i in self.set_A:
# #                     A.add(i)
# #             B = set()
# #             for i in self.b:
# #                 if i in self.set_B:
# #                     B.add(i)
# #             R = []
# #             self.druzina = list()
# #             while len(A) != 0 and len(B) != 0:
# #                 p = random.choice(list(A))
# #                 q = random.choice(list(B))
# #                 if p != q and p + q not in self.tescha and q not in self.druzina:
# #                     R.append([p, q])
# #                     self.druzina.append(q)
# #                     A.remove(p)
# #                     B.remove(q)
# #             return R
# #
# #         self.S = a_tescha_b()
# #         self.R = a_druzina_b()
# #
# #         aSb = Canvas(self.frm_win3, width=600, height=200)
# #         dict_SA = {}
# #         dict_SB = {}
# #         for i in range(len(self.a)):
# #             aSb.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #             aSb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #             dict_SA.update({list(self.a)[i]: [30 + i * 50, 80]})
# #         for j in range(len(self.b)):
# #             aSb.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #             aSb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #             dict_SB.update({list(self.b)[j]: [30 + j * 50, 160]})
# #         for k in self.S:
# #             aSb.create_line(dict_SA[k[0]], dict_SB[k[1]], arrow=LAST)
# #         aSb.grid(row=3, column=0, columnspan=3, rowspan=2)
# #
# #         aRb = Canvas(self.frm_win3, width=600, height=200)
# #         dict_RA = {}
# #         dict_RB = {}
# #         for i in range(len(self.a)):
# #             aRb.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #             aRb.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #             dict_RA.update({list(self.a)[i]: [30 + i * 50, 80]})
# #         for j in range(len(self.b)):
# #             aRb.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #             aRb.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #             dict_RB.update({list(self.b)[j]: [30 + j * 50, 160]})
# #         for k in self.R:
# #             aRb.create_line(dict_RA[k[0]], dict_RB[k[1]], arrow=LAST)
# #         aRb.grid(row=6, column=0, columnspan=3, rowspan=2)
# #         self.lbl_aSb = Label(self.frm_win3, text='a теща b:', font=('Arial', 14))
# #         self.lbl_aSb.grid(row=2, columnspan=3)
# #         self.lbl_aRb = Label(self.frm_win3, text='a дружина b:', font=('Arial', 14))
# #         self.lbl_aRb.grid(row=5, columnspan=3)
# #
# #     def window4(self):
# #         self.win4 = Toplevel(self.main)
# #         self.win4.title('Window 4')
# #         self.frm_win4 = Frame(self.win4, bd=10)
# #         self.frm_win4.pack()
# #         self.lbl_oper = Label(self.frm_win4, text='Операції над відношеннями', font=('Arial', 16))
# #         self.lbl_oper.grid(row=0, columnspan=4)
# #
# #         def btn1():
# #             self.canv.delete("all")
# #             self.canv.create_text(150, 20, text='R \u222A S', font='Arial 16')
# #             dict_b1 = {}
# #             dict_b2 = {}
# #             V = self.R + self.S
# #             for i in range(len(self.a)):
# #                 self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #                 self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #                 dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
# #             for j in range(len(self.b)):
# #                 self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #                 self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #                 dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
# #             for k in V:
# #                 self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)
# #
# #         def btn2():
# #             self.canv.delete("all")
# #             self.canv.create_text(150, 20, text='R \u2229 S', font='Arial 16')
# #             dict_b1 = {}
# #             dict_b2 = {}
# #             V = []
# #             for i in self.R:
# #                 if i in self.S:
# #                     V.append(i)
# #
# #             for i in range(len(self.a)):
# #                 self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #                 self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #                 dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
# #             for j in range(len(self.b)):
# #                 self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #                 self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #                 dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
# #
# #             for k in V:
# #                 if len(V) != 0:
# #                     self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)
# #
# #         def btn3():
# #             self.canv.delete("all")
# #             self.canv.create_text(150, 20, text='R \ S', font='Arial 16')
# #             dict_b1 = {}
# #             dict_b2 = {}
# #             V = copy.deepcopy(self.R)
# #             for i in V:
# #                 if i in self.S:
# #                     V.remove(i)
# #
# #             for i in range(len(self.a)):
# #                 self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #                 self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #                 dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
# #             for j in range(len(self.b)):
# #                 self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #                 self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #                 dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
# #             for k in V:
# #                 self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)
# #
# #         def btn4():
# #             self.canv.delete("all")
# #             self.canv.create_text(150, 20, text='U \ R', font='Arial 16')
# #             dict_b1 = {}
# #             dict_b2 = {}
# #             V = self.S
# #
# #             for i in range(len(self.a)):
# #                 self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #                 self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #                 dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
# #             for j in range(len(self.b)):
# #                 self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #                 self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #                 dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
# #             for k in V:
# #                 if len(V) != 0:
# #                     self.canv.create_line(dict_b1[k[0]], dict_b2[k[1]], arrow=LAST)
# #
# #         def btn5():
# #             self.canv.delete("all")
# #             self.canv.create_text(150, 20, text='S⁻¹', font='Arial 16')
# #             dict_b1 = {}
# #             dict_b2 = {}
# #             V = copy.deepcopy(self.S)
# #             for i in V:
# #                 i[0], i[1] = i[1], i[0]
# #             for i in range(len(self.a)):
# #                 self.canv.create_text(30 + i * 50, 50, text=list(self.a)[i], font='Arial 10')
# #                 self.canv.create_oval([20 + i * 50, 60], [40 + i * 50, 80], fill="white")
# #                 dict_b1.update({list(self.a)[i]: [30 + i * 50, 80]})
# #             for j in range(len(self.b)):
# #                 self.canv.create_text(30 + j * 50, 190, text=list(self.b)[j], font='Arial 10')
# #                 self.canv.create_oval([20 + j * 50, 160], [40 + j * 50, 180], fill="black")
# #                 dict_b2.update({list(self.b)[j]: [30 + j * 50, 160]})
# #             for k in V:
# #                 self.canv.create_line(dict_b2[k[0]], dict_b1[k[1]], arrow=LAST)
# #
# #         self.union_btn = Button(self.frm_win4, text='R ∪ S', width=5, command=btn1)
# #         self.union_btn.grid(row=1, column=0, sticky='w')
# #         self.intersection_btn = Button(self.frm_win4, text='R ∩ S', width=5, command=btn2)
# #         self.intersection_btn.grid(row=2, column=0, sticky='w')
# #         self.difference_btn = Button(self.frm_win4, text='R \ S', width=5, command=btn3)
# #         self.difference_btn.grid(row=3, column=0, sticky='w')
# #         self.not_btn = Button(self.frm_win4, text='U \ R', width=5, command=btn4)
# #         self.not_btn.grid(row=4, column=0, sticky='w')
# #         self.reverse_btn = Button(self.frm_win4, text='S⁻¹', width=5, command=btn5)
# #         self.reverse_btn.grid(row=5, column=0, sticky='w')
# #         self.canv = Canvas(self.frm_win4, width=600, height=250)
# #         self.canv.grid(row=1, rowspan=6, column=3)
# #
# #
# # root = Tk()
# # window = Main(root)
# # root.mainloop()
