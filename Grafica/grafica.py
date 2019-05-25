# -*- coding: latin-1 -*-
import pygraphviz as pgv
from Arbol import arbol
import matplotlib.pyplot as plt
from Read import read as rd


# recibe un conjunto de datos y el valor de una clase
# a todos los regitros cuya clase coincida con la clase ingresada van a tener un tipo de representaci�n en el grafico
# al resto de registros van a tener otra representaci�n
def puntos(entrada, clase):

    for registro in entrada:
        #print(registro)
        if registro[len(registro) - 1] == clase:
            plt.scatter(float(registro[0]), float(registro[1]), c='red', marker="^")
        else:
            plt.scatter(float(registro[0]), float(registro[1]), c='blue')


# Funcion recursiva que recibe un nodo, los limtes del grafico tanto en x como en y, y las restricciones tanto en x como en y
# y genera las lineas de cortes
def cortes(arbol, limitex, limitey, restrix=None, restriy=None):
    if restriy is None:
        restriy = [limitey[0], limitey[1]]
    if restrix is None:
        restrix = [limitex[0], limitex[1]]
    ancho = float(limitex[1]) - float(limitex[0])  # Establece el ancho de la grafica
    alto = float(limitey[1]) - float(limitey[0])  # Establece el alto de la grafica

    if arbol.nombre == "Eje y":  # Pregunta si el corte es sobre el eje Y
        limi = 0  # establece el limite inferior en 0
        lims = 1  # establece el limite superior en 1
        # Si tiene alguna restricci�n distinta de 0 hay que actualizar los limites
        if restrix[0] != 0:  #
            limi = (float(restrix[0]) - float(limitex[0])) / ancho
        if restrix[1] != 0:
            lims = (float(restrix[1]) - float(limitex[0])) / ancho
        plt.axhline(float(arbol.corte), limi, lims,
                    color='r')  # Funcion que plotea, recibe el valor del eje y en terminos relativos, donde comienza
        # y donde termina la linea, los valores van de 0 a 1
        # Actualiza los valores y se llama recursivamente
        if arbol.izq is not None:
            restriyn=[0,0]
            if restriy[0]== limitey[0]:
               restriyn = [restriy[0], arbol.corte]
               #print('LA restriccion: ', restriyn)
            if restriy[0]!=limitey[0]:
                restriyn=[restriy[0],arbol.corte]
                #print('LA restriccion: ',restriy,restriyn)
            #print('Eje y, izq: ',arbol.corte,restriyn)
            cortes(arbol.izq, limitex, limitey, restrix, restriyn)
        if arbol.der is not None:
            restriyn = [0, 0]
            if restriy[1] == limitey[1]:
                restriyn = [arbol.corte,restriy[1]]
            if restriy[1]!=limitey[1]:
                restriyn=[arbol.corte,restriy[1]]
            #print('Eje y, der: ',arbol.corte,restriyn)
            cortes(arbol.der, limitex, limitey, restrix, restriyn)
    # Lo mismo para el eje X
    if arbol.nombre == "Eje x":
        limi = 0
        lims = 1
        if restriy[0] != 0:
            limi = (float(restriy[0]) - float(limitey[0])) / alto
        if restriy[1] != 0:
            lims = (float(restriy[1]) - float(limitey[0])) / alto
        plt.axvline(float(arbol.corte), limi, lims, color='g')
        if arbol.izq is not None:
            restrixn=[0,0]
            if restrix[0]==limitex[0]:
                restrixn=[restrix[0],arbol.corte]
            if restrix[0]!=limitex[0]:
                restrixn = [restrix[0], arbol.corte]
            #print('Ejex, izq: ',arbol.corte,restrixn )
            cortes(arbol.izq, limitex, limitey, restrixn, restriy)
        if arbol.der is not None:
            restrixn = [0, 0]
            restrixn = [arbol.corte, restrix[1]]
            #print('Ejex, der: ',arbol.corte, restrixn)
            cortes(arbol.der, limitex, limitey, restrixn, restriy)


# Funci�n que recibe los valores de las clases, el conjunto de datos del archivo, el nodo raiz y el nombre del archivo
# Genera el grafico de 2D con los cortes
def plotear(clase, archivo, arbol, nombre):
    puntos(archivo, clase[0])  # plotea los puntos
    limitex = rd.extremos(archivo, 0)  # Establece los limites del grafico
    limitey = rd.extremos(archivo, 1)
    minx = float(limitex[0]) - 0.5
    maxx = float(limitex[1]) + 0.5
    limitex = [minx, maxx]
    miny = float(limitey[0]) - 0.5
    maxy = float(limitey[1]) + 0.5
    limitey = [miny, maxy]
    plt.xlim(minx, maxx)
    plt.ylim(miny, maxy)

    plt.xlabel('Eje X')  # Etiqueta del eje OX
    plt.ylabel('Eje Y')  # Etiqueta del eje OY
    plt.title('Grafico de Corte')  # Título del gráfico
    cortes(arbol, limitex, limitey)  # Llama a la funcion Cortes
    plt.savefig(nombre)  # Guada el archivo
    # plt.savefig("grafica_desintegracion.png")
    # plt.show()#Lo muestra


# Funcion recursiva que se recibe a si mismo y al grafico
    # genera todos los nodos y los arcos del grafico
def plot_recusivo(arbol,grafica):
    id = (str(arbol.nombre) + str(arbol.corte) + str(arbol.nivel))
    if arbol is not None and arbol.izq is not None:  # Pregunto  si es el nodo existe y si tiene hijo
        nodo_hijo = arbol.izq
        menor = ('< ' + str(arbol.corte))  # Genero las etiquetas de los arcos
        id_local = (str(nodo_hijo.nombre) + str(nodo_hijo.corte) + str(nodo_hijo.nivel))
        if nodo_hijo.hoja == 'si':  # Genero los 2 nodos origen destino, teniendo al nodo destino como hoja
            id_local = (str(nodo_hijo.nombre) + str(arbol.corte) + str(nodo_hijo.nivel))
            grafica.add_edge((id, arbol.soporte),
                               (id_local, nodo_hijo.soporte, nodo_hijo.confianza), label=menor)
        else:  # Genero los 2 nodos origen destino, teniendo al nodo destino como nodo de decisi�n
             grafica.add_edge((id, arbol.soporte,), (id_local, nodo_hijo.soporte),
                               label=menor, )
        plot_recusivo(arbol.izq,grafica)
        # Lo mismo que el anterior
    if arbol is not None and arbol.der is not None:
        nodo_hijo = arbol.der
        mayor = ('> ' + str(arbol.corte))
        id_local = (str(nodo_hijo.nombre) + str(nodo_hijo.corte) + str(nodo_hijo.nivel))
        if nodo_hijo.hoja == 'si':
            id_local = (str(nodo_hijo.nombre) + str(arbol.corte) + str(nodo_hijo.nivel))
            grafica.add_edge((id, arbol.soporte),(id_local, nodo_hijo.soporte, nodo_hijo.confianza), label=mayor)
        else:
            grafica.add_edge((id, arbol.soporte), (id_local, nodo_hijo.soporte),label=mayor)
        plot_recusivo(arbol.der,grafica)




def plot(arbol,nombre):
    grafica = pgv.AGraph(directed=True, label='Arbol Desicion')
    plot_recusivo(arbol,grafica)
    grafica.layout(prog='dot')
    grafica.draw(nombre)

"""PRUEBA"""
# from READ import *
# Archivo=read_ar('datos_continuo.csv')
# axvline(3,color='r')
# plt.scatter(1.5,4.5)  # Dibujamos un scatterplot de valores aleatorios
# plt.scatter(3,5)
# plt.show()
# plt.savefig("grafica_desintegracion.png")

# axhline(3,color='g')
# cortes(2)
# cortes(2)
# var2=conjuntos(Archivo[1],'no')
# print(var2)
# plot(var2[0],var2[1],'*')
# plot(var1[0],var1[1],'s')
