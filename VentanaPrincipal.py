# coding=utf-8
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from Read.read import read_ar
from Desicion.desicion import principal, probar_arbol
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import img_rc
from Arbol import arbol as ab


class Ventana(QMainWindow):
    def __init__(self):
        global archivo
        global arbol
        QMainWindow.__init__(self)
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        uic.loadUi(os.path.join(base_path, "ventana1.ui"), self)
        self.btnBuscar.clicked.connect(self.leerArchivo)
        self.btnGenerar.clicked.connect(self.generarGraficos)
        self.btnClasificar.clicked.connect(self.clasificarPunto)
        self.btnTrainToTest.clicked.connect(self.trainToTest)
        self.btnTestToTrain.clicked.connect(self.testToTrain)
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
        self.tablaEntrenamiento.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tablaEntrenamiento.setEditTriggers(QAbstractItemView.NoEditTriggers) # No editable
        # self.tablaEntrenamiento.horizontalHeader().setStretchLastSection(True) #Hace que el la fila de encabezado ocupe todo el ancho

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
        self.tablaPrueba.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tablaPrueba.setEditTriggers(QAbstractItemView.NoEditTriggers) # No editable

        # ======================================================

    def leerArchivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.nombre_fichero, _ = QFileDialog.getOpenFileName(self,'.csv ;; .txt', '~/Escritorio/','*.csv;; *.txt',options=options) #Lee archivo

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

        nodo = ab.Nodo() #Creo un nodo vacio
        if len(self.archivo[1]) == 0:
            mensaje = "No hay datos de entrenamiento para generar el árbol."
            self.mostrarMensaje("Error",mensaje)
            return

        self.arbol = principal(self.archivo, nodo , self.limite.value()/100)  #Llama a la funcion principal de apriory_exe que es el que genera los graficos
        
        ########## Prueba el arbol y muestra la eficiencia ##################
        eficienciaEntr = probar_arbol(self.archivo[1], self.arbol)
        mensaje = "Se entrenó con una eficiencia del: "+ str(round(eficienciaEntr,2))+"% \n"
        if len(self.archivo[3]) > 0:
            eficienciaPrueba = probar_arbol(self.archivo[3], self.arbol)
            mensaje += "Se probó con una eficiencia del: "+ str(round(eficienciaPrueba,2))+"%"
        self.mostrarMensaje("Eficiencia del Arbol de Decision",mensaje)

        self.btnClasificar.setEnabled(True)  #Una vez cargado los datos activo el boton para generar
        self.btnClasificar.setStyleSheet('QPushButton {background-color: blue; color: black;}')  #Le devuelvo color

    def clasificarPunto(self):
        clase = self.arbol.clasepunto(self.puntox.value(),self.puntoy.value())  #Llama a la funcion para clasificar el punto en Arbol
        mensaje = "El punto x:"+str(self.puntox.value())+" y:"+str(self.puntoy.value())+" es de la clase: " +str(clase)
        self.mostrarMensaje("Clasificiacion del punto",mensaje)
        
    def trainToTest(self):
        indexes = self.tablaEntrenamiento.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            count = self.tablaPrueba.rowCount()
            self.tablaPrueba.insertRow(count)
            self.tablaPrueba.setItem(count, 0, QTableWidgetItem(self.tablaEntrenamiento.item(row, 0).text()))
            self.tablaPrueba.setItem(count, 1, QTableWidgetItem(self.tablaEntrenamiento.item(row, 1).text()))
            self.tablaPrueba.setItem(count, 2, QTableWidgetItem(self.tablaEntrenamiento.item(row, 2).text()))
            self.tablaEntrenamiento.removeRow(row)
        if indexes:
            self.archivo[3].append(self.archivo[1][row])
            del self.archivo[1][row]

    def testToTrain(self):
        indexes = self.tablaPrueba.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            count = self.tablaEntrenamiento.rowCount()
            self.tablaEntrenamiento.insertRow(count)
            self.tablaEntrenamiento.setItem(count, 0, QTableWidgetItem(self.tablaPrueba.item(row, 0).text()))
            self.tablaEntrenamiento.setItem(count, 1, QTableWidgetItem(self.tablaPrueba.item(row, 1).text()))
            self.tablaEntrenamiento.setItem(count, 2, QTableWidgetItem(self.tablaPrueba.item(row, 2).text()))
            self.tablaPrueba.removeRow(row)
        if indexes:
            self.archivo[1].append(self.archivo[3][row])
            del self.archivo[3][row]        

    def bloqueoGeneracion(self):
        self.btnGenerar.setEnabled(False)
        self.btnGenerar.setStyleSheet('QPushButton {background-color: grey; color: black;}')

    def bloqueoClasificacion(self):
        self.btnClasificar.setEnabled(False)
        self.btnClasificar.setStyleSheet('QPushButton {background-color: grey; color: black;}')

    def mostrarMensaje(self, titulo, mensaje):
        msg = QMessageBox()  #Crea mensaje
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle(titulo)
        msg.exec_()  #Muestra mensaje


#========== Inicia la App ============
app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()        
#======================================
