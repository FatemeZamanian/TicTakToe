# This Python file uses the following encoding: utf-8
import sys
import os
from functools import partial

from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import random


class TicTokToe(QWidget):
    def __init__(self):
        super(TicTokToe, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ar_btn = [[None for i in range(3)]for j in range(3) ]
        self.ar_btn[0][0] = self.ui.btn00
        self.ar_btn[0][1] = self.ui.btn01
        self.ar_btn[0][2] = self.ui.btn02
        self.ar_btn[1][0] = self.ui.btn10
        self.ar_btn[1][1] = self.ui.btn11
        self.ar_btn[1][2] = self.ui.btn12
        self.ar_btn[2][0] = self.ui.btn20
        self.ar_btn[2][1] = self.ui.btn21
        self.ar_btn[2][2] = self.ui.btn22
        self.ui.show()

        self.ui.btn_new.clicked.connect(partial(self.new))
        for i in range(3):
            for j in range(3):
                self.ar_btn[i][j].clicked.connect(partial(self.play, i, j))
                self.ar_btn[i][j].clicked.connect(partial(self.cmptr_play))

        self.player = 1
        self.pl1_win=0
        self.pl2_win=0
        self.draw=0
        self.pl=''

    def play(self, i=0, j=0):

        if self.ar_btn[i][j].text()=='':
            if self.player==1:
                self.ar_btn[i][j].setText('X')
                self.ar_btn[i][j].setStyleSheet('color:red;background-color:#FFCCCC')
                self.player=2

            elif self.player==2:
                if self.ui.rbtn_pvp.isChecked():
                    self.ar_btn[i][j].setText('O')
                    self.ar_btn[i][j].setStyleSheet('color:blue;background-color:#CCFFFF')
                    self.player=1
        self.check()

    def cmptr_play(self):
        if self.ui.rbtn_pvc.isChecked() and self.player==2:
            while True:
                r = random.randint(0, 2)
                c = random.randint(0, 2)
                if self.ar_btn[r][c].text() == '':
                    self.ar_btn[r][c].setText('O')
                    self.ar_btn[r][c].setStyleSheet('color:blue;background-color:#CCFFFF')
                    self.player = 1
                    break
        self.check()

    def check(self):
        for i in range(3):
            if self.ar_btn[i][0].text() == self.ar_btn[i][1].text() == self.ar_btn[i][2].text() and self.ar_btn[i][0].text() != '':
                self.pl = self.ar_btn[i][0].text()
            elif self.ar_btn[0][i].text() == self.ar_btn[1][i].text() == self.ar_btn[2][i].text() and self.ar_btn[0][i].text() != '':
                self.pl = self.ar_btn[0][i].text()
        if self.ar_btn[0][0].text() == self.ar_btn[1][1].text() == self.ar_btn[2][2].text() and self.ar_btn[0][0].text() != '':
            self.pl = self.ar_btn[0][0].text()
        elif self.ar_btn[0][2].text() == self.ar_btn[1][1].text() == self.ar_btn[2][0].text() and self.ar_btn[0][2].text() != '':
            self.pl = self.ar_btn[0][2].text()
        if all(self.ar_btn[0][i].text()!='' for i in range(3)) and all(self.ar_btn[i][0].text()!='' for i in range(3)):
            self.draw+=1
            self.ui.lbl_d.setText(str(self.draw))
            msg = QMessageBox()
            msg.setText('no body win...')
            msg.exec()
            self.pl='non'

        if self.pl == 'X':
            self.pl1_win+=1
            self.ui.lbl_1.setText(str(self.pl1_win))
            msg=QMessageBox()
            msg.setText('player1 wins...')

            msg.exec()

        elif self.pl == 'O':
            self.pl2_win+=1
            self.ui.lbl_2.setText(str(self.pl2_win))
            msg = QMessageBox()
            msg.setText('player2 wins...')
            msg.exec()

        if self.pl !='':
            self.ui.lbl_1.setText(str(self.pl1_win))
            self.ui.lbl_2.setText(str(self.pl2_win))
            self.pl=''
            for i in range(3):
                for j in range(3):
                    self.ar_btn[i][j].setText('')
                    self.ar_btn[i][j].setStyleSheet('border-style: outset;border-width:3px;border-color: beige;')

    def new(self):
        self.player = 1
        self.pl1_win = 0
        self.pl2_win = 0
        self.draw = 0
        self.pl = ''
        self.ui.lbl_1.setText(str(self.pl1_win))
        self.ui.lbl_2.setText(str(self.pl2_win))
        self.ui.lbl_d.setText(str(self.draw))
        for i in range(3):
            for j in range(3):
                self.ar_btn[i][j].setText('')
                self.ar_btn[i][j].setStyleSheet('border-style: outset;border-width:3px;border-color: beige;')



if __name__ == "__main__":

    app = QApplication([])
    widget = TicTokToe()
    sys.exit(app.exec())
