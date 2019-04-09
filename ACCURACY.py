#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal

"""Recibe como entrada un archivo, y por cada registro del archivo pregunt si el valor del ultimo campo
es si, y devuelve el porcentaje de acierto"""
def accuracy(entrada):#ARCHIVO DE ENTRADA
    total=0#CONTADOR TOTAL DE REGISTRO
    count=0#CONTADOR TOTAL DE ACIERTO
    for reg in entrada:#POR CADA REGISTRO:
        indice=int(len(reg)-1)
        last=reg[indice]#OBTENGO EL VALOR DE LA ULTIMA POSICION
        total=total+1#incremento EL TOTAL DE REGISTRO
        if last=="yes":#PREGUNTO
            count=count+1# Si es SI, incrementeo e CONTADOR de ACIERTO
    c=Decimal(count)/Decimal(total)# Calculo el cociente
    return(c)# devuelvo dicho cociente
