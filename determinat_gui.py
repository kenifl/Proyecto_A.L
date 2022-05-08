import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from determinant_inverse_transpose import determinant
import numpy as np


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

    def create_layout(self):
        self.wid = QWidget()
        b_grid = QGridLayout()
        grid=QGridLayout()
        r_grid=QGridLayout()
        layout_matriz_entrada=QVBoxLayout()
        layout_procedimiento= QVBoxLayout()
        b_grid.addLayout(layout_matriz_entrada,0,0)
        b_grid.addLayout(layout_procedimiento,0,1)

        # create labels
        label_1=QLabel("Matriz")
        layout_matriz_entrada.addWidget(label_1)
        determinante= determinant()
        layout_matriz_entrada.addLayout(grid)

        label_2= QLabel('|A|=', self)
        layout_procedimiento.addWidget(label_2)
        for j in range(len(determinante)):
            for i in range (len(determinante[j])):
                label=QLabel(str(determinante[j][i]))
                r_grid.addWidget(label, i, j)
        layout_procedimiento.addLayout(r_grid)


        # add labels to grid
        grid.addWidget(label_1, 0, 0)

        # create buttons
        button_1 = QPushButton('Calcular', self)

        # add buttons to grid
        grid.addWidget(button_1, 1, 1)
    
        self.wid.setLayout(b_grid)