#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class
import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal
import ACCURACY
import ENTROPY
import READ
import GAIN
from SUBCONJUNTO import subconjunto
from ARBOL import *

def decisionTree(Title,Data,arbol,cont=0,A=None,T=None):
    print(cont)
    print("estado ARbol: ",arbol)
    if ACCURACY.accuracy(Data)==1:# si el acierto es igual a 1, quiere decir que todos los elementos son de la misma clase
        print("funciona")
        return arbol
    else:# En caso de que no sea asi, entra aquí
        pruebatotal=ENTROPY.entropy(Data)
        print("prueba total: ",pruebatotal)
        #print(Data)
        archivo= Data
        longitud=archivo[0]
        contador=len(longitud)
        maximo=[0,0]
        for i in range(1,contador):
            incremento=GAIN.gain(Data,i)
            if incremento>maximo[1]:
                maximo[0]=i
                maximo[1]=incremento
        print(Title[maximo[0]-1],maximo[1]) #le reste 1 porque está todo desfasado
        if maximo[1]<0.40:
            return arbol
        else:
            nombre=Title[maximo[0]-1]
            nod=Nodo(nombre)
            arbol.agregar(nod)
            conjunto=[]
            conjunto=subconjunto(Data,maximo[0])
            print("maximo: ",conjunto[0])
            for reg in conjunto[0]:
                subconjunt=[]
                for reg1 in Data:
                    if reg1[maximo[0]-1]==reg:
                        subconjunt+=[reg1]
                print(subconjunt)
                arbol=decisionTree(Title,subconjunt,arbol,cont+1)
        #if
        return arbol

import READ
Archivo=READ.read_ar('prestamo.csv')
print(Archivo[0])
#entropy(Data,2)
ab= aBinarios()
print("tipo :",ab)
ab=decisionTree(Archivo[0],Archivo[1],ab)
print("tipo :",ab)
arreglo=ab.preorder(ab.getRaiz())
ar=limpiar(arreglo)
plot(ar,"decision.png")
