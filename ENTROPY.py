#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal


def entropy(entrada,indice=0):
    total=0
    final=0
    if indice==0:
        final=1
    else:
        indice=indice-1

    elementos=[]
    Valor=[]
    for reg in entrada:
        if final==1:
            indice=int(len(reg)-1)
        last=reg[indice]
        i=-1
        if last not in elementos:
            elementos=elementos+[last]
            Valor.extend([1])
            total=total+1
        else:
            for pos in elementos:
                i=i+1
                if(pos==last):
                    Valor[i]=Valor[i]+1
                    total=total+1
    print(elementos)
    print(Valor)
    resultado=0
    for reg in Valor:
        c=int(reg)
        c=Decimal(c)/Decimal(total)
        resultado=resultado-float(c)*math.log(float(c),2)
        #print(resultado)
    return resultado
