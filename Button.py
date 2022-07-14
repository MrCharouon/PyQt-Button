import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 200))
        self.setWindowTitle("PyQt Button examples")

        btn1 = QPushButton('btn1', self)
        btn1.clicked.connect(self.clickMethod1)
        btn1.resize(100,32)
        btn1.move(50, 20)
        btn1.setToolTip('This is btn1')

        btn2 = QPushButton('btn2', self)
        btn2.clicked.connect(self.toastMethod2)
        btn2.resize(100,32)
        btn2.move(150, 20)
        btn2.setToolTip('This is btn2')

        btn3 = QPushButton('btn3', self)
        btn3.clicked.connect(self.toastMethod3)
        btn3.resize(100,32)
        btn3.move(250, 20)
        btn3.setToolTip('This is btn3')


    def clickMethod1(self):
        print('btn1')
    def toastMethod2(self):
        print('btn2')
    def toastMethod3(self):
        print('btn3')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
