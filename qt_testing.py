import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class LabelPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout_principal = QtWidgets.QVBoxLayout(self)
        self.pestañas = QtWidgets.QTabWidget()
        self.layout_principal.addWidget(self.pestañas)

        
        
            

        self.gb_alfabetos = QtWidgets.QGroupBox("Pantalla principal alfabetos")

        self.principal_alfabetos = QtWidgets.QVBoxLayout()
        
        self.label1 = QtWidgets.QLabel("Ingresar alfabeto: ")
        self.input1 = QtWidgets.QLineEdit()
        self.check_input1 = QtWidgets.QPushButton("add")
        self.principal_alfabetos.addWidget(self.label1)
        self.principal_alfabetos.addWidget(self.input1)
        self.principal_alfabetos.addWidget(self.check_input1)
        self.gb_alfabetos.setLayout(self.principal_alfabetos)

        self.pestañas.addTab(self.gb_alfabetos, "Alfabetos")
        self.principal_alfabetos.addStretch(0)

        self.componente(self.input1)
        
    def componente(self, input):
        # creating a push button
        button = input
        # adding action to a button
        button.connect(self.clickme())
        # getting text in button
        text = button.text()
        print(text)

    def clickme(self):
        print("Button clicked, Hello!")
            
        
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    label = LabelPrincipal()
    label.resize(500,500)
    label.show()

    sys.exit(app.exec())