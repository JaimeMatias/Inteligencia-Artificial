#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal


def entropy(entrada,indice=0):
    elementos=[]
    Valor=[]
    subconj=subconjunto(entrada,indice)
    Datributo=[]
    elementoe=subconj[0]
    Valor=subconj[1]
    Datributo=subconj[2]
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



def contar_tot(entrada):
    total=0
    for reg in entrada:
        total=total+1
    return total


def subconjunto(entrada,indice=0):
    total=0
    final=0
    devolver=[[],[],[]]
    if indice==0:
        final=1
    else:
        indice=indice-1
    elementos=[]
    Valor=[]
    acierto=[]
    for reg in entrada:
        if final==1:
            indice=int(len(reg)-1)
        elem=reg[indice]
        i=-1
        if elem not in elementos:
            elementos=elementos+[elem]
            Valor.extend([0])
            acierto.extend([[0,0]])
        for pos in elementos:
            i=i+1
            if(pos==elem):
                Valor[i]=Valor[i]+1
                if reg[len(reg)-1]=='yes':
                    acierto[i][0]=int(acierto[i][0])+1
                else:
                    acierto[i][1]=int(acierto[i][1])+1
    devolver[0]=elementos
    devolver[1]=Valor
    devolver[2]=acierto
    #print(elementos)
    #print(Valor)
    #print(acierto)
    return devolver
