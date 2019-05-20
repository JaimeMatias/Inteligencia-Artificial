# coding=utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView
from PyQt5 import uic
from PyQt5.QtCore import Qt
from Read.read import read_ar
from Desicion.apriory2 import principal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import img_rc


class Ventana(QMainWindow):
    def __init__(self):
        global nombre_fichero
        QMainWindow.__init__(self)
        uic.loadUi("ventana1.ui",self)
        self.btnBuscar.clicked.connect(self.leerArchivo)
        self.btnGenerar.clicked.connect(self.generarGraficos)

        # ================== Configurar Tabla ==================

        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers) # Deshabilitar edición
        self.tabla.setDragDropOverwriteMode(False) # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows) # Seleccionar toda la fila
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection) # Seleccionar una fila a la vez
        self.tabla.setColumnCount(3) # Establecer el número de columnas
        self.tabla.setRowCount(0) # Establecer el número de filas        
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) # Alineación del texto del encabezado
        self.tabla.setAlternatingRowColors(True) # Dibujar el fondo usando colores alternados
        self.tabla.verticalHeader().setDefaultSectionSize(20) # Establecer altura de las filas
        nombreColumnas = ("Eje X","Eje Y", "Clase")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas) # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.horizontalHeader().setStretchLastSection(True) #Hace que el la fila de encabezado ocupe todo el ancho

        # ======================================================

    def leerArchivo(self):
        self.nombre_fichero, _ = QFileDialog.getOpenFileName(self,'.csv', '~/Escritorio/','*.csv') #Lee archivo

        if self.nombre_fichero!='':  #Pregunta si es vacio(Se apreto cancel)
            archivo = read_ar(self.nombre_fichero) #Llama a la funcion que lee el .csv
            self.tabla.clearContents() #limpia la tabla
            self.ruta.setText(self.nombre_fichero)

            #=================== Rellena la tabla ==================
            row = 0
            for reg in archivo[1]:
                self.tabla.setRowCount(row + 1)
                self.tabla.setItem(row, 0, QTableWidgetItem(reg[0]))
                self.tabla.setItem(row, 1, QTableWidgetItem(reg[1]))
                self.tabla.setItem(row, 2, QTableWidgetItem(reg[2]))
                row += 1
            # ======================================================    

    def generarGraficos(self):
        principal(self.nombre_fichero)  #Llama a la funcion principal de apriory_exe que es el que genera los graficos
        img=mpimg.imread('grafica_desintegracion.png')
        plt.imshow(img)
        plt.figure()  #Crea otra ventana
        img2=mpimg.imread('Arbol_Decision.png')
        plt.imshow(img2)
        plt.show()


#========== Inicia la App ============
app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()        
#======================================