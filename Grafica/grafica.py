# -*- coding: latin-1 -*-
from Arbol import arbol
import matplotlib.pyplot as plt
from Read import read as rd
from graphviz import Digraph, nohtml

# recibe un conjunto de datos y el valor de una clase
# a todos los regitros cuya clase coincida con la clase ingresada van a tener un tipo de representaci�n en el grafico
# al resto de registros van a tener otra representaci�n
def graficar_puntos(entrada, clase):
    """
    Grafica todos los puntos del conjunto de datos en un par de ejes cartesianos

    :param entrada: el conjunto de datos
    :param clase: la primer clse del conjunto
    :return:
    """
    for registro in entrada:
        #print(registro)
        if registro[len(registro) - 1] == clase:
            plt.scatter(float(registro[0]), float(registro[1]), c='red', marker="^")
        else:
            plt.scatter(float(registro[0]), float(registro[1]), c='blue')


# Funcion recursiva que recibe un nodo, los limtes del grafico tanto en x como en y, y las restricciones tanto en x como en y
# y genera las lineas de cortes
def graficar_diagrama_cortes_recursivo(arbol, limitex, limitey, restrix=None, restriy=None):
    """
    Genera las lineas de corte del diagrama de corte de manera recursiva

    :param arbol: el arbol de decision del problema
    :param limitex: los limites en x del grafico
    :param limitey: los limites en y del grafico
    :param restrix: el rango sobre el cual un conjunto o subconjunto de datos puede actuar en x
    :param restriy: el rango sobre el cual un conjunto o subconjunto de datos puede actuar en y
    :return:
    """
    if restriy is None:
        restriy = [limitey[0], limitey[1]]
    if restrix is None:
        restrix = [limitex[0], limitex[1]]
    if arbol.nombre == "Eje y":  # Pregunta si el corte es sobre el eje Y
        plt.hlines(float(arbol.corte),restrix[0],restrix[1] ,color='r')  # Funcion que plotea, recibe el valor del eje y en terminos relativos, donde comienza
        #plt.hlines(float(arbol.corte), limi, lims,

        # y donde termina la linea, los valores van de 0 a 1
        # Actualiza los valores y se llama recursivamente
        if arbol.izq is not None:
            if restriy[0]== limitey[0]:
               restriyn = [restriy[0], arbol.corte]
            if restriy[0]!=limitey[0]:
                restriyn=[restriy[0],arbol.corte]
            graficar_diagrama_cortes_recursivo(arbol.izq, limitex, limitey, restrix, restriyn)
        if arbol.der is not None:
            if restriy[1] == limitey[1]:
                restriyn = [arbol.corte,restriy[1]]
            if restriy[1]!=limitey[1]:
                restriyn=[arbol.corte,restriy[1]]
            graficar_diagrama_cortes_recursivo(arbol.der, limitex, limitey, restrix, restriyn)

    # Lo mismo para el eje X
    if arbol.nombre == "Eje x":
        plt.vlines(float(arbol.corte), restriy[0],restriy[1], color='g')
        if arbol.izq is not None:
            if restrix[0]==limitex[0]:
                restrixn=[restrix[0],arbol.corte]
            if restrix[0]!=limitex[0]:
                restrixn = [restrix[0], arbol.corte]
            graficar_diagrama_cortes_recursivo(arbol.izq, limitex, limitey, restrixn, restriy)
        if arbol.der is not None:
            restrixn = [arbol.corte, restrix[1]]
            graficar_diagrama_cortes_recursivo(arbol.der, limitex, limitey, restrixn, restriy)


# Funci�n que recibe los valores de las clases, el conjunto de datos del archivo, el nodo raiz y el nombre del archivo
# Genera el grafico de 2D con los cortes
def graficar_diagrama_cortes(clase, archivo, arbol, nombre):
    """
    Genera el grafico en 2 dimenciones de los puntos y las respetivas lineas de corte

    :param clase: la primer clase de los datos
    :param archivo: el conjunto de datos
    :param arbol: el arbol de decision del problema
    :param nombre: El nombre de los datos
    :return:
    """
    graficar_puntos(archivo, clase[0])  # plotea los puntos
    limitex = rd.extremos(archivo, 0)  # Establece los limites del grafico
    limitey = rd.extremos(archivo, 1)
    minx = float(limitex[0]) #- 0.5
    maxx = float(limitex[1]) #+ 0.5
    limitex = [minx, maxx]
    miny = float(limitey[0])# - 0.5
    maxy = float(limitey[1]) #+ 0.5
    limitey = [miny, maxy]
    #plt.xlim(minx, maxx)
    #plt.ylim(miny, maxy)
    graficar_diagrama_cortes_recursivo(arbol, limitex, limitey)  # Llama a la funcion Cortes
    plt.xlabel('Eje X')  # Etiqueta del eje OX
    plt.ylabel('Eje Y')  # Etiqueta del eje OY
    plt.title('Grafico de Corte')  # Título del gráfico

    plt.savefig(nombre)  # Guada el archivo


def graficar_arbol_recursivo(arbol, grafica, id):
    """    
    Genera de manera recusiva cada uno de los nodos y de las aristas del grafico de manera recursiva
    :param arbol: el arbol de decision del problema
    :param grafica: el grafico
    :param id: ID del nodo padre
    :return:
    """

    if arbol is not None and arbol.izq is not None:  # Pregunto  si es el nodo existe y si tiene hijo
        nodo_hijo = arbol.izq
        menor = ('< ' + str(arbol.corte))  # Genero las etiquetas de los arcos
        id_local = (str(nodo_hijo.nombre)+' ' + str(nodo_hijo.corte) + str(nodo_hijo.nivel)+'<')
        if nodo_hijo.hoja == 'si':  # Genero los 2 nodos origen destino, teniendo al nodo destino como hoja
            id_local = (str(nodo_hijo.nombre) +' '+ str(arbol.corte) + str(nodo_hijo.nivel)+'<')
            grafica.node(id_local, nohtml('<f1> '+ str(nodo_hijo.nombre)), color='green')
            grafica.edge(id, id_local, label=menor)
        else:  # Genero los 2 nodos origen destino, teniendo al nodo destino como nodo de decisi�n
            grafica.node(id_local, nohtml('<f1> '+ str(nodo_hijo.nombre)))
            grafica.edge(id, id_local, label=menor)
        graficar_arbol_recursivo(arbol.izq, grafica,id_local)
        # Lo mismo que el anterior
    if arbol is not None and arbol.der is not None:
        nodo_hijo = arbol.der
        mayor = ('> ' + str(arbol.corte))
        id_local = (str(nodo_hijo.nombre) +' '+ str(nodo_hijo.corte) + str(nodo_hijo.nivel)+'>')
        if nodo_hijo.hoja == 'si':
            id_local = (str(nodo_hijo.nombre)+' ' + str(arbol.corte) + str(nodo_hijo.nivel)+'>')
            grafica.node(id_local, nohtml('<f1> '+ str(nodo_hijo.nombre)), color='green')
            grafica.edge(id, id_local, label=mayor)
        else:
            grafica.node(id_local, nohtml('<f1> '+ str(nodo_hijo.nombre)))
            grafica.edge(id, id_local, label=mayor)
        graficar_arbol_recursivo(arbol.der, grafica, id_local)


def graficar_arbol(arbol, nombre):
    """
    Genero el grafico del arbol de deciones
    :param arbol: el arbol de decision del problema
    :param nombre: el nombre de la grafica
    :return:
    """
    grafica= Digraph('g', filename='btree.gv', node_attr={'shape': 'record', 'height': '.1'}, format='png')
    id = (str(arbol.nombre)+' ' + str(arbol.corte) + str(arbol.nivel))
    grafica.node(id, nohtml('<f1> '+ str(arbol.nombre)))
    graficar_arbol_recursivo(arbol, grafica, id)
    grafica.render(nombre)

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
