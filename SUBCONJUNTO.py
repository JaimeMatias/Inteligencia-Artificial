#!/usr/bin/python
 #-*- coding: latin-1 -*-
import os, sys
from copy import deepcopy
#Devuelve los subconj de ese atributo

def subconjuntoclase(datos):
    Valor=[]
    elementos=[]
    for reg in datos:
        elem=reg[len(reg)-1] #Posicion de la clase
        if elem not in elementos:
            elementos=elementos+[elem]
            Valor.extend([1])
        else:
            i=0
            for pos in elementos:
                if pos==elem:
                    Valor[i]=Valor[i]+1
                i=i+1
    return(elementos,Valor)

def subconjuntoatributo(datos,k):
    Valor=[]
    elementos=[]
    var=subconjuntoclase(datos)
    var3=[]
    for i in range(0,len(var[1])):
        var3.extend([0])
    for reg in datos:
        elem=reg[k]
        if elem not in elementos:
            elementos=elementos+[elem]
            Valor.extend([deepcopy(var3)])
        j=0
        for pos in elementos:
            if pos==elem:
                i=0
                for reg2 in var[0]:
                    if reg[len(reg)-1]==reg2:
                        Valor[j][i]=Valor[j][i]+1
                    i=i+1
            j=j+1

    return(elementos,Valor)


"""PRUEBA """
#import READ
#Archivo=READ.read_ar('datos_continuo.csv')
#Archivo2=READ.read_ar('prestamo.csv')
#clases=subconjuntoclase(Archivo[1])
#clases2=subconjuntoatributo(Archivo2[1],0)
#print(clases)
#print('hola')
#print(clases2)
#clases3=subconjuntoatributo(Archivo[1],0)
#print(clases3)
