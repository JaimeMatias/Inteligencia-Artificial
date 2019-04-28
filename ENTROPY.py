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
    totalgeneral=contar_tot(archivo)
    totalparcial=0
    for reg in entro:
        resultado=0
        for reg2 in reg:
            resultado=resultado+reg2
        resultado4=0
        for reg2 in reg:
            c=0
            if reg2!=0:
                c=Decimal(reg2)/Decimal(resultado)
                resultado4=resultado4-float(c)*math.log(float(c),2)
        totalparcial=totalparcial+Decimal(resultado4)*Decimal(resultado)/Decimal(totalgeneral)
    return(round(totalparcial,2))

#Una simple función que cuenta la cantidad de registro
def contar_tot(entrada):
    total=0
    for reg in entrada:
        total=total+1
    return total
"""PRUEBA """
#import READ
#Archivo=READ.read_ar('prestamo.csv')
#clases=entropiaclase(Archivo[1])
#clases2=entropiaatributo(Archivo[1],0)

#print(clases2)
