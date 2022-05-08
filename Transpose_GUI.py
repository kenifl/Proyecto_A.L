
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from determinant_inverse_transpose import transpose 
import numpy as np


class Transpose(QMainWindow):
    def __init__(self,matrix=np.array([[5,4,5],[4,7,6],[5,3,1]])):
        super().__init__()
        self.matrix = matrix
        self.setWindowTitle('Transpose')
        self.create_layout()
        self.setCentralWidget(self.wid)
    
    def create_layout(self):
        transpose_matrix = transpose(self.matrix)
        if(True):
            self.wid = QWidget()
            grid_grandote = QGridLayout()
            self.matrix = np.array(self.matrix)
            # create grid layout
            grid = QGridLayout()
            grid_result = QGridLayout()
            layout_matriz_entrada = QVBoxLayout()
            layout_procedimiento = QVBoxLayout()
            grid_grandote.addLayout(layout_matriz_entrada, 0, 0)
            grid_grandote.addLayout(layout_procedimiento, 0, 1)
        
            # create labels
            label1 = QLabel('Matrix:')
            layout_matriz_entrada.addWidget(label1)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    label = QLabel(str(self.matrix[i][j]))
                    grid.addWidget(label, j, i)
            transpose_matrix = transpose(self.matrix)
            layout_matriz_entrada.addLayout(grid)
        
            label_transpuesta = QLabel('Transpose:')
            layout_procedimiento.addWidget(label_transpuesta)
            for j in range(len(transpose_matrix)):
                for i in range(len(transpose_matrix[j])):
                    label = QLabel(str(transpose_matrix[j][i]))
                    grid_result.addWidget(label, i, j)
            layout_procedimiento.addLayout(grid_result)

            self.wid.setLayout(grid_grandote)

def cerrar(self):
    self.close()
        
# app = QApplication(sys.argv)
# window = Transpose()
# window.show()
# app.exec()



