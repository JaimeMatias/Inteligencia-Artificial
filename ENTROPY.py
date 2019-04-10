#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal
from SUBCONJUNTO import subconjunto


# Me devuelve el nivel de entropia del conjunto
def entropy(entrada,indice=0):#El indice= 0indica que estamos analizando la clase, sino analizamos un atributo
    elementos=[] # Posee los valores distintos de los conjuntos
    Valor=[]# Posee la cantidad de veces que aparece cada atributo(En caso de que el indice sea 0 coincide con el Datributo)
    Datributo=[]#Posee la cantidad de veces que cada atributo coincide con cada elemeto de la clase
    subconj=subconjunto(entrada,indice)
    elementos=subconj[0]# se obtienen los elementos distintos
    Valor=subconj[1]#Se obtienen las cantidad de los atributos
    Datributo=subconj[2]#se obtiene la cantidad de veces que cada atributo coincide con cada elemeto
    resultado=0 #Lo que me va devolver la función
    i=0
    if indice==0:#Estamos analizando la clase
        for reg in Valor:
            c=int(reg)#transformo el valor a in integer
            total=contar_tot(entrada)#calculo la cantidad de registros
            c=Decimal(c)/Decimal(total)#divido
            resultado=resultado-float(c)*math.log(float(c),2)#lo voy resguardando
        return resultado
    else:#EStamos analizando los atributos
        result=Decimal(0)
        for reg1 in Valor:  #[10,5]
            total=Datributo[i][1]+Datributo[i][0] #el total ahora es sobre la ocurrencia del atributo
            resultado=0# cada valor de un atributo tiene su resultado particular
            for reg2 in Datributo[i]:#[[4,6],[5,0]]
                c=Decimal(reg2)/Decimal(total) #por la forma que se calcula la entropia, tengo que calcular para cada tipo del atributo
                if c!=0: #si no pregunto, me puede dar error matematico
                    resultado=resultado-float(c)*math.log(float(c),2)#parte de la form entropia
            tot=contar_tot(entrada)# el total de elementos
            result=result+(Decimal(reg1)/Decimal(tot))*Decimal(resultado) #parte de la formula entropia
            i=i+1
        return result


#Una simple función que cuenta la cantidad de registro
def contar_tot(entrada):
    total=0
    for reg in entrada:
        total=total+1
    return total
