 # !/usr/bin/python
 #  -*- coding: latin-1 -*-


import math as mt
import copy as cp
from Subconjunto import subconjunto as sb
import decimal as dc


def entropiaclase(archivo):
    """
    Calcula la entropia de la clase para un conjunto de datos

    :param archivo: el conjunto de datos
    :return:
    """
    subconjuntos_clase = sb.subconjuntoclase(archivo)
    valores_clases = cp.deepcopy(subconjuntos_clase[1])
    resultado: float = 0
    total = len(archivo)  # calculo la cantidad de registros
    for registros in valores_clases:
        if registros != 0:
            valor_parcial = dc.Decimal(registros) / dc.Decimal(total)  # divido
            resultado = resultado - float(valor_parcial) * mt.log(float(valor_parcial), 2)  # lo voy resguardando
    return round(resultado, 4)



def clase(archivo):
    """
    Me devuelve la clase en caso de ser una hoja pura
    Me devuelve la clase mas probable en caso de ser una hoja impura

    :param archivo: un conjunto de datos
    :return:
    """
    entropia_datos = entropiaclase(archivo)
    subconjuntos = sb.subconjuntoclase(archivo)
    if entropia_datos == 0:
        return subconjuntos[0][0]
    else:
        entropia_datos = 0

        i = 0
        clase= []
        for registros in subconjuntos[0]:

            if subconjuntos[1][i] > entropia_datos:
                clase = registros
                entropia_datos = subconjuntos[1][i]
            i = i + 1
        return clase #Devuelve la clase mas frecuente


# Función que recibe un conjunto de datos y un valor de la clase
# Genera la probabilidad de esa clase
def confianzaclase(archivo, clase):
    """Genera la probabilidad de esa clase

    :param archivo: El conjunto de Datos
    :param clase: la clase sobre las que se quier calcular la confianz
    :return:
    """
    confianza = 0
    total=len(archivo)
    for reg in archivo:
        if reg[len(reg) - 1] == clase:
            confianza = confianza + 1
    confianza = dc.Decimal(confianza) / dc.Decimal(total)
    return round(confianza, 4)
    pass


# Función que recibe un conjunto de datos y la posicion del atributo
# Genera la entropia de ese atributo
def entropiaatributo(archivo, atributo):
    """
    Calcula la entropia del conjunto de datos para ese atributo

    :param archivo: El conjunto de Datos
    :param atributo: El atributo
    :return:
    """
    subconjuntos = sb.subconjuntoatributo(archivo, atributo)
    entropia = cp.deepcopy(subconjuntos[1])
    totalelementos = len(archivo)
    total = 0
    for registro in entropia:
        denominador_parcial = 0
        for instancia in registro:
            denominador_parcial = denominador_parcial + instancia

        resultado_parcial = 0
        for instancia in registro:
            if instancia != 0:
                probabilidad = dc.Decimal(instancia) / dc.Decimal(denominador_parcial)
                resultado_parcial = resultado_parcial - float(probabilidad) * mt.log(float(probabilidad), 2)
        total = total + dc.Decimal(resultado_parcial) * dc.Decimal(denominador_parcial) / dc.Decimal(totalelementos)
    return round(total, 4)


# Una simple función que cuenta la cantidad de registro


"""PRUEBA """
# import READ
# Archivo=READ.read_ar('datos_continuo.csv')
# clases=clase(Archivo[1])
# clases=entropiaratio(Archivo[1],0)
# clases2=entropiaatributo(Archivo[1],0)
# Archivo=READ.read_ar('datos_continuo.csv')
# clases2=entropiaclase(Archivo[1])
# print(clases2)
