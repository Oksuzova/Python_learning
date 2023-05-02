from __future__ import annotations
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import math


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
        return QSize(self._circle * 2 + 4, text_size.height() + self._circle * 4 + 10)

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


class ArrowsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._t_lay = QHBoxLayout()
        self._b_lay = QHBoxLayout()
        self._top_labels = []
        self._bot_labels = []
        self._top_to_bot = []
        self._bot_to_top = []
        self._main_l = QVBoxLayout()
        self._main_l.addLayout(self._t_lay, 2)
        self._main_l.addSpacing(40)
        self._main_l.addStretch(4)
        self._main_l.addLayout(self._b_lay, 2)
        self.setLayout(self._main_l)

    def _splash_text(self, painter):
        if not self._bot_labels and not self._top_labels:
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, 'No data for show')
            return
        if not self._top_to_bot and not self._bot_to_top:
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, 'No relations for show')

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(self.palette().color(self.foregroundRole()))
        painter.setPen(self.palette().color(self.foregroundRole()))
        self._splash_text(painter)
        for k, v in self._top_to_bot:
            self._draw_arrow(painter, self._top_labels[k], self._bot_labels[v])
        for k, v in self._bot_to_top:
            self._draw_arrow(painter, self._bot_labels[k], self._top_labels[v])

    def _draw_arrow(self, paint: QPainter, frm: QDLabel, to: QDLabel):
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

    def set_data_sets(self, A: list, B: list):
        self.clear()
        self._top_labels = list([QDLabel(x, parent=self) for x in A])
        self._bot_labels = list([QDLabel(x, parent=self) for x in B])
        for x in self._top_labels:
            self._t_lay.addWidget(x)
        for x in self._bot_labels:
            x.color = Qt.GlobalColor.black
            self._b_lay.addWidget(x)

    def set_relations(self, rel: list[tuple]):
        pass

    def add_relation_from_top_to_bot(self, idx_a, idx_b):
        self._top_to_bot.append((idx_a, idx_b))
        self.update()

    def add_relation_from_bot_to_top(self, idx_b, idx_a):
        self._bot_to_top.append((idx_b, idx_a))
        self.update()

    def clear(self):
        self._top_labels.clear()
        self._bot_labels.clear()
        self._top_to_bot.clear()
        self._bot_to_top.clear()
        self.update()

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("ArrowsWidget example")
        self.mw = ArrowsWidget()
        self.setCentralWidget(self.mw)
        self.timer = QTimer(self)
        self.timer.singleShot(2000, self.act_1)
        self.timer.singleShot(4000, self.act_2)
        self.timer.singleShot(6000, self.act_3)

    def act_1(self):
        import string, random
        self.mw.set_data_sets(random.sample(string.ascii_lowercase, 7), random.sample(string.ascii_lowercase, 7))

    def act_2(self):
        self.mw.add_relation_from_top_to_bot(2, 5)

    def act_3(self):
        self.mw.add_relation_from_bot_to_top(4, 6)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()