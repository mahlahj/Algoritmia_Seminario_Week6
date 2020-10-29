from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from organizador import Organizador
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particula = Particula()
        self.organizador = Organizador()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.abInicio.clicked.connect(self.click_agregar_inicio)
        self.ui.abFinal.clicked.connect(self.click_agregar_final)
        self.ui.abMostrar.clicked.connect(self.click_mostrar)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir.triggered.connect(self.abrir)


    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEditor.clear()
        self.ui.plainTextEditor.insertPlainText(self.organizador.mostrar())
    
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id.value()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.value()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.organizador.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id.value()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.value()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.organizador.agregar_final(particula)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar', '.', 'JSON (*.json)')
        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.organizador.guardar(), archivo, indent=4)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir', '.', 'JSON (*.json)')
        with open(ubicacion[0], 'r') as archivo:
            self.organizador.get(json.load(archivo))