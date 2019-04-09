#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal


def subconjunto(entrada,indice=0):
    final=0 #Variable de control utilizada para saber si estoy analizando atributos o clases
    devolver=[[],[],[]] #lo que va a devolver un arreglo de 3 posiciones donde cada una significa algo
                        #Primer posicoin elemento
                        #Segunda Posición valor
                        #Tercera Posción acierto
    if indice==0: #pregunta si el indice es 0, para saber si poner o no la variable de control a 1
        final=1
    else:
        indice=indice-1 #Decremento en 1 el indice por el tema de las posciones (empieza en 0w)
    elementos=[]
    Valor=[]
    acierto=[]
    for reg in entrada:
        if final==1:# Si final verdadedor tengo que ir a la ultima poscion
            indice=int(len(reg)-1) #obtengo la longitud del registro
        elem=reg[indice] #a elemento le asigno el contenido en esa posicion
        if elem not in elementos:
            elementos=elementos+[elem]# Si el elemento no esta en la lista, lo añado a la lista
            Valor.extend([0])# Creo una posicoin para adjudicar el elemento
            acierto.extend([[0,0]])# Creo otra posicion en el acierto
            #
        i=-1#lo inicio en -1 para que en el bucle no se pase del arreglo
        for pos in elementos: #sirve para incrementar los valores de valores y de atributos
            i=i+1
            if(pos==elem):# busco que el valor en posción final sea igual al contenido del vecto del elemento
                Valor[i]=Valor[i]+1# incremento el valor de la posicion
                if reg[len(reg)-1]=='yes':# Pregunto si  es si o no
                    acierto[i][0]=int(acierto[i][0])+1# Incremento el valor del acierto
                else:
                    acierto[i][1]=int(acierto[i][1])+1 #Incremento el alor del fallo
    devolver[0]=elementos
    devolver[1]=Valor
    devolver[2]=acierto
    print("Elementos: ",elementos)
    print("Valores: ",Valor)
    print("Aciertos: ",acierto)
    return devolver

# Me devuelve el nivel de entropia del conjunto
def entropy(entrada,indice=0):
    elementos=[] # Posee los valores distintos de los conjuntos
    Valor=[]# Posee la cantidad de veces que aparece cada atributo(En caso de que el indice sea 0 coincide con el Datributo)
    Datributo=[]#Posee la cantidad de veces que cada atributo coincide con cada elemeto de la clase
    subconj=subconjunto(entrada,indice)
    elementos=subconj[0]# se obtienen los elementos distintos
    Valor=subconj[1]#Se obtienen las cantidad de los atributos
    Datributo=subconj[2]#se obtiene la cantidad de veces que cada atributo coincide con cada elemeto
    resultado=0
    i=0
    if indice==0:
        for reg in Valor:
            c=int(reg)
            total=contar_tot(entrada)
            c=Decimal(c)/Decimal(total)
            resultado=resultado-float(c)*math.log(float(c),2)
        return resultado
    else:
        result=Decimal(0)
        for reg1 in Valor:
            total=Datributo[i][1]+Datributo[i][0]
            resultado=0
            for reg2 in Datributo[i]:
                c=Decimal(reg2)/Decimal(total)
                if c!=0:
                    resultado=resultado-float(c)*math.log(float(c),2)
            tot=contar_tot(entrada)
            result=result+(Decimal(reg1)/Decimal(tot))*Decimal(resultado)
            i=i+1
        return result


#Una simple función que cuenta la cantidad de registro
def contar_tot(entrada):
    total=0
    for reg in entrada:
        total=total+1
    return total
