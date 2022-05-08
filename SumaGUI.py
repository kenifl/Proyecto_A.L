from PyQt6.QtWidgets import *
from fractions import Fraction
import numpy as np
from suma_matriz import suma_matriz


class Add(QMainWindow):
    def __init__(self, matrix=None):
        super().__init__()
        if matrix is None:
            matrix = [[5, 4, 5], [4, 7, 6], [5, 3, 1]]
        self.matrix = matrix
        self.setWindowTitle('Matrix Addition')
        self.create_layout()
        self.setCentralWidget(self.wid)

    def create_layout(self):
        if True:
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
            grid_grandote.addLayout(layout_matriz_entrada, 0, 0)
            grid_grandote.addLayout(layout_resultado, 0, 2)
            grid_grandote.addLayout(layout_procedimiento, 0, 3)
            grid_grandote.addLayout(self.grid_result, 0, 5)
            self.tabla = QTableWidget()
            self.tabla.setRowCount(self.matrix.shape[0])
            self.tabla.setColumnCount(self.matrix.shape[1])
            self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            layout_procedimiento.addWidget(self.tabla)
            self.boton_resultado = QPushButton('Resultado')
            self.boton_resultado.clicked.connect(self.resultado)
            layout_procedimiento.addWidget(self.boton_resultado)
            # create labels
            label1 = QLabel('+')
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

    def get_matrix(self):
        matrix = []
        for i in range(self.tabla.rowCount()):
            row = []
            for j in range(self.tabla.columnCount()):
                if self.tabla.item(i, j) is None or self.tabla.item(i, j).text() == '':
                    QMessageBox.warning(self, 'Error', 'Fill all cells')
                    return False
                else:
                    row.append(Fraction(self.tabla.item(i, j).text()))
            matrix.append(row)
        return matrix

    def resultado(self):
        matrix_2 = self.get_matrix()
        self.labels['resultado'].setText('')
        if not matrix_2:
            self.labels['resultado'].setText('Error, operation can´t be done')
        else:
            result = suma_matriz(self.matrix, matrix_2)
            for i in range(len(result)):
                for j in range(len(result[i])):
                    label = QLabel(str(result[i][j]))
                    self.grid_result.addWidget(label, i, j)
