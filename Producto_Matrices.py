import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from determinant_inverse_transpose import inverse
import numpy as np


class ProductoM_GUI(QMainWindow):
    def __init__(self,matrix=np.array([[5,4,5],[4,7,6],[5,3,1]])):
        super().__init__()
        self.matrix = matrix
        self.setWindowTitle('Matrix multiplication')
        self.create_layout()
        self.setCentralWidget(self.wid)
    
    def create_layout(self):
        if(True):
            self.wid = QWidget()
            grid_grandote = QGridLayout()
            self.matrix = np.array(self.matrix)
            self.wid.setLayout(grid_grandote)
            # create grid layout
            grid = QGridLayout()
            grid_result = QGridLayout()
            layout_matriz_entrada = QVBoxLayout()
            layout_procedimiento = QVBoxLayout()
            layout_resultado = QVBoxLayout()
            layout_line_button = QHBoxLayout()
            layout_procedimiento.addLayout(layout_line_button)
            grid_grandote.addLayout(layout_matriz_entrada, 0, 0)
            grid_grandote.addLayout(layout_resultado, 0, 2)
            grid_grandote.addLayout(layout_procedimiento, 0, 3)
            #procedimiento
            label_procedimiento = QLabel('Number of columns:')
            layout_line_button.addWidget(label_procedimiento)
            self.num_columnas = QLineEdit()
            layout_line_button.addWidget(self.num_columnas)
            self.boton_procedimiento = QPushButton('Update')
            layout_line_button.addWidget(self.boton_procedimiento)
            layout_procedimiento.addWidget(self.boton_procedimiento)
            self.tabla = QTableWidget()
            self.tabla.setRowCount(self.matrix.shape[0])
            self.tabla.setColumnCount(1)
            self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            layout_procedimiento.addWidget(self.tabla)

            # create labels
            label1 = QLabel('X')
            grid_grandote.addWidget(label1, 0, 1)

            # create labels
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    label = QLabel(str(self.matrix[i][j]))
                    grid.addWidget(label, i, j)
            layout_matriz_entrada.addLayout(grid)

app = QApplication(sys.argv)
window = ProductoM_GUI()
window.show()
app.exec()