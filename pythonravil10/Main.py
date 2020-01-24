#!/usr/bin/env python3
# coding=utf-8

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot,QTimer
from PyQt5 import uic,QtGui
import random
import math

class Example(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def frontPos(self, x, y):
        self.frontX = x
        self.frontY = y
        self.label_front.move(self.frontX - 35, self.frontY - 35)

    def initUI(self):
        self.btn1 = QPushButton("GO!", self)
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))

        self.label_back = QLabel(self)
        pixmap = QPixmap('img/t10_v1_back.png')
        self.label_back.setPixmap(pixmap)
        self.label_back.setGeometry(0, 0, 560, 560)

        self.label_front = QLabel(self)
        self.label_front.setStyleSheet("background-color:#111111;")
        self.label_front.setGeometry(0, 0, 70, 70)

        self.btn1.clicked.connect(self.btn1Click)
        self.btn1.setGeometry(10, 580, 130, 40)

        self.frontX = 0
        self.frontY = 0
        self.stepX = 0
        self.stepY = 0

        self.frontPos(40, 40)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerEvent)

        self.setGeometry(300, 300, 560, 640)
        self.setWindowTitle('zadanie 10')
        self.show()

    def timerEvent(self):
        self.frontPos(self.frontX + self.stepX, self.frontY + self.stepY)



        if self.frontY <= 80 and self.frontX >= 280:
            self.stepX = 0
            self.stepY = 5

        if self.frontY >= 120 and self.frontY < 160 and self.frontX < 320:
            self.stepX = 5
            self.stepY = 0

        if self.frontY <= 160 and self.frontX >= 440:
            self.stepX = 0
            self.stepY = 5

        if self.frontY >= 520 and self.frontX >= 400:
            self.stepX = -5
            self.stepY = 0

        if self.frontY >= 480 and self.frontX >= 320 and self.frontX <= 360:
            self.stepX = 0
            self.stepY = -5

        if self.frontY > 240 and self.frontY <= 280 and self.frontX >= 320 and self.frontX <= 400:
            self.stepX = -5
            self.stepY = 0

        if self.frontY > 240 and self.frontX <= 40:
            self.stepX = 0
            self.stepY = 5

        if self.frontY >= 520 and self.frontX <= 80:
            self.stepX = 0
            self.stepY = 0
            self.timer.stop()


    def btn1Click(self):
        self.frontPos(40, 40)
        self.stepX = 5
        self.stepY = 0
        self.timer.start(20)


if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
