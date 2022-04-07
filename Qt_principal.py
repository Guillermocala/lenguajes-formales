import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QPushButton, QLabel, QLineEdit, QGridLayout, QWidget,
    QTabWidget, QComboBox, QVBoxLayout, QHBoxLayout
    )

class AlfabetoWidget(QWidget):
    def __init__(self):
        super().__init__()
        #configuracion layouts
        self.principal = QVBoxLayout(self)
        self.ingreso_alfabetos = QHBoxLayout()
        self.seleccion_alfabetos = QHBoxLayout()
        self.operaciones_alfabetos = QVBoxLayout()
        self.cerradura_alfabeto = QHBoxLayout()
        self.principal.addLayout(self.ingreso_alfabetos)
        self.principal.addLayout(self.seleccion_alfabetos)
        self.principal.addLayout(self.operaciones_alfabetos)
        self.principal.addLayout(self.cerradura_alfabeto)
        #entrada alfabetos
        self.entrada_alfabetos = QLineEdit()
        self.entrada_alfabetos.setPlaceholderText("Ingrese el alfabeto(minimo 2 alfabetos)")
        self.entrada_alfabetos.setClearButtonEnabled(True)
        self.button_add = QPushButton("Agregar alfabeto")
        
        self.ingreso_alfabetos.addWidget(self.entrada_alfabetos)
        self.ingreso_alfabetos.addWidget(self.button_add)
        #seleccion alfabetos
        self.alfabeto1 = QComboBox()
        self.alfabeto1.setPlaceholderText("Indice alfabeto 1")
        self.alfabeto2 = QComboBox()
        self.alfabeto2.setPlaceholderText("Indice alfabeto 2")
        self.seleccion_alfabetos.addWidget(self.alfabeto1)
        self.seleccion_alfabetos.addWidget(self.alfabeto2)
        #operaciones alfabetos
        self.button_union = QPushButton("Union")
        self.button_diff = QPushButton("Diferencia")
        self.button_inter = QPushButton("Interseccion")
        self.button_show = QPushButton("Mostrar alfabetos")
        self.operaciones_alfabetos.addWidget(self.button_union)
        self.operaciones_alfabetos.addWidget(self.button_diff)
        self.operaciones_alfabetos.addWidget(self.button_inter)
        self.operaciones_alfabetos.addWidget(self.button_show)
        #cerradura alfabeto
        self.alfabeto_cerradura = QComboBox()
        self.alfabeto_cerradura.setPlaceholderText("Indice alfabeto")
        self.cantidad_palabras = QLineEdit()
        self.cantidad_palabras.setPlaceholderText("Ingrese la cantidad de palabras")
        self.cantidad_palabras.setClearButtonEnabled(True)
        self.calcular_cerradura = QPushButton("Generar palabras")
        self.cerradura_alfabeto.addWidget(self.alfabeto_cerradura)
        self.cerradura_alfabeto.addWidget(self.cantidad_palabras)
        self.cerradura_alfabeto.addWidget(self.calcular_cerradura)
        

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
        self.setGeometry(500, 100, 500, 500)
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
        self.opcion1 = self.menu_bar.addMenu("Menu")
        self.subAction11 = self.opcion1.addAction("Asistente de voz")
        self.subAction11.triggered.connect(self.imprimo)
        self.opcion1.addSeparator()
        self.opcion1.addAction("Exit", self.close)
        #opcion2
        self.opcion2 = self.menu_bar.addMenu("Lenguaje")
        self.subAction21 = self.opcion2.addAction("Español")
        self.subAction22 = self.opcion2.addAction("Ingles")
        self.subAction21.triggered.connect(self.imprimo)
        self.subAction22.triggered.connect(self.imprimo)
    
    def imprimo(self):
        print("soy una accion de los menus")

        
def ventana():
    app = QApplication(sys.argv)
    ventana = MyApp()
    sys.exit(app.exec())

ventana()