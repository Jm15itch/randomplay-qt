from subprocess import Popen, PIPE
import os
import sys
import select
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.QtGui import QPalette

#rp = Popen(["randomplay", ""], shell=False)

global rp
rp = "NULL"

try:

    class MainWindow(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)

            self.setFixedSize(QSize(250, 350))
            self.setWindowTitle("QT-RandomPlay")

            self.SongLabel = QLabel(self)

            self.SongLabel.setText("No Song Selected")
            self.SongLabel.setAutoFillBackground(True)
            palette = QPalette()
            palette.setColor(QPalette.Window,Qt.black)
            self.SongLabel.setPalette(palette)
            self.SongLabel.setAlignment(Qt.AlignCenter)
            self.SongLabel.move(50, 275)
            self.SongLabel.resize(150,32)

            pybutton = QPushButton('Start RandomPlay', self)
            pybutton.clicked.connect(self.startRandomPlay)
            pybutton.resize(150,32)
            pybutton.move(50, 30)

            pybutton = QPushButton('Toggle Sound', self)
            pybutton.clicked.connect(self.ToggleSound)
            pybutton.resize(150,32)
            pybutton.move(50, 80)

            pybutton = QPushButton('Skip', self)
            pybutton.clicked.connect(self.SkipSong)
            pybutton.resize(75,32)
            pybutton.move(150, 150)

            pybutton = QPushButton('Rewind', self)
            pybutton.clicked.connect(self.RewindSong)
            pybutton.resize(75,32)
            pybutton.move(25, 150)

            pybutton = QPushButton('Like!', self)
            pybutton.clicked.connect(self.LikeSong)
            pybutton.resize(75,32)
            pybutton.move(150, 200)

            pybutton = QPushButton('Dislike', self)
            pybutton.clicked.connect(self.DislikeSong)
            pybutton.resize(75,32)
            pybutton.move(25, 200)

        def startRandomPlay(self):
            global rp
            Directory = "NULL"

            while (not os.path.exists(Directory)):
                Directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                print("Select directory: " + Directory)

            rp = Popen(["randomplay", Directory], stdin=PIPE, stdout=PIPE, shell=False, bufsize=1, universal_newlines=True, encoding="latin-1")
            self.RefreshSongDisplay()

        def RefreshSongDisplay(self):
            global rp
            poll_obj = select.poll()
            poll_obj.register(rp.stdout, select.POLLIN)
            line = []
            while True:
                poll_result = poll_obj.poll(0)
                if poll_result:
                    line.append( rp.stdout.readline() )
                else:
                    break;
            matching = [s for s in line if "TITLE" in s][0]
            self.SongLabel.setText(matching)
            return

        def ToggleSound(self):
            global rp
            rp.stdin.write('p')
            rp.stdin.flush()

        def SkipSong(self):
            global rp
            rp.stdin.write('f')
            rp.stdin.flush()
            self.RefreshSongDisplay()

        def RewindSong(self):
            global rp
            rp.stdin.write('b')
            rp.stdin.flush()
            self.RefreshSongDisplay()

        def LikeSong(self):
            global rp
            rp.stdin.write('+')
            rp.stdin.flush()

        def DislikeSong(self):
            global rp
            rp.stdin.write('-')
            rp.stdin.flush()


    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        app.exec_()
        rp.stdin.write('q')
        rp.stdin.flush()
        sys.exit(1)


except KeyboardInterrupt:
    rp.stdin.write('q')
    rp.stdin.flush()
    sys.exit(1)
