# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 500))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 500))
        self.widget.setMaximumSize(QSize(800, 500))
        self.widget.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.menubar = QMenuBar(self.widget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.labelColorVerde = QLabel(self.widget)
        self.labelColorVerde.setObjectName(u"labelColorVerde")
        self.labelColorVerde.setGeometry(QRect(200, 260, 95, 35))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelColorVerde.setFont(font)
        self.labelColorVerde.setAlignment(Qt.AlignCenter)
        self.id = QSpinBox(self.widget)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(120, 50, 90, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.id.setFont(font1)
        self.id.setCursor(QCursor(Qt.PointingHandCursor))
        self.id.setWrapping(False)
        self.id.setMaximum(9999)
        self.labelCOLOR = QLabel(self.widget)
        self.labelCOLOR.setObjectName(u"labelCOLOR")
        self.labelCOLOR.setGeometry(QRect(0, 300, 95, 35))
        self.labelCOLOR.setFont(font)
        self.labelCOLOR.setAlignment(Qt.AlignCenter)
        self.labelColorRojo = QLabel(self.widget)
        self.labelColorRojo.setObjectName(u"labelColorRojo")
        self.labelColorRojo.setGeometry(QRect(100, 260, 95, 35))
        self.labelColorRojo.setFont(font)
        self.labelColorRojo.setAlignment(Qt.AlignCenter)
        self.destinoY = QSpinBox(self.widget)
        self.destinoY.setObjectName(u"destinoY")
        self.destinoY.setGeometry(QRect(240, 210, 90, 30))
        self.destinoY.setFont(font1)
        self.destinoY.setCursor(QCursor(Qt.PointingHandCursor))
        self.destinoY.setWrapping(False)
        self.destinoY.setMaximum(500)
        self.rojo = QSpinBox(self.widget)
        self.rojo.setObjectName(u"rojo")
        self.rojo.setGeometry(QRect(100, 300, 90, 30))
        self.rojo.setFont(font1)
        self.rojo.setCursor(QCursor(Qt.PointingHandCursor))
        self.rojo.setWrapping(False)
        self.rojo.setMaximum(255)
        self.labelVELOCIDAD = QLabel(self.widget)
        self.labelVELOCIDAD.setObjectName(u"labelVELOCIDAD")
        self.labelVELOCIDAD.setGeometry(QRect(240, 10, 95, 35))
        self.labelVELOCIDAD.setFont(font)
        self.labelVELOCIDAD.setAlignment(Qt.AlignCenter)
        self.labelORIGEN_X = QLabel(self.widget)
        self.labelORIGEN_X.setObjectName(u"labelORIGEN_X")
        self.labelORIGEN_X.setGeometry(QRect(120, 90, 95, 35))
        self.labelORIGEN_X.setFont(font)
        self.labelORIGEN_X.setAlignment(Qt.AlignCenter)
        self.velocidad = QSpinBox(self.widget)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setGeometry(QRect(240, 50, 90, 30))
        self.velocidad.setFont(font1)
        self.velocidad.setCursor(QCursor(Qt.PointingHandCursor))
        self.velocidad.setWrapping(False)
        self.velocidad.setMaximum(9999)
        self.destinoX = QSpinBox(self.widget)
        self.destinoX.setObjectName(u"destinoX")
        self.destinoX.setGeometry(QRect(240, 130, 90, 30))
        self.destinoX.setFont(font1)
        self.destinoX.setCursor(QCursor(Qt.PointingHandCursor))
        self.destinoX.setWrapping(False)
        self.destinoX.setMaximum(500)
        self.labelDESTINO_X = QLabel(self.widget)
        self.labelDESTINO_X.setObjectName(u"labelDESTINO_X")
        self.labelDESTINO_X.setGeometry(QRect(240, 90, 95, 35))
        self.labelDESTINO_X.setFont(font)
        self.labelDESTINO_X.setAlignment(Qt.AlignCenter)
        self.labelID = QLabel(self.widget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setGeometry(QRect(120, 10, 95, 35))
        self.labelID.setFont(font)
        self.labelID.setAlignment(Qt.AlignCenter)
        self.labelColorAzul = QLabel(self.widget)
        self.labelColorAzul.setObjectName(u"labelColorAzul")
        self.labelColorAzul.setGeometry(QRect(300, 260, 95, 35))
        self.labelColorAzul.setFont(font)
        self.labelColorAzul.setAlignment(Qt.AlignCenter)
        self.labelDESTINO_Y = QLabel(self.widget)
        self.labelDESTINO_Y.setObjectName(u"labelDESTINO_Y")
        self.labelDESTINO_Y.setGeometry(QRect(240, 170, 95, 35))
        self.labelDESTINO_Y.setFont(font)
        self.labelDESTINO_Y.setAlignment(Qt.AlignCenter)
        self.verde = QSpinBox(self.widget)
        self.verde.setObjectName(u"verde")
        self.verde.setGeometry(QRect(200, 300, 90, 30))
        self.verde.setFont(font1)
        self.verde.setCursor(QCursor(Qt.PointingHandCursor))
        self.verde.setWrapping(False)
        self.verde.setMaximum(255)
        self.origenY = QSpinBox(self.widget)
        self.origenY.setObjectName(u"origenY")
        self.origenY.setGeometry(QRect(120, 210, 90, 30))
        self.origenY.setFont(font1)
        self.origenY.setCursor(QCursor(Qt.PointingHandCursor))
        self.origenY.setWrapping(False)
        self.origenY.setMaximum(500)
        self.azul = QSpinBox(self.widget)
        self.azul.setObjectName(u"azul")
        self.azul.setGeometry(QRect(300, 300, 90, 30))
        self.azul.setFont(font1)
        self.azul.setCursor(QCursor(Qt.PointingHandCursor))
        self.azul.setWrapping(False)
        self.azul.setMaximum(255)
        self.origenX = QSpinBox(self.widget)
        self.origenX.setObjectName(u"origenX")
        self.origenX.setGeometry(QRect(120, 130, 90, 30))
        self.origenX.setFont(font1)
        self.origenX.setCursor(QCursor(Qt.PointingHandCursor))
        self.origenX.setWrapping(False)
        self.origenX.setMaximum(500)
        self.labelORIGEN_Y = QLabel(self.widget)
        self.labelORIGEN_Y.setObjectName(u"labelORIGEN_Y")
        self.labelORIGEN_Y.setGeometry(QRect(120, 170, 95, 35))
        self.labelORIGEN_Y.setFont(font)
        self.labelORIGEN_Y.setAlignment(Qt.AlignCenter)
        self.abInicio = QPushButton(self.widget)
        self.abInicio.setObjectName(u"abInicio")
        self.abInicio.setGeometry(QRect(30, 430, 100, 40))
        self.abInicio.setFont(font)
        self.distancia = QDoubleSpinBox(self.widget)
        self.distancia.setObjectName(u"distancia")
        self.distancia.setEnabled(True)
        self.distancia.setGeometry(QRect(180, 390, 90, 30))
        self.distancia.setDecimals(2)
        self.labelDistancia = QLabel(self.widget)
        self.labelDistancia.setObjectName(u"labelDistancia")
        self.labelDistancia.setGeometry(QRect(180, 350, 95, 35))
        self.labelDistancia.setFont(font)
        self.labelDistancia.setAlignment(Qt.AlignCenter)
        self.plainTextEditor = QPlainTextEdit(self.widget)
        self.plainTextEditor.setObjectName(u"plainTextEditor")
        self.plainTextEditor.setGeometry(QRect(420, 20, 371, 451))
        self.abMostrar = QPushButton(self.widget)
        self.abMostrar.setObjectName(u"abMostrar")
        self.abMostrar.setGeometry(QRect(300, 430, 100, 40))
        self.abMostrar.setFont(font)
        self.abFinal = QPushButton(self.widget)
        self.abFinal.setObjectName(u"abFinal")
        self.abFinal.setGeometry(QRect(160, 430, 100, 40))
        self.abFinal.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.labelColorVerde.setText(QCoreApplication.translate("MainWindow", u"VERDE:", None))
        self.labelCOLOR.setText(QCoreApplication.translate("MainWindow", u"COLOR:", None))
        self.labelColorRojo.setText(QCoreApplication.translate("MainWindow", u"ROJO:", None))
        self.labelVELOCIDAD.setText(QCoreApplication.translate("MainWindow", u"VEL.:", None))
        self.labelORIGEN_X.setText(QCoreApplication.translate("MainWindow", u"ORIGEN: X", None))
        self.labelDESTINO_X.setText(QCoreApplication.translate("MainWindow", u"DESTINO: X", None))
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.labelColorAzul.setText(QCoreApplication.translate("MainWindow", u"AZUL:", None))
        self.labelDESTINO_Y.setText(QCoreApplication.translate("MainWindow", u"DESTINO: Y", None))
        self.labelORIGEN_Y.setText(QCoreApplication.translate("MainWindow", u"ORIGEN: Y", None))
        self.abInicio.setText(QCoreApplication.translate("MainWindow", u"A. INICIO", None))
        self.labelDistancia.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA", None))
        self.abMostrar.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.abFinal.setText(QCoreApplication.translate("MainWindow", u"A. FINAL", None))
    # retranslateUi