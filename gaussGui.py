import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from fractions import Fraction
from gaussjordan import gaussJordan


class GaussJordanUI(QMainWindow):
    def __init__(self,matrix=[[Fraction(2),Fraction(1),Fraction(-1)],[Fraction(1),Fraction(4),Fraction(-3)],[Fraction(-3),Fraction(1),Fraction(2)]]):
        super().__init__()
        self.matrix = matrix
        self.setWindowTitle('Gauss-Jordan')
        self.create_layout()
        self.setCentralWidget(self.wid)
    
    def create_layout(self):
        self.wid = QWidget()
        box = QVBoxLayout()
        qhorizontal = QHBoxLayout()
        self.wid.setLayout(box)
        self.tabla = QTableWidget()
        self.tabla.setRowCount(len(self.matrix))
        self.tabla.setColumnCount(len(self.matrix[0])+1)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        boton = QPushButton('Calculate')
        boton.clicked.connect(self.calcular)
        self.tablaRes = QTableWidget()
        self.tablaRes.setRowCount(len(self.matrix))
        self.tablaRes.setColumnCount(len(self.matrix[0])+1)
        self.tablaRes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tablaRes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaRes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaRes.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])+1):
                self.tablaRes.setItem(i,j,QTableWidgetItem(""))
                if j == len(self.matrix[0]):
                    self.tabla.setItem(i,j,QTableWidgetItem(""))
                    self.tabla.item(i,j).setBackground(QColor(255,255,0))
                    self.tablaRes.item(i,j).setBackground(QColor(255,255,0))
                else:
                    self.tabla.setItem(i, j, QTableWidgetItem(str(self.matrix[i][j])))
        qhorizontal.addWidget(self.tabla)
        qhorizontal.addWidget(QLabel('Result:'))
        qhorizontal.addWidget(self.tablaRes)
        box.addWidget(QLabel('Complete the augmented matrix:'))
        box.addLayout(qhorizontal)
        box.addWidget(boton)
    
    def calcular(self):
        temp = []
        for i in range(self.tabla.rowCount()):
            row = []
            for j in range(self.tabla.columnCount()):
                if(self.tabla.item(i, j).text() == ''):
                    QMessageBox.warning(self, 'Error', 'Fill all cells')
                    return False
                row.append(Fraction(self.tabla.item(i, j).text()))
            temp.append(row)
        print(temp)
        res = gaussJordan(temp)
        for i in range(len(res)):
            for j in range(len(res[0])):
                self.tablaRes.setItem(i,j,QTableWidgetItem(str(res[i][j])))
                if j == len(res[0])-1:
                    self.tablaRes.item(i,j).setBackground(QColor(255,255,0))
