from unittest import result
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from Scalar_Product import scalar_product
import numpy as np

class ProductoS_GUI(QMainWindow):
    def __init__(self, matrix=[[5, 4, 5], [4, 7, 6], [5, 3, 1]]):
        super().__init__()
        self.matrix = matrix
        self.setWindowTitle('Scalar multiplication')
        self.create_layout()
        self.setCentralWidget(self.wid)

    def create_layout(self):
        if (True):
            self.wid = QWidget()
            grid_grandote = QGridLayout()
            self.matrix = np.array(self.matrix)
            self.wid.setLayout(grid_grandote)
            # create grid layout
            grid = QGridLayout()
            self.grid_result = QGridLayout()
            self.labels = {}
            layout_matriz_entrada = QVBoxLayout()
            layout_procedimiento = QVBoxLayout()
            layout_resultado = QVBoxLayout()
            layout_line_button = QHBoxLayout()
            layout_procedimiento.addLayout(layout_line_button)
            grid_grandote.addLayout(layout_procedimiento, 0, 0)
            grid_grandote.addLayout(layout_resultado, 0, 2)
            grid_grandote.addLayout(layout_matriz_entrada, 0, 3)
            grid_grandote.addLayout(self.grid_result, 0, 5)
            # procedimiento
            label_procedimiento = QLabel('Scalar:')
            layout_line_button.addWidget(label_procedimiento)
            self.scalar = QLineEdit()
            layout_line_button.addWidget(self.scalar)
            self.boton_resultado = QPushButton('Result')
            self.boton_resultado.clicked.connect(self.resultado)
            layout_procedimiento.addWidget(self.boton_resultado)
            # create labels
            label1 = QLabel('X')
            grid_grandote.addWidget(label1, 0, 1)
            label1 = QLabel('=')
            grid_grandote.addWidget(label1, 0, 4)

            # create labels
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    label = QLabel(str(self.matrix[i][j]))
                    grid.addWidget(label, i, j)
            layout_matriz_entrada.addLayout(grid)

            self.labels['resultado'] = QLabel('')
            self.grid_result.addWidget(self.labels['resultado'], 0, 0)

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    self.grid_result.addWidget(QLabel(''), i, j)

    def resultado(self):
        self.clearResult()
        escalar = self.scalar.text()
        self.labels['resultado'].setText('')
        if (escalar == ''):
            self.labels['resultado'].setText('Error, the scalar is empty')
        else:
            escalar = int(escalar)
            result = scalar_product(self.matrix, escalar)
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.grid_result.itemAtPosition(i, j).widget().setText(str(result[i][j]))
    
    def clearResult(self):
        for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    self.grid_result.itemAtPosition(i, j).widget().setText("")