import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QPushButton, QLabel, QLineEdit, QGridLayout, QWidget,
    QTabWidget, QComboBox
    )

class AlfabetoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.principal = QGridLayout(self)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Ingrese el alfabeto")
        self.input.setClearButtonEnabled(True)
        self.principal.addWidget(self.input, 0, 0)
        self.button_add = QPushButton("Agregar")
        self.principal.addWidget(self.button_add, 0, 2)
        self.button_add.clicked.connect(self.texto)
        self.alfabeto1 = QComboBox()
        self.alfabeto1.setPlaceholderText("Alfabeto 1")
        self.alfabeto2 = QComboBox()
        self.alfabeto2.setPlaceholderText("Alfabeto 2")
        self.principal.addWidget(self.alfabeto1, 2, 0)
        self.principal.addWidget(self.alfabeto2, 2, 2)
        self.button_union = QPushButton("Union")
        self.principal.addWidget(self.button_union, 3, 0)
        self.button_diff = QPushButton("Diferencia")
        self.principal.addWidget(self.button_diff, 4, 0)
        self.button_inter = QPushButton("Interseccion")
        self.principal.addWidget(self.button_inter, 5, 0)

    def texto(self):
        res = "texto ingresado: " + self.input.displayText()
        print(res)

class LenguajeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.principal = QGridLayout()
        self.label = QLabel("Lenguajes")
        self.principal.addWidget(self.label, 0, 0, 1, 1)
        self.input = QLineEdit()
        self.principal.addWidget(self.input, 0, 1, 1, 1)
        self.button1 = QPushButton("Submit")
        self.principal.addWidget(self.button1, 0, 2, 1, 1)
        self.button1.clicked.connect(self.texto)
        self.setLayout(self.principal)  
    
    def texto(self):
        res = "texto ingresado: " + self.input.displayText()
        print(res)

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Operador de lenguajes")
        self.initUI()
        self.initMenuBar()
        self.show()
        
    def initUI(self):
        self.principal = QTabWidget()
        self.indice_alfabetos = self.principal.addTab(AlfabetoWidget(), "Alfabetos")
        self.indice_lenguajes = self.principal.addTab(LenguajeWidget(), "Lenguajes")
        self.setCentralWidget(self.principal)
    
    def initMenuBar(self):
        self.menu_bar = self.menuBar()
        #opcion 1
        self.opcion1 = self.menu_bar.addMenu("Opcion1")
        self.subAction11 = self.opcion1.addAction("SubOpcion1")
        self.subAction12 = self.opcion1.addAction("SubOpcion2")
        self.subAction11.triggered.connect(self.imprimo)
        self.subAction12.triggered.connect(self.imprimo)
        self.opcion1.addSeparator()
        self.opcion1.addAction("Exit", self.close)
        #opcion2
        self.opcion2 = self.menu_bar.addMenu("Opcion2")
        self.subAction21 = self.opcion2.addAction("SubOpcion1")
        self.subAction22 = self.opcion2.addAction("SubOpcion2")
        self.subAction21.triggered.connect(self.imprimo)
        self.subAction22.triggered.connect(self.imprimo)
    
    def imprimo(self):
        print("soy una accion de los menus")

        
def ventana():
    app = QApplication(sys.argv)
    ventana = MyApp()
    sys.exit(app.exec())

ventana()