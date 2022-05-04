# USE PYQT and create a 3z2 grid of buttons
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *

# create 6 buttons
# class Principal(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Calculadora de matrices')
#         self.centerWindow() 
#         self.initUI()
#         self.setCentralWidget(self.wid)
    
#     def centerWindow(self):
#         qtRectangle = self.frameGeometry()
#         centerPoint = self.screen().availableGeometry().center()
#         qtRectangle.moveCenter(centerPoint)
#         self.move(qtRectangle.topLeft())

#     def initUI(self):
#         self.wid = QWidget()
#         # create grid layout
#         grid = QGridLayout()

#         self.wid.setLayout(grid)
#         # create labels
#         label1 = QLabel('Button 1', self)
#         label2 = QLabel('Button 2', self)
#         label3 = QLabel('Button 3', self)
#         label4 = QLabel('Button 4', self)
#         label5 = QLabel('Button 5', self)
#         label6 = QLabel('Button 6', self)
#         # add labels to grid
#         grid.addWidget(label1, 0, 0)
#         grid.addWidget(label2, 0, 2)
#         grid.addWidget(label3, 1, 0)
#         grid.addWidget(label4, 1, 2)
#         grid.addWidget(label5, 2, 0)
#         grid.addWidget(label6, 2, 2)
#         # create buttons
#         button1 = QPushButton('Button 1', self)
#         button2 = QPushButton('Button 2', self)
#         button3 = QPushButton('Button 3', self)
#         button4 = QPushButton('Button 4', self)
#         button5 = QPushButton('Button 5', self)
#         button6 = QPushButton('Button 6', self)
#         # add buttons to grid
#         grid.addWidget(button1, 0, 1)
#         grid.addWidget(button2, 0, 3)
#         grid.addWidget(button3, 1, 1)
#         grid.addWidget(button4, 1, 3)
#         grid.addWidget(button5, 2, 1)
#         grid.addWidget(button6, 2, 3)

class Determinante(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Determinante de una matriz')
        self.centerWindow() 
        self.initUI()
        self.setCentralWidget(self.wid)

    def centerWindow(self):
        qtRectangle = self.frameGeometry()
        centerPoint = self.screen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def initUI(self):
        self.wid = QWidget()
        # create grid layout
        grid = QGridLayout()

        self.wid.setLayout(grid)
        # create labels
        label_1 = QLabel('|A|=', self)

        # add labels to grid
        grid.addWidget(label_1, 0, 0)

        # create buttons
        button_1 = QPushButton('Calcular', self)
        button_2 = QPushButton('Regresar', self)
        button_2.clicked.connect(self.regresar)

        # add buttons to grid
        grid.addWidget(button_1, 1, 1)
        grid.addWidget(button_2, 1, 3)

    def regresar (self):
        window.show()
        self.close()

        
class Producto_escalar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Determinante de una matriz')
        self.centerWindow() 
        self.initUI()
        self.setCentralWidget(self.wid)

    def centerWindow(self):
        qtRectangle = self.frameGeometry()
        centerPoint = self.screen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def initUI(self):
        self.wid = QWidget()
        # create grid layout
        grid = QGridLayout()

        self.wid.setLayout(grid)
        # create labels
        label_1 = QLabel('|A|=', self)

        # add labels to grid
        grid.addWidget(label_1, 0, 0)

        # create buttons
        button_1 = QPushButton('Calcular', self)
        button_2 = QPushButton('Regresar', self)
        button_2.clicked.connect(self.regresar)

        # add buttons to grid
        grid.addWidget(button_1, 1, 1)
        grid.addWidget(button_2, 1, 3)

    def regresar (self):
        window.show()
        self.close()



app = QApplication(sys.argv)
window = Determinante()
window.show()
app.exec()

