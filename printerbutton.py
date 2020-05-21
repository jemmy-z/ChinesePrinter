from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QLabel, QHBoxLayout, QSizePolicy, QFrame)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty, QRect, Qt

class PrinterButton(QPushButton):

    def __init__(self, text, widget, width=50, height=20, xPos=0, yPos=0, visible=True,
                 border=None, font_size="12px", color="#000000", background_color="#ffffff",
                 background_color_pressed="#000000", border_radius="0px"):
        super().__init__(text, widget)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setVisible(visible)

        self.setStyleSheet("QPushButton { \
                                background-color:%s; \
                                border:%s; \
                                border-radius:%s; \
                                font-size:%s; \
                                color:%s } \
                            QPushButton:pressed { \
                                background-color: % s }"
                            % (background_color, border, border_radius, font_size, color,
                                background_color_pressed))

        self.move(xPos, yPos)
        self.setGeometry(QRect(xPos, yPos, width, height))


    

