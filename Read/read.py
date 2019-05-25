#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- Age,Has_job,Own_house,Credit_rating,Class
import os, sys
import csv, operator
import copy as cp
import decimal as dc


# from copy import cp.deepcopy
# from dc.Decimal import dc.Decimal
#
# Lee un archivo csv y devuelve un arreglo de 3 posciones
# La primera posicion tiene la lista de nombre de los atributos
# La segunda posicion tiene cada uno de los registros
# La tercera cada una de las clase
def read_ar(dataset):
    """
    Lee un archivo csv y devuelve un arreglo de 3 posciones
    :param archivo: un conjunto de datos
    :return:
    La primera posicion tiene la lista de nombre de los atributos
    La segunda posicion tiene cada uno de los registros
    La tercera cada una de las clase
    """
    archivo = [[], [], []]  # Posicion 1 titulos atributo, Posicion 2 registros
    pos = -1
    with open(dataset) as csvarchivo:
        datos = csv.reader(csvarchivo)
        for reg in datos:
            if pos == -1:
                archivo[0] = ['Eje x', 'Eje y', 'Clase:']
            else:
                archivo[1] += [[float(reg[0]), float(reg[1]), reg[2]]]
                if reg[len(reg) - 1] not in archivo[2]:
                    archivo[2] += [reg[len(reg) - 1]]
            pos = pos + 1
        return archivo


# funcion que lee un conjunto de datos y la posición de un atributo
# y los ordena por un atributo especifico
def ordenar(archivo, atributo):
    """
    lee un conjunto de datos y la posición de un atributo

    :param archivo: un conjunto de datos
    :param atributo: el atributo con el que se va a ordenar
    :return:
    """

    ordenado = sorted(archivo, key=lambda it: it[atributo])
    return ordenado


# funcion que va a recibir un conjunto de datos
# primero va a generar 2 subconnjuntos el primero de los registros de 0 a rango y el segundo
# de rango al liminte de archivo
# A todos los elemento del primer cojunto les va a asignar el mismo valor al atributo seleccionado
# A todos los elementos del segundo conjunto les va a asignar otro valor en el atributo seleccionado
# va a devolver ambos conjuntos
def genintervalo(archivo, rango, atributo, nuevo_valor):
    """
    funcion que va a recibir un conjunto de datos
    primero va a generar 2 subconnjuntos el primero de los registros de 0 a rango y el segundo
    de rango al liminte de archivo
    A todos los elemento del primer cojunto les va a asignar el mismo valor al atributo seleccionado
    A todos los elementos del segundo conjunto les va a asignar otro valor en el atributo seleccionado
    va a devolver ambos conjuntos

    :param archivo: un cojunto de datos
    :param rango: la cantidad de elementos que van a pertenecer al priemr conjunto
    :param atributo: el atributo que se va a sobre escribir
    :param nuevo_valor: el valor con el que se va a sobreescribir
    :return:
    """
    var1 = []
    for i in range(0, rango):
        var3 = cp.deepcopy(archivo[i])
        var3[atributo] = nuevo_valor[0]
        var1 = var1 + [var3]
    for i in range(rango, len(archivo)):
        var3 = cp.deepcopy(archivo[i])
        var3[atributo] = nuevo_valor[1]
        var1 = var1 + [var3]
    return var1


# funcion que va a recibir el conjunto de datos, el atributo a modificar y la posiciÃ³n
# del ultimo corte.
# En base a eso va a buscar cual es la proxima posicion para cortar
# si encuentra devuelve la poscion sino devuelve -1
def genproxcorte(archivo, desplazamiento, atributo):
    """
    va a buscar la proxima posición a cortar
    :param archivo: un conjunto de datos
    :param desplazamiento: el punto a partir de donde se busca
    :param atributo: el atributo que se analiza
    :return:
    """
    control = False
    i = desplazamiento
    while control is False:
        # print(len(archivo), i)
        var1 = archivo[desplazamiento][atributo]
        var1 = float(var1)
        var2 = float(archivo[i][atributo])
        # print(var1,var2)
        # print(archivo[i][2],archivo[desplazamiento][2])
        # print(archivo[i][2]!= archivo[desplazamiento][2])
        if archivo[i][2] != archivo[desplazamiento][2]:
            # print((var2 - var1) != 0)
            if (var2 - var1) != 0:
                return i
            i = i + 1
            if i == len(archivo):
                return -1

        else:
            i = i + 1
            if i == len(archivo):
                return -1


# Funcion que recibe el conjunto de datos, la posicion del corte y el atributos
# y devuelve el valor medio entre los 2 puntos donde se genera el corte, con los valore de
# ese atributo
def valorcorte(archivo, rango, atributo):
    """
    el promedio de los 2 valores de los puntos
    :param archivo: un conjunto de datos
    :param rango: la poscion donde se va a cortar
    :param atributo: el atributo a analizar
    :return:
    """
    valor = dc.Decimal(float(archivo[rango][atributo]) + float(archivo[rango - 1][atributo])) / 2
    return round(valor, 4)


# Función que va a recibir el conjunto de datos, y la posición del atributo
# y va a devolver el valor maximo y minimo de ese atributo.
def extremos(archivo, atributo):
    """
    devolver el valor maximo y minimo de ese atributo.
    :param archivo: un conjunto de datos
    :param atributo: la posicion del atributo
    :return:
    """
    max = 0.0
    min = 0.0
    for reg in archivo:
        if float(reg[atributo]) < min:
            min = float(reg[atributo])
        if float(reg[atributo]) > max:
            max = float(reg[atributo])
    return min, max


"""Prueba"""
# archivo=read_ar('datos_continuo.csv')
# atributo=read_at(archivo[1])
# print(atributo)
# var3=['si','no']
# for i in range(0,(len(Archivo))):
#    var1=genintervalo(Archivo[1],i,0,var3)
#    print(var1)

# var1=genintervalo(Archivo[1],0,1,var3)
# var1=genproxcorte(Archivo[1],5,1)
# print(var1)
# print(Archivo)
