# -*- coding: latin-1 -*-
import copy as cp
import read as rd


def subconjuntoclase(datos):
    """
    va a generar todos los subconjuntos de clases con su nombre y su cardinalidad
     El orden va a coincider con el orden en que aparecen en los datos.

    :type datos: arreglo con todos los datos
    :return: elements(un arreglo con los nombre de las clases), valor(un arreglo con las cardinalidades de los valores de las clases)
    """
    valor = []
    elements = []
    for reg in datos:
        elem = reg[len(reg) - 1]  # Posicion de la clase
        if elem not in elements:
            elements = elements + [elem]
            valor.extend([1])
        else:
            i = 0
            for pos in elements:
                if pos == elem:
                    valor[i] = valor[i] + 1
                i = i + 1
    return elements, valor


def subconjuntoatributo(datos, atributo):
    """
    va a generar un arreglo donde para cada valor del atributo, va a indicar que valores de clase tiene asociado y sus cardinalidades
    :param datos: arreglo con todos los datos
    :param atributo: posición del atributo a analizar
    :return:elementos(un arreglo con los valores del atributo
            valor(un arreglo con las cardinalidades para cada atributo de de los valores de las clases)
    """
    valor = []
    elementos = []
    clases = subconjuntoclase(datos)
    clasesdist = []
    for i in range(0, len(clases[1])):
        clasesdist.extend([0])  # sirve para determinar cuantas clases distintas hay
    for reg in datos:
        elem = reg[atributo]
        if elem not in elementos:
            elementos = elementos + [elem]
            valor.extend([cp.deepcopy(clasesdist)])
        j = 0
        for pos in elementos:  # bucle para encontrar la coincidencia
            # entre el valor del atributo, y la poscion que ocupa
            if pos == elem:
                i = 0
                for reg2 in clases[0]:  # bucle para encontrar la coincidencia entre el valor
                    # de la clase de ese atributo y la poscion que ocupa
                    if reg[len(reg) - 1] == reg2:
                        valor[j][i] = valor[j][i] + 1
                    i = i + 1
            j = j + 1

    return elementos, valor


"""PRUEBA """

"NECESARIO PARA TODAS LAS FUNCIONES"
Archivo = rd.read_ar('datos_continuo.csv')

"PRUEBA FUNCION SUBCONJUNTOCLASE"
# subconjunto=subconjuntoclase(Archivo[1])
# print(subconjunto)

"PRUEBA FUNCION SUBCONJUNTOATRIBUTO"
atributo=subconjuntoatributo(Archivo[1],0)
print(atributo)
