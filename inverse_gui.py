
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from determinant_inverse_transpose import inverse
import numpy as np


class Inverse_GUI(QMainWindow):
    def __init__(self,matrix=np.array([[5,4,5],[4,7,6],[5,3,1]])):
        super().__init__()
        self.matrix = matrix
        self.setWindowTitle('Inverse')
        self.create_layout()
        self.setCentralWidget(self.wid)
    
    def create_layout(self):
        inverse_matrix = inverse(self.matrix)
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
            label1 = QLabel('Matriz de entrada')
            layout_matriz_entrada.addWidget(label1)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    label = QLabel(str(self.matrix[i][j]))
                    grid.addWidget(label, i, j)
            inverse_matrix = inverse(self.matrix)
            layout_matriz_entrada.addLayout(grid)
        
            label_inverse = QLabel('Inverse matrix:')
            layout_procedimiento.addWidget(label_inverse)
            for j in range(len(inverse_matrix)):
                for i in range(len(inverse_matrix[j])):
                    label = QLabel(str(inverse_matrix[j][i]))
                    grid_result.addWidget(label, j, i)
            layout_procedimiento.addLayout(grid_result)

            self.wid.setLayout(grid_grandote)
        #else:
            #self.wid = QWidget()
            #QMessageBox.warning(self, 'Error', inverse(self.matrix))
            #self.cerrar()
        
#app = QApplication(sys.argv)
#window = Inverse_GUI()
#window.show()
#app.exec()



