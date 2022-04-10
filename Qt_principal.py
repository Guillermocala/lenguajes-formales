from Clases import Alfabetos, Lenguajes
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QPushButton, QLabel, QLineEdit, QGridLayout, QWidget,
    QTabWidget, QComboBox, QVBoxLayout, QHBoxLayout,
    QDialog, QTableWidget, QTableWidgetItem
    )

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.alfabetos = Alfabetos()
        self.setGeometry(500, 100, 500, 500)
        self.setWindowTitle("Operador de lenguajes")
        self.initUI()
        self.initMenuBar()
        self.show()
        
    def initUI(self):
        self.principal = QTabWidget()
        self.indice_alfabetos = self.principal.addTab(AlfabetoWidget(self.alfabetos), "Alfabetos")
        self.indice_lenguajes = self.principal.addTab(LenguajeWidget(self.alfabetos), "Lenguajes")
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
        self.opcion2 = self.menu_bar.addMenu("Idioma")
        self.subAction21 = self.opcion2.addAction("Español")
        self.subAction22 = self.opcion2.addAction("Ingles")
        self.subAction21.triggered.connect(self.imprimo)
        self.subAction22.triggered.connect(self.imprimo)
    
    def imprimo(self):
        print("soy una accion de los menus")

class AlfabetoWidget(QWidget):
    def __init__(self, alfabetos):
        super().__init__()
        #configuracion layouts
        self.objeto_alfabetos = alfabetos
        self.principal = QVBoxLayout(self)
        self.ingreso_alfabetos = QHBoxLayout()
        self.seleccion_alfabetos = QHBoxLayout()
        self.operaciones_alfabetos = QVBoxLayout()
        self.cerradura_alfabeto = QHBoxLayout()
        self.principal.addLayout(self.ingreso_alfabetos)
        self.principal.addLayout(self.seleccion_alfabetos)
        self.principal.addLayout(self.operaciones_alfabetos)
        self.principal.addLayout(self.cerradura_alfabeto)
        #entrada alfabetos  QLineEdit y button agregar
        self.entrada_alfabetos = QLineEdit()
        self.entrada_alfabetos.setPlaceholderText("Ingrese el alfabeto(separado por coma)")
        self.entrada_alfabetos.setClearButtonEnabled(True)
        self.button_add = QPushButton("Agregar alfabeto")
        self.button_add.clicked.connect(self.ingresa_alfabeto)
        self.ingreso_alfabetos.addWidget(self.entrada_alfabetos)
        self.ingreso_alfabetos.addWidget(self.button_add)
        #seleccion alfabetos    comboBox
        self.comboBox_alfabeto1 = QComboBox()
        self.comboBox_alfabeto1.setPlaceholderText("Indice alfabeto 1")
        self.comboBox_alfabeto2 = QComboBox()
        self.comboBox_alfabeto2.setPlaceholderText("Indice alfabeto 2")
        self.seleccion_alfabetos.addWidget(self.comboBox_alfabeto1)
        self.seleccion_alfabetos.addWidget(self.comboBox_alfabeto2)
        #operaciones alfabetos  QPushButton y connect
        self.button_union = QPushButton("Union")
        self.button_diff = QPushButton("Diferencia")
        self.button_inter = QPushButton("Interseccion")
        self.button_show = QPushButton("Mostrar alfabetos")
        self.button_union.clicked.connect(self.funciones_alfabetos)
        self.button_diff.clicked.connect(self.funciones_alfabetos)
        self.button_inter.clicked.connect(self.funciones_alfabetos)
        self.button_show.clicked.connect(self.mostrar_alfabetos)
        self.operaciones_alfabetos.addWidget(self.button_union)
        self.operaciones_alfabetos.addWidget(self.button_diff)
        self.operaciones_alfabetos.addWidget(self.button_inter)
        self.operaciones_alfabetos.addWidget(self.button_show)
        #cerradura alfabeto
        self.comboBox_generar = QComboBox()
        self.comboBox_generar.setPlaceholderText("Indice alfabeto")
        self.cantidad_palabras = QLineEdit()
        self.cantidad_palabras.setPlaceholderText("Ingrese la cantidad de palabras")
        self.cantidad_palabras.setClearButtonEnabled(True)
        self.calcular_cerradura = QPushButton("Generar palabras")
        self.calcular_cerradura.clicked.connect(self.generar_palabras)
        self.cerradura_alfabeto.addWidget(self.comboBox_generar)
        self.cerradura_alfabeto.addWidget(self.cantidad_palabras)
        self.cerradura_alfabeto.addWidget(self.calcular_cerradura)

    def ingresa_alfabeto(self):
        cadena_entrada = self.entrada_alfabetos.displayText()
        if cadena_entrada != "":
            temp = self.objeto_alfabetos
            lista_alfabetos = cadena_entrada.split(",")
            if lista_alfabetos not in temp.get_lista():
                temp.add_item(lista_alfabetos)
                indice = str(len(temp.get_lista()))
                self.comboBox_alfabeto1.addItem(indice)
                self.comboBox_alfabeto2.addItem(indice)
                self.comboBox_generar.addItem(indice)
                self.alerta("Alfabeto ingresado!")
            else:
                self.alerta("Alfabeto repetido, ingrese otro!")
        else:
            self.alerta("El campo ingresar alfabeto está vacío!")
    
    def mostrar_alfabetos(self):
        lista = self.objeto_alfabetos.get_lista()
        if lista:
            self.tabla(lista)
        else:
            self.alerta("No hay elementos para mostrar!")

    def funciones_alfabetos(self):
        if len(self.objeto_alfabetos.get_lista()) > 1:
            seleccion1 = self.comboBox_alfabeto1.currentText()
            seleccion2 = self.comboBox_alfabeto2.currentText()
            if seleccion1 != "" and seleccion2 != "":
                boton = self.sender().text()
                match boton:
                    case "Union":
                        self.alerta(str(self.objeto_alfabetos.union(int(seleccion1) - 1, int(seleccion2) - 1)))
                        pass
                    case "Diferencia":
                        self.alerta(str(self.objeto_alfabetos.diferencia(int(seleccion1) - 1, int(seleccion2) - 1)))
                        pass
                    case "Interseccion":
                        self.alerta(str(self.objeto_alfabetos.interseccion(int(seleccion1) - 1, int(seleccion2) - 1)))
                        pass
                    case _:
                        self.alerta("Excepcion del case -> operaciones_alfabetos")
            else:
                self.alerta("Debe seleccionar 2 indices!")
        else:
            self.alerta("Debe ingresar al menos dos alfabetos!")
    
    def generar_palabras(self):
        if len(self.objeto_alfabetos.get_lista()) > 0:
            seleccion = self.comboBox_generar.currentText()
            cant_palabras = self.cantidad_palabras.displayText()
            if seleccion != "":
                if cant_palabras != "":
                    self.tabla(self.objeto_alfabetos.cerradura(int(seleccion) - 1, int(cant_palabras)))
                else:
                    self.alerta("Debe ingresar la cantidad de palabras!")
            else:
                self.alerta("Debe seleccionar el indice!")
        else:
            self.alerta("Debe ingresar minimo un alfabeto")
    
    def alerta(self, mensaje):
        dialog = QDialog(self)
        layout_mensaje = QVBoxLayout()
        campo_mensaje = QLabel(mensaje)
        boton_aceptar = QPushButton("Aceptar")
        boton_aceptar.clicked.connect(dialog.close)
        layout_mensaje.addWidget(campo_mensaje)
        layout_mensaje.addWidget(boton_aceptar)
        dialog.setLayout(layout_mensaje)
        dialog.exec()
    
    def tabla(self, data):
        dialog = QDialog(self)
        layout_data = QVBoxLayout()
        dialog.setWindowTitle("Tabla datos")
        tableWidget = QTableWidget(len(data), 1)
        tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for item in range(len(data)):
            newItemValue = QTableWidgetItem(str(data[item]))
            tableWidget.setItem(item - 1, 1, newItemValue)
        boton_aceptar = QPushButton("Aceptar")
        boton_aceptar.clicked.connect(dialog.close)
        layout_data.addWidget(tableWidget)
        layout_data.addWidget(boton_aceptar)
        dialog.setLayout(layout_data)
        dialog.exec()
        
class LenguajeWidget(QWidget):
    def __init__(self, alfabeto):
        super().__init__()
        self.banco = alfabeto
        self.principal = QHBoxLayout()
        self.label = QLabel("Prueba de comunicacion")
        self.principal.addWidget(self.label)
        self.button1 = QPushButton("Mostrar alfabetos")
        self.principal.addWidget(self.button1)
        self.button1.clicked.connect(self.texto)
        self.setLayout(self.principal)  
    
    def texto(self):
        print(self.banco.get_lista())

def ventana():
    app = QApplication(sys.argv)
    ventana = MyApp()
    sys.exit(app.exec())

ventana()