#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
from decimal import Decimal
from SUBCONJUNTO import *
from copy import deepcopy

# Me devuelve el nivel de entropia del conjunto
def entropiaclase(archivo):
    var1=subconjuntoclase(archivo)
    entro=deepcopy(var1[1])
    resultado=0
    total=contar_tot(archivo)#calculo la cantidad de registros
    for reg in entro:
        if reg!=0:
            c=Decimal(reg)/Decimal(total)#divido
            resultado=resultado-float(c)*math.log(float(c),2)#lo voy resguardando
    return resultado

def entropiaatributo(archivo,i):
    var1=subconjuntoatributo(archivo,i)
    entro=deepcopy(var1[1])
    totalelementos=contar_tot(archivo)
    total=0
    for reg in entro:
        denominador_parcial=0
        for reg2 in reg:
            denominador_parcial=denominador_parcial+reg2
        resultado_parcial=0
        for reg2 in reg:
            c=0
            if reg2!=0:
                c=Decimal(reg2)/Decimal(denominador_parcial)
                resultado_parcial=resultado_parcial-float(c)*math.log(float(c),2)
        total=total+Decimal(resultado_parcial)*Decimal(denominador_parcial)/Decimal(totalelementos)
    return(round(total,2))

def entropiaratio(archivo,i):
    var1=subconjuntoatributo(archivo,i)
    entro=deepcopy(var1[1])
    totalelementos=contar_tot(archivo)
    total=0
    for reg in entro:
        ocurrencia_atributo=0
        for reg2 in reg:
            ocurrencia_atributo=ocurrencia_atributo+reg2
        c=0
        if ocurrencia_atributo!=0:
            c=Decimal(ocurrencia_atributo)/Decimal(totalelementos)
        total=total-float(c)*math.log(float(c),2)
    return(round(total,2))

#Una simple función que cuenta la cantidad de registro
def contar_tot(entrada):
    total=0
    for reg in entrada:
        total=total+1
    return total
"""PRUEBA """
import READ
#Archivo=READ.read_ar('prestamo.csv')
#clases=entropiaratio(Archivo[1],0)
#clases2=entropiaatributo(Archivo[1],0)

#print(clases)
