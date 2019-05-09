#-*- coding: latin-1 -*-
"""import Tkinter as tk
from Tkinter import ttk
from Tkinter import filedialog as fd
from READ import *

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Arbol de decisión para datos continuos")
        self.ventana1.geometry("350x400")  #Tamaño
        self.ventana1.resizable(0,0)
        self.ventana1.configure(background="light gray")

        self.texto1=tk.Label(self.ventana1, text="Seleccione el archivo donde se encuentra el conjunto de datos:", bg="black", fg="white")
        self.texto1.pack(fill=tk.X)

        self.btnCargar=tk.Button(self.ventana1, text="Cargar", command=self.abrirArchivo)
        self.btnCargar.pack(padx="20",pady="10")

        ############Crea Tabla################
        self.tv = ttk.Treeview(self.ventana1)
        self.tv['columns'] = ('Eje Y', 'Clase')
        self.tv.heading("#0", text='Eje X', anchor='center')
        self.tv.column("#0", anchor="center", width=70)
        self.tv.heading("Eje Y",text='Eje Y')
        self.tv.column("Eje Y", anchor="center", width=70)
        self.tv.heading("Clase",text='Clase')
        self.tv.column("Clase", anchor="center", width=70)
        self.Treeview = self.tv
        self.tv.pack(pady="8")
        ########################################

        self.btnGenArbol = tk.Button(self.ventana1, text="Generar Arbol de Decision")
        self.btnGenArbol.pack(pady="10")

        self.btnGen2D = tk.Button(self.ventana1, text="Generar Grafico 2D")
        self.btnGen2D.pack(padx="1",pady="1")

        self.ventana1.mainloop()

    def abrirArchivo(self):
        nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (('.csv', '.csv'),("todos los archivos","*.*")))
        if nombrearch!='':  #Si se apreto cancel devuelve String vacio ""

            ################# Muestra Archivo en tabla #####################
            archivo = read_ar(nombrearch)
            for reg in archivo[1]:
                self.tv.insert('', 'end', text=reg[0], values=(reg[1],reg[2]))
            ##############################################################

aplicacion1=Aplicacion()
"""
