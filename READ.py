#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class
import os, sys
import csv, operator
from copy import deepcopy
from decimal import Decimal
def read_ar(arg):
    archivo=[[],[]]#Posicion 1 titulos atributo, Posicion 2 registros
    pos=-1
    with open(arg) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            if pos==-1:
                archivo[0]=reg
            else:
                archivo[1]+=[[]]
                archivo[1][pos]=reg
            pos=pos+1
        return archivo

def read_at(entrada):
    archivo=[]
    pos=0
    for reg in entrada:
        atributo=[]

        posi=0
        for i in range(0,(len(reg)-1)):
            atributo+=[[]]
            atributo[posi]=reg[i]
            posi=posi+1
        print(atributo)
        archivo+=[[]]
        archivo[pos]=atributo
        pos=pos+1
    return archivo


def genintervalo(entrada,rango,atributo,nuevo_valor):
    var1=[]
    var2=[]
    var3=[]
    for i in range(0,rango):
        var3=deepcopy(entrada[i])
        var3[atributo]=nuevo_valor[0]
        var1=var1 +[var3]
    for i in range(rango,len(entrada)):
        var3=deepcopy(entrada[i])
        var3[atributo]=nuevo_valor[1]
        var1=var1+[var3]
    return(var1)


def genproxcorte(entrada, rango,atributo):
    control=False
    i=rango
    while control==False:
        #print('valor del indice: ',i)
        #print(entrada)
        var1=entrada[rango][atributo]
        var1=float(var1)
        var2=float(entrada[i][atributo])
        #print('atributo 1 ',var1,'atributo2 ',var2)
        if (var2-var1)!=0:
            #print('distintos')
            control=True
            return(i)
        i=i+1
        if i==len(entrada):
            control=True
            return(-1)
def valorcorte(entrada,rango,atributo):
    print('valor  para dividir',entrada[rango][atributo])
    print('valor  para dividir',entrada[rango-1][atributo])
    valor=Decimal(float(entrada[rango][atributo])+float(entrada[rango-1][atributo]))/2

    return round( valor,4)


"""Prueba"""
#Archivo=read_ar('datos_continuo.csv')
#var3=['si','no']
#for i in range(0,(len(Archivo))):
#    var1=genintervalo(Archivo[1],i,0,var3)
#    print(var1)

#var1=genintervalo(Archivo[1],0,1,var3)
#var1=genproxcorte(Archivo[1],5,1)
#print(var1)
#print(Archivo)
