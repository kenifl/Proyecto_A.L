# USE PYQT and create a 3z2 grid of buttons
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# create 6 buttons
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 grid layout'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create grid layout
        grid = QGridLayout()
        # create labels
        label1 = QLabel('Button 1', self)
        label2 = QLabel('Button 2', self)
        label3 = QLabel('Button 3', self)
        label4 = QLabel('Button 4', self)
        label5 = QLabel('Button 5', self)
        label6 = QLabel('Button 6', self)
        # add labels to grid
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 0)
        grid.addWidget(label6, 2, 1)
        # create buttons
        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)
        button3 = QPushButton('Button 3', self)
        button4 = QPushButton('Button 4', self)
        button5 = QPushButton('Button 5', self)
        button6 = QPushButton('Button 6', self)
        # add buttons to grid
        grid.addWidget(button1, 0, 2)
        grid.addWidget(button2, 0, 3)
        grid.addWidget(button3, 1, 2)
        grid.addWidget(button4, 1, 3)
        grid.addWidget(button5, 2, 2)
        grid.addWidget(button6, 2, 3)
        # set layout
        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())