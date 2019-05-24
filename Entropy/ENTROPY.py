 # !/usr/bin/python
 #  -*- coding: latin-1 -*-

import math as mt
import copy as cp
from Subconjunto import SUBCONJUNTO as sb
import decimal as dc


# Función que recibe el conjunto de datos
# Me devuelve el nivel de entropia del conjunto
def entropiaclase(archivo):
    var1 = sb.subconjuntoclase(archivo)
    entro = cp.deepcopy(var1[1])
    resultado = 0
    total = contar_tot(archivo)  # calculo la cantidad de registros
    for reg in entro:
        if reg != 0:
            c = dc.Decimal(reg) / dc.Decimal(total)  # divido
            resultado = resultado - float(c) * mt.log(float(c), 2)  # lo voy resguardando
    return resultado


# Recibe un conjunto de datos
# Me devuelve la clase en caso de ser una hoja pura
# Me devuelve la clase mas probable en caso de ser una hoja impura
def clase(archivo):
    entropi = entropiaclase(archivo)
    subconjunto = sb.subconjuntoclase(archivo)
    #print(subconjunto)
    if entropi == 0:
        return subconjunto[0][0]
    else:
        entropi = 0

        i = 0
        clase = []
        for reg in subconjunto[0]:

            if subconjunto[1][i] > entropi:
                clase = reg
                entropi = subconjunto[1][i]
            i = i + 1
        return clase


# Función que recibe un conjunto de datos y un valor de la clase
# Genera la probabilidad de esa clase
def confianzaclase(entrada, clase):
    cuenta = 0
    for reg in entrada:
        if reg[len(reg) - 1] == clase:
            cuenta = cuenta + 1
    cuenta = dc.Decimal(cuenta) / dc.Decimal(contar_tot(entrada))
    return cuenta
    pass


# Función que recibe un conjunto de datos y la posicion del atributo
# Genera la entropia de ese atributo
def entropiaatributo(archivo, atributo):
    var1 = sb.subconjuntoatributo(archivo, atributo)
    entro = cp.deepcopy(var1[1])
    totalelementos = contar_tot(archivo)
    total = 0
    for reg in entro:
        denominador_parcial = 0
        for reg2 in reg:
            denominador_parcial = denominador_parcial + reg2
        resultado_parcial = 0
        for reg2 in reg:
            c = 0
            if reg2 != 0:
                c = dc.Decimal(reg2) / dc.Decimal(denominador_parcial)
                resultado_parcial = resultado_parcial - float(c) * mt.log(float(c), 2)
        total = total + dc.Decimal(resultado_parcial) * dc.Decimal(denominador_parcial) / dc.Decimal(totalelementos)
    return round(total, 2)


# Funcion que recibe un conjunto de datos y la posición del atributo
"""
def entropiaratio(archivo,atributo):
    var1=sb.subconjuntoatributo(archivo,atributo)
    entro=cp.deepcopy(var1[1])
    totalelementos=contar_tot(archivo)
    total=0
    for reg in entro:
        ocurrencia_atributo=0
        for reg2 in reg:
            ocurrencia_atributo=ocurrencia_atributo+reg2
        c=0
        if ocurrencia_atributo!=0:
            c=dc.Decimal(ocurrencia_atributo)/dc.Decimal(totalelementos)
        total=total-float(c)*mt.log(float(c),2)
    return(round(total,2))
"""


# Una simple función que cuenta la cantidad de registro
def contar_tot(entrada):
    total = 0
    for reg in entrada:
        total = total + 1
    return total


"""PRUEBA """
# import READ
# Archivo=READ.read_ar('datos_continuo.csv')
# clases=clase(Archivo[1])
# clases=entropiaratio(Archivo[1],0)
# clases2=entropiaatributo(Archivo[1],0)
# Archivo=READ.read_ar('datos_continuo.csv')
# clases2=entropiaclase(Archivo[1])
# print(clases2)
