from subprocess import Popen, PIPE
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

rp = Popen(["randomplay", ""], stdin=PIPE, shell=False)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'RandomPlay - PYQT5'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('Skip', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        self.show()
    @pyqtSlot()
    def on_click(self):
        rp.communicate(input=b'f')

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
