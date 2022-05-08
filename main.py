from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QScreen
from PyQt6.QtWidgets import *
import sys
import sqlite3
import uuid

from gui import Principal

con = sqlite3.connect('base.db')
cur = con.cursor()
class inicioSesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(450, 150)
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
        layout = QGridLayout()
        self.wid.setLayout(layout)

        self.etiquetas = {}
        self.campos_texto = {}
        self.botones = {}
        self.botones['ingresar'] = QPushButton('Ingresar')
        self.botones['ingresar'].clicked.connect(self.validar)
        self.botones['registrar'] = QPushButton('Registrar')
        self.botones['registrar'].clicked.connect(self.registrar)

        self.etiquetas['usuario'] = QLabel('Usuario: ')
        self.etiquetas['contrasena'] = QLabel('Contraseña: ')
        self.etiquetas['mensaje'] = QLabel(' ')
        self.etiquetas['mensaje'].setStyleSheet('color: red; font-size: 10pt;')
        self.etiquetas['mensaje'].hide()
        self.campos_texto['usuario'] = QLineEdit()
        self.campos_texto['contrasena'] = QLineEdit()
        self.campos_texto['contrasena'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.etiquetas['usuario'], 1, 0)
        layout.addWidget(self.campos_texto['usuario'], 1, 1)
        layout.addWidget(self.etiquetas['contrasena'], 2, 0)
        layout.addWidget(self.campos_texto['contrasena'], 2, 1)
        layout.addWidget(self.etiquetas['mensaje'], 3, 0, 1, 2)
        layout.addWidget(self.botones['ingresar'], 4, 0, 1, 2)
        layout.addWidget(self.botones['registrar'], 5, 0, 1, 2)

    def validar(self):
        self.etiquetas['mensaje'].hide()
        usuario = self.campos_texto['usuario'].text()
        contrasena = self.campos_texto['contrasena'].text()
        cur.execute("SELECT id FROM Usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena))
        usuario = cur.fetchone()
        self.etiquetas['mensaje'].show()
        if usuario is None:
            self.etiquetas['mensaje'].setText('Usuario o contraseña incorrectos')
        else:
            self.mainWindow = Principal(usuario[0])
            self.mainWindow.show()
            self.close()
    
    def registrar(self):
        self.etiquetas['mensaje'].setVisible(False)
        username = self.campos_texto['usuario'].text()
        contrasena = self.campos_texto['contrasena'].text()
        if contrasena == '' or username == '':
            self.etiquetas['mensaje'].setVisible(True)
            self.etiquetas['mensaje'].setText('Campos vacíos')
        else:
            cur.execute("SELECT * FROM Usuarios WHERE usuario = ?", (username,))
            usuario = cur.fetchone()
            if usuario is not None:
                self.etiquetas['mensaje'].setVisible(True)
                self.etiquetas['mensaje'].setText('Usuario ya existente')
                self.etiquetas['mensaje'].setStyleSheet('color: red')
            else:
                id = str(uuid.uuid4())
                cur.execute("INSERT INTO Usuarios VALUES (?, ?, ?)", (id, username, contrasena))
                con.commit()
                self.etiquetas['mensaje'].setVisible(True)
                self.etiquetas['mensaje'].setText('Usuario registrado. Inicie sesión')
                self.etiquetas['mensaje'].setStyleSheet('color: green')
                self.campos_texto['usuario'].setText('')
                self.campos_texto['contrasena'].setText('')

app = QApplication(sys.argv)
window = inicioSesion()
window.show()
app.exec()