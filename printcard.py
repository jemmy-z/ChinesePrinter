from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QLabel, QHBoxLayout, QSizePolicy, QFrame)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty, QRect, Qt

class PrintCard(QLabel):
    def __init__(self, widget, start_x, start_y, card_w, card_h):
        super().__init__(widget)

        self.card_w = card_w
        self.card_h = card_h

        self.setStyleSheet("QLabel {border-image: url(./images/simple-paper.jpg) 0 0 0 0 stretch stretch}")

        self.setAlignment(Qt.AlignCenter)
        self.setGeometry(QRect(start_x, start_y, self.card_w, self.card_h))

        # font
        font = self.font()
        font.setPointSize(50)
        self.setFont(font)

    def _set_color(self, col):
        palette = self.palette()
        palette.setColor(self.foregroundRole(), col)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=_set_color)
