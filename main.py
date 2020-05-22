import sys
import pyautogui
import read_words

from printcard import PrintCard
from printerbutton import PrinterButton

from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QLabel, QHBoxLayout, QSizePolicy)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import (QPropertyAnimation, pyqtProperty, QRect,
                            Qt)

SCREEN_X, SCREEN_Y = pyautogui.size()
WORDS = read_words.get_txt()
INDEX = 0

class Screen(QWidget):
    card_w = 200
    card_h = 250
    card_start_x = SCREEN_X/2 - card_w/2
    card_start_y = SCREEN_Y/2 - card_h/2
    card_pause_x = SCREEN_X/2 - card_w/2
    card_pause_y = 0.4275*SCREEN_Y - card_h/2
    card_pause2_x = SCREEN_X/2 - card_w/2
    card_pause2_y = 0.4225*SCREEN_Y - card_h/2
    card_pause3_x = SCREEN_X/2 - card_w/2
    card_pause3_y = 0.4175*SCREEN_Y - card_h/2
    card_end_x = SCREEN_X/2 - card_w/2
    card_end_y = SCREEN_Y/6 - card_h/2
    speed = 1000

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initButtons()

        self.printerback = QLabel(self)
        self.printerback.setStyleSheet("QLabel {border-image: url(./images/printer-back.png) 0 0 0 0 stretch stretch}")
        self.printerback.setGeometry(QRect(SCREEN_X/2 - SCREEN_X/4.2, SCREEN_Y/2 - SCREEN_Y/2.625, SCREEN_X/2.1, SCREEN_Y/1.3125))
        self.label = PrintCard(self, self.card_start_x, self.card_start_y,
                                            self.card_w, self.card_h)
        self.label.setText(self.chooseWord())
        self.printerfront = QLabel(self)
        self.printerfront.setStyleSheet("QLabel {border-image: url(./images/printer-front.png) 0 0 0 0 stretch stretch}")
        self.printerfront.setGeometry(QRect(SCREEN_X/2 - SCREEN_X/4.2, SCREEN_Y/2 - SCREEN_Y/2.625, SCREEN_X/2.1, SCREEN_Y/1.3125))

        self.gameover = QLabel(self)
        self.gameover.setVisible(False)
        self.gameover.setText("Game Over!")
        self.gameover.setStyleSheet("font-size: 30pt")
        self.gameover.setGeometry(QRect(SCREEN_X/6 - SCREEN_X/16.8, SCREEN_Y/2,
                                        SCREEN_X/8.4, SCREEN_Y/25))
        
        self.anim = QPropertyAnimation(self.label, b"geometry")
        self.anim.setDuration(self.speed)
        self.anim.setStartValue(QRect(self.label.x(), self.label.y(), 
                                        self.label.card_w, self.label.card_h))
        self.anim.setEndValue(QRect(self.card_pause_x, self.card_pause_y, 
                                        self.label.card_w, self.label.card_h))
        
        self.anim2 = QPropertyAnimation(self.label, b"geometry")
        self.anim2.setDuration(200)
        self.anim2.setEndValue(QRect(self.card_pause2_x, self.card_pause2_y,
                                    self.label.card_w, self.label.card_h))
        
        self.anim3 = QPropertyAnimation(self.label, b"geometry")
        self.anim3.setDuration(200)
        self.anim3.setEndValue(QRect(self.card_pause3_x, self.card_pause3_y,
                                     self.label.card_w, self.label.card_h))
        
        self.animFinish = QPropertyAnimation(self.label, b"geometry")
        self.animFinish.setDuration(self.speed)
        self.animFinish.setEndValue(QRect(self.card_end_x, self.card_end_y,
                                    self.label.card_w, self.label.card_h))

        self.startbutton.clicked.connect(self.startButtonClicked)
        self.randombutton.clicked.connect(self.randomButtonClicked)
        self.printbutton.clicked.connect(self.printButtonClicked)
        self.print2button.clicked.connect(self.print2ButtonClicked)
        self.print3button.clicked.connect(self.print3ButtonClicked)
        self.finishprintbutton.clicked.connect(self.finishprintButtonClicked)
        self.reprintbutton.clicked.connect(self.reprintButtonClicked)
        self.nextbutton.clicked.connect(self.nextButtonClicked)
        self.restartbutton.clicked.connect(self.restartButtonClicked)
        self.exitbutton.clicked.connect(self.exit)
        self.animFinish.finished.connect(self.endAnimation)
        
        self.setWindowTitle("Printer")
        self.setGeometry(0, 0, SCREEN_X, SCREEN_Y)
        self.show()
    
    def initButtons(self):
        self.startbutton = PrinterButton("Start", self,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2,
                                            font_size="20pt", background_color="#77eb34",
                                            background_color_pressed="#449615", border_radius="8px")

        self.randombutton = PrinterButton("Randomize Words", self,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2 - SCREEN_Y/25 - 15,
                                            font_size="20pt", background_color="#f49eff",
                                            background_color_pressed="#a843cc", border_radius="8px")

        self.printbutton = PrinterButton("Print", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2,
                                            font_size="20pt", background_color="#77eb34",
                                            background_color_pressed="#449615", border_radius="8px")

        self.print2button = PrinterButton("Print More", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2 + SCREEN_Y/25 + 15,
                                            font_size="20pt", background_color="#77eb34",
                                            background_color_pressed="#449615", border_radius="8px")
        
        self.print3button = PrinterButton("Print More", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2 + SCREEN_Y/25 + 15,
                                            font_size="20pt", background_color="#77eb34",
                                            background_color_pressed="#449615", border_radius="8px")

        self.finishprintbutton = PrinterButton("Finish Printing", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2,
                                            font_size="20pt", background_color="#ff9717",
                                            background_color_pressed="#8f4f00", border_radius="8px")

        self.reprintbutton = PrinterButton("Print Again", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2 + SCREEN_Y/25 + 15,
                                            font_size="20pt", background_color="#77eb34",
                                            background_color_pressed="#449615", border_radius="8px")

        self.nextbutton = PrinterButton("Next Page", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2,
                                            font_size="20pt", background_color="#f49eff",
                                            background_color_pressed="#a843cc", border_radius="8px")

        self.restartbutton = PrinterButton("Restart", self, visible=False,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=SCREEN_Y/2 - SCREEN_Y/25 - 15,
                                            font_size="20pt", background_color="#30f5ff",
                                            background_color_pressed="17a6ff", border_radius="8px")

        self.exitbutton = PrinterButton("Exit", self,
                                            width=SCREEN_X/8.4, height=SCREEN_Y/25,
                                            xPos=SCREEN_X/6 - SCREEN_X/16.8, yPos=8*SCREEN_Y/10 - SCREEN_Y/50,
                                            font_size="20pt", background_color="#fc3003",
                                            background_color_pressed="a11216", border_radius="8px")

    def startButtonClicked(self):
        self.startbutton.setVisible(False)
        self.randombutton.setVisible(False)
        self.printbutton.setVisible(True)
        self.restartbutton.setVisible(True)

    def randomButtonClicked(self):
        global WORDS
        WORDS = read_words.shuffle(WORDS)
        self.restartButtonClicked()

    def printButtonClicked(self):
        self.anim.start()
        self.printbutton.setVisible(False)
        self.print2button.setVisible(True)
        self.finishprintbutton.setVisible(True)
    
    def print2ButtonClicked(self):
        if self.anim.state() == 2:
            return
        self.anim2.setStartValue(QRect(self.label.x(), self.label.y(),
                                            self.label.card_w, self.label.card_h))
        self.anim2.start()
        self.print2button.setVisible(False)
        self.print3button.setVisible(True)
    
    def print3ButtonClicked(self):
        if self.anim2.state() == 2:
            return
        self.anim3.setStartValue(QRect(self.label.x(), self.label.y(),
                                       self.label.card_w, self.label.card_h))
        self.anim3.start()
        self.print3button.setVisible(False)

    def finishprintButtonClicked(self):
        if (self.anim.state() == 2 or self.anim2.state() == 2
                or self.anim3.state() == 2):
            return
        self.animFinish.setStartValue(QRect(self.label.x(), self.label.y(),
                                       self.label.card_w, self.label.card_h))
        self.animFinish.start()
        self.printbutton.setVisible(False)
        self.print2button.setVisible(False)
        self.print3button.setVisible(False)
        self.finishprintbutton.setVisible(False)
        self.nextbutton.setVisible(True)
        self.reprintbutton.setVisible(True)

    def reprintButtonClicked(self):
        if self.animFinish.state() == 2:
            return
        global INDEX
        INDEX -= 1
        self.nextButtonClicked()

    def nextButtonClicked(self):
        if self.animFinish.state() == 2:
            return
        if INDEX >= len(WORDS):
            self.restartbutton.setVisible(True)
            self.reprintbutton.setVisible(False)
            self.nextbutton.setVisible(False)
            self.gameover.setVisible(True)
            return
        self.resetUI()

    def restartButtonClicked(self):
        if self.anim.state() == 2:
            return
        global INDEX
        INDEX = 0
        self.resetUI(main_menu=True)

    def endAnimation(self):
        self.printbutton.setVisible(False)
        self.finishprintbutton.setVisible(False)
        self.nextbutton.setVisible(True)
        self.reprintbutton.setVisible(True)

    def chooseWord(self):
        global INDEX
        word = WORDS[INDEX]
        INDEX += 1
        return word

    def resetUI(self, main_menu=False):
        if main_menu:
            self.startbutton.setVisible(True)
            self.randombutton.setVisible(True)
            self.printbutton.setVisible(False)
            self.restartbutton.setVisible(False)
        else:
            self.startbutton.setVisible(False)
            self.randombutton.setVisible(False)
            self.printbutton.setVisible(True)
            self.restartbutton.setVisible(True)
        self.gameover.setVisible(False)
        self.anim.setCurrentTime(0)
        self.animFinish.setCurrentTime(0)
        self.reprintbutton.setVisible(False)
        self.nextbutton.setVisible(False)
        self.label.setText(self.chooseWord())
        self.label.move(self.card_start_x, self.card_start_y)

    def exit(self):
        sys.exit(0)




if __name__ == "__main__":
    app = QApplication([])
    ex = Screen()
    ex.show()
    app.exec_()
