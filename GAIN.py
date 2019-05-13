#!/usr/bin/python3.6
 #-*- coding: latin-1 -*-
import ENTROPY as ep
#Función que recibe el conjunto de datos y la posicion de un atributo
#Genera la gananca de información de ese atributo
def gain(entrada,atributo):
    data=ep.entropiaclase(entrada)
    alternativa=ep.entropiaatributo(entrada,atributo)
    ganancia=float(data)-float(alternativa)
    return round(ganancia,3)

#Función que recibe el conjunto de datos y la posicion de un atributo
#Genera el Radio de Ganancia de ese atributo
"""def gainRatio(entrada,atributo):
    numerado=gain(entrada,atributo)
    denominador=ep.entropiaratio(entrada,atributo)
    return(round((numerado/denominador),2))"""
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
