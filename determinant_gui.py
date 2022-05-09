import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from determinant_inverse_transpose import determinant
import numpy as np


class Determinante(QMainWindow):
    def __init__(self, matriz=[[1,1,3],[4,8,6],[7,8,9]]):
        super().__init__()
        self.matriz= np.array(matriz)
        self.setWindowTitle('Determinant')
        self.centerWindow() 
        self.create_layout()
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
        label_1=QLabel("Matrix")
        layout_matriz_entrada.addWidget(label_1)
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                label = QLabel(str(self.matriz[i][j]))
                grid.addWidget(label, i, j)
        determinante= determinant(self.matriz)
        layout_matriz_entrada.addLayout(grid)

        label_2= QLabel('|A|=', self)
        layout_procedimiento.addWidget(label_2)

        label_det=QLabel(str(determinante))
        layout_procedimiento.addWidget(label_det)


        # add labels to grid
        grid.addWidget(label_1, 0, 0)

    
        self.wid.setLayout(b_grid)