# coding=utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
from Read.read import read_ar
from Desicion.desicion import principal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import img_rc
from Arbol import arbol as ab


class Ventana(QMainWindow):
    def __init__(self):
        global archivo
        global arbol
        QMainWindow.__init__(self)
        uic.loadUi("ventana1.ui",self)
        self.btnBuscar.clicked.connect(self.leerArchivo)
        self.btnGenerar.clicked.connect(self.generarGraficos)
        self.btnClasificar.clicked.connect(self.clasificarPunto)
        self.bloqueoClasificacion()
        self.bloqueoGeneracion()

        # ================== Configurar Tablas ==================

        self.tablaEntrenamiento.setDragDropOverwriteMode(False) # Deshabilitar el comportamiento de arrastrar y soltar
        self.tablaEntrenamiento.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleccionar toda la fila
        self.tablaEntrenamiento.setSelectionMode(QAbstractItemView.SingleSelection) # Seleccionar una fila a la vez
        self.tablaEntrenamiento.setColumnCount(3) # Establecer el número de columnas
        self.tablaEntrenamiento.setRowCount(0) # Establecer el número de filas        
        self.tablaEntrenamiento.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) # Alineación del texto del encabezado
        self.tablaEntrenamiento.setAlternatingRowColors(True) # Dibujar el fondo usando colores alternados
        self.tablaEntrenamiento.verticalHeader().setDefaultSectionSize(20) # Establecer altura de las filas
        nombreColumnas = ("Eje X","Eje Y", "Clase")
        self.tablaEntrenamiento.setHorizontalHeaderLabels(nombreColumnas) # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tablaEntrenamiento.horizontalHeader().setStretchLastSection(True) #Hace que el la fila de encabezado ocupe todo el ancho

        self.tablaPrueba.setDragDropOverwriteMode(False) # Deshabilitar el comportamiento de arrastrar y soltar
        self.tablaPrueba.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleccionar toda la fila
        self.tablaPrueba.setSelectionMode(QAbstractItemView.SingleSelection) # Seleccionar una fila a la vez
        self.tablaPrueba.setColumnCount(3) # Establecer el número de columnas
        self.tablaPrueba.setRowCount(0) # Establecer el número de filas        
        self.tablaPrueba.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) # Alineación del texto del encabezado
        self.tablaPrueba.setAlternatingRowColors(True) # Dibujar el fondo usando colores alternados
        self.tablaPrueba.verticalHeader().setDefaultSectionSize(20) # Establecer altura de las filas
        nombreColumnas = ("Eje X","Eje Y", "Clase")
        self.tablaPrueba.setHorizontalHeaderLabels(nombreColumnas) # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tablaPrueba.horizontalHeader().setStretchLastSection(True) #Hace que el la fila de encabezado ocupe todo el ancho

        # ======================================================

    def leerArchivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.nombre_fichero, _ = QFileDialog.getOpenFileName(self,'.csv', '~/Escritorio/','*.csv',options=options) #Lee archivo

        if self.nombre_fichero!='':  #Pregunta si es vacio(Se apreto cancel)
            self.archivo = read_ar(self.nombre_fichero, 80) #Llama a la funcion que lee el .csv
            self.tablaEntrenamiento.clearContents() #limpia la tabla
            self.ruta.setText(self.nombre_fichero)
            self.btnGenerar.setEnabled(True)  #Una vez cargado los datos activo el boton para generar
            self.btnGenerar.setStyleSheet('QPushButton {background-color: red; color: black;}')  #Le devuelvo color
            self.bloqueoClasificacion() #Boqueo el clasificador hasta que se genere el nuevo arbol

            #=================== Rellena la tabla Entrenamiento ==================
            row = 0
            for reg in self.archivo[1]:
                self.tablaEntrenamiento.setRowCount(row + 1)
                self.tablaEntrenamiento.setItem(row, 0, QTableWidgetItem(str(reg[0])))
                self.tablaEntrenamiento.setItem(row, 1, QTableWidgetItem(str(reg[1])))
                self.tablaEntrenamiento.setItem(row, 2, QTableWidgetItem(reg[2]))
                row += 1
            # ======================================================    

            self.tablaPrueba.clearContents() #limpia la tabla
            #=================== Rellena la tabla Prueba ==================
            row = 0
            for reg in self.archivo[3]:
                self.tablaPrueba.setRowCount(row + 1)
                self.tablaPrueba.setItem(row, 0, QTableWidgetItem(str(reg[0])))
                self.tablaPrueba.setItem(row, 1, QTableWidgetItem(str(reg[1])))
                self.tablaPrueba.setItem(row, 2, QTableWidgetItem(reg[2]))
                row += 1
            # ======================================================    

    def generarGraficos(self):

        print(self.limite.value()) #Para leer el valor del limite

        nodo=ab.Nodo() #Creo un nodo vacio
        self.arbol=principal(self.archivo, nodo)  #Llama a la funcion principal de apriory_exe que es el que genera los graficos
        img=mpimg.imread('grafica_desintegracion.png')
        plt.imshow(img)
        plt.figure()  #Crea otra ventana
        img2=mpimg.imread('Arbol_Decision.png')
        plt.imshow(img2)
        plt.show()
        self.btnClasificar.setEnabled(True)  #Una vez cargado los datos activo el boton para generar
        self.btnClasificar.setStyleSheet('QPushButton {background-color: blue; color: black;}')  #Le devuelvo color


    def clasificarPunto(self):
        clase = self.arbol.clasepunto(self.puntox.value(),self.puntoy.value())  #Llama a la funcion para clasificar el punto en Arbol
        msg = QMessageBox()  #Crea mensaje
        msg.setIcon(QMessageBox.Information)
        msg.setText("El punto "+str(self.puntox.value())+","+str(self.puntoy.value())+" es de la clase: " +str(clase))
        msg.setWindowTitle("Clasificacion de punto")
        msg.exec_()  #Muestra mensaje

    def bloqueoGeneracion(self):
        self.btnGenerar.setEnabled(False)
        self.btnGenerar.setStyleSheet('QPushButton {background-color: grey; color: black;}')

    def bloqueoClasificacion(self):
        self.btnClasificar.setEnabled(False)
        self.btnClasificar.setStyleSheet('QPushButton {background-color: grey; color: black;}')


#========== Inicia la App ============
app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()        
#======================================