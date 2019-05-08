#!/usr/bin/python3.6
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal
import ENTROPY
from ENTROPY import *
def gain(entrada,i):
    data=entropiaclase(entrada)
    alternativa=entropiaatributo(entrada,i)
    ganancia=float(data)-float(alternativa)
    return round(ganancia,3)

def gainRatio(entrada,i):
    numerado=gain(entrada,i)
    denominador=entropiaratio(entrada,i)
    return(round((numerado/denominador),2))
"""PRUEBA"""
#import READ
#Archivo=READ.read_ar('datos_continuo.csv')
#clases0=gainRatio(Archivo[1],0)
#clases1=gainRatio(Archivo[1],1)
#clases2=gainRatio(Archivo[1],2)
#clases3=gainRatio(Archivo[1],3)
#clases2=entropiaatributo(Archivo[1],0)

#print('Entropia atributo 0: ',clases0)
#print('Entropia atributo 1: ',clases1)
#print('Entropia atributo 2: ',clases2)
#print('Entropia atributo 3: ',clases3)
