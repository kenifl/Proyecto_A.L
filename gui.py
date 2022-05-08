# USE PYQT and create a 3z2 grid of buttons
from fractions import Fraction
from importlib.metadata import FileHash
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
from determinant_gui import Determinante
from inverse_gui import Inverse_GUI
import numpy as np

matrix = []
filas = 0
columnas = 0

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora de matrices')
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
        self.genMatrix = QPushButton('Ingresar datos')
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
        suma = QPushButton('Suma')
        suma.clicked.connect(self.suma)
        multiMatrices = QPushButton('Multiplicación de matrices')
        multiMatrices.clicked.connect(self.multiMatrices)
        escalar = QPushButton('Escalar de multiplicación')
        escalar.clicked.connect(self.escalar)
        determinante = QPushButton('Determinante')
        determinante.clicked.connect(self.determinante)
        inversa = QPushButton('Inversa')
        inversa.clicked.connect(self.inversa)
        transpuesta = QPushButton('Transpuesta')
        transpuesta.clicked.connect(self.transpuesta)
        adjunta = QPushButton('Adjunta')
        adjunta.clicked.connect(self.adjunta)
        guass = QPushButton('Gauss-Jordan')
        guass.clicked.connect(self.gauss)
        box2.addWidget(suma)
        box2.addWidget(multiMatrices)
        box2.addWidget(escalar)
        box2.addWidget(determinante)
        box2.addWidget(inversa)
        box2.addWidget(transpuesta)
        box2.addWidget(adjunta)
        box2.addWidget(guass)
        horizontal2.addLayout(box2)
    
    def generateTable(self):
        filas = int(self.rows.text())
        columnas = int(self.columns.text())
        self.tabla.setVisible(True)
        self.tabla.setRowCount(filas)
        self.tabla.setColumnCount(columnas)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def getMatrix(self):
        matrix = []
        for i in range(self.tabla.rowCount()):
            row = []
            for j in range(self.tabla.columnCount()):
                row.append(Fraction(self.tabla.item(i, j).text()))
            matrix.append(row)
        #print(matrix)
        return matrix
    
    def suma(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()
    
    def multiMatrices(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()

    def escalar(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()

    def determinante(self):
        # self.mainWindow = homeAdmin(self.id)
        self.venatana_determinante=Determinante(self.getMatrix())
        self.venatana_determinante.show()
        self.close()

    def inversa(self):
        # self.mainWindow = homeAdmin(self.id)
        #print(np.array(self.getMatrix()))
        self.VentanaInversa = Inverse_GUI(np.array(self.getMatrix()))
        self.VentanaInversa.show()
        #self.close()

    def transpuesta(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()

    def adjunta(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()

    def gauss(self):
        self.getMatrix()
        # self.mainWindow = homeAdmin(self.id)
        self.mainWindow.show()
        self.close()



app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()

