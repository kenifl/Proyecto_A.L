import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from Adjugate_GUI import Adjugate
from Transpose_GUI import Transpose
from determinant_gui import Determinante
from inverse_gui import Inverse_GUI
from fractions import Fraction
from Producto_Matrices import ProductoM_GUI
from gaussGui import GaussJordanUI
import numpy as np

filas = 0
columnas = 0

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Matrix Calculator')
        self.setFixedSize(1280, 720)
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
        box = QVBoxLayout()
        qhorizontal = QHBoxLayout()
        horizontal2 = QHBoxLayout()
        box2 = QVBoxLayout()
        self.wid.setLayout(horizontal2)

        self.rows = QLineEdit()
        self.columns = QLineEdit()
        self.genMatrix = QPushButton('Input data')
        self.genMatrix.clicked.connect(self.generateTable)

        self.tabla = QTableWidget()
        self.tabla.setVisible(False)

        qhorizontal.addWidget(self.rows)
        qhorizontal.addWidget(QLabel('x'))
        qhorizontal.addWidget(self.columns)
        qhorizontal.addWidget(self.genMatrix)
        box.addLayout(qhorizontal)
        box.addWidget(self.tabla)

        horizontal2.addLayout(box)
        self.suma = QPushButton('Addition')
        self.suma.clicked.connect(self.suma_matrices)
        self.suma.setEnabled(False)
        self.multiMatrices = QPushButton('Multiplicación de matrices')
        self.multiMatrices.clicked.connect(self.multimatrices_funcion)
        self.multiMatrices.setEnabled(False)
        self.escalar = QPushButton('Scalar multiplication')
        self.escalar.clicked.connect(self.escalar_funcion)
        self.escalar.setEnabled(False)
        self.determinante = QPushButton('Determinant')
        self.determinante.clicked.connect(self.determinante_funcion)
        self.determinante.setEnabled(False)
        self.inversa = QPushButton('Inverse')
        self.inversa.clicked.connect(self.inversa_funcion)
        self.inversa.setEnabled(False)
        self.transpuesta = QPushButton('Transpose')
        self.transpuesta.clicked.connect(self.transpuesta_funcion)
        self.transpuesta.setEnabled(False)
        self.adjunta = QPushButton('Adjugate')
        self.adjunta.clicked.connect(self.adjunta_funcion)
        self.adjunta.setEnabled(False)
        self.guass = QPushButton('Gauss-Jordan')
        self.guass.clicked.connect(self.gauss_funcion)
        self.guass.setEnabled(False)
        box2.addWidget(self.suma)
        box2.addWidget(self.multiMatrices)
        box2.addWidget(self.escalar)
        box2.addWidget(self.determinante)
        box2.addWidget(self.inversa)
        box2.addWidget(self.transpuesta)
        box2.addWidget(self.adjunta)
        box2.addWidget(self.guass)
        horizontal2.addLayout(box2)
    
    def generateTable(self):
        filas = int(self.rows.text())
        columnas = int(self.columns.text())
        self.tabla.setVisible(True)
        self.tabla.setRowCount(filas)
        self.tabla.setColumnCount(columnas)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        if(filas == columnas):
            self.determinante.setEnabled(True)
            self.inversa.setEnabled(True)
            self.adjunta.setEnabled(True)
        else:
            self.determinante.setEnabled(False)
            self.inversa.setEnabled(False)
            self.adjunta.setEnabled(False)
        self.suma.setEnabled(True)
        self.multiMatrices.setEnabled(True)
        self.escalar.setEnabled(True)
        self.guass.setEnabled(True)
        self.transpuesta.setEnabled(True)

            

    def getMatrix(self):
        matrix = []
        for i in range(self.tabla.rowCount()):
            row = []
            for j in range(self.tabla.columnCount()):
                if(self.tabla.item(i, j) == None):
                    QMessageBox.warning(self, 'Error', 'Fill all cells')
                    return False
                else:
                    row.append(Fraction(self.tabla.item(i, j).text()))
            matrix.append(row)
        return matrix
    
    def suma_matrices(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()
    
    def multimatrices_funcion(self):
        matrix = self.getMatrix()
        if not matrix:
            QMessageBox.warning(self, 'Error', 'Fill all cells')
        else:
            self.VentanaInversa = ProductoM_GUI(matrix)
            self.VentanaInversa.show()
        

    def escalar_funcion(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()

    def determinante_funcion(self):
        # self.mainWindow = homeAdmin(self.id)
        self.ventana_determinante=Determinante(self.getMatrix())
        self.ventana_determinante.show()
        self.close()

<<<<<<< HEAD
    def determinante(self):
        # self.mainWindow = homeAdmin(self.id)
        self.venatana_determinante=Determinante(self.getMatrix())
        self.venatana_determinante.show()
        #self.close()

    def inversa(self):
=======
    def inversa_funcion(self):
>>>>>>> 6cc5edcb5323407436c3ba21dc53b84d931863cd
        # self.mainWindow = homeAdmin(self.id)
        #print(np.array(self.getMatrix()))
        matrix = self.getMatrix()
        if not matrix:
            QMessageBox.warning(self, 'Error', 'Fill all cells')
        else:
            self.VentanaInversa = Inverse_GUI(np.array(matrix))
            self.VentanaInversa.show()
        #self.close()

    def transpuesta_funcion(self):
        # self.mainWindow = homeAdmin(self.id)
        self.ventana_transpose= Transpose(np.array(self.getMatrix()))
        self.ventana_transpose.show()
        # self.close()

<<<<<<< HEAD
    def adjunta(self):
        self.ventana_adjugate=Adjugate(np.array(self.getMatrix()))
        self.ventana_adjugate.show()
        #self.close
=======
    def adjunta_funcion(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()
>>>>>>> 6cc5edcb5323407436c3ba21dc53b84d931863cd

    def gauss_funcion(self):
        self.ventanaGauss = GaussJordanUI(self.getMatrix())
        self.ventanaGauss.show()
        # self.close()

app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()

