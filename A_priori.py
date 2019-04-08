#-*- coding: latin-1 -*-
 #!/usr/bin/python
import os, sys
import csv, operator
import READ
import math
import copy
from copy import deepcopy
import decimal
from decimal import Decimal
import SUPPORT
from SUPPORT import support


def confidence(vector1,vector2,archivo):
    n=0
    count1=0
    count2=0
    for reg in archivo:
        bandera1=0
        bandera2=0
        for reg1 in vector1:
            if (reg1 in reg)!=True:
                bandera1=1
            if bandera1==0:
                count1=count1+1
        for reg2 in vector2:
            if (reg2 in reg)!=True:
                bandera2=1
            if bandera2==0:
                count2=count2+1
    total=Decimal(count1)/Decimal(count2)
    return total

def int_pass(entrada):
    a=0
    lista=[]
    for reg in entrada:

        for reg1 in reg:
            if reg1.strip() not in lista:
                lista+=[[]]
                lista[a]=reg1.strip()
                a=a+1
    lista.sort()
    return lista

def candidato_gen(vector,conjunto,iteracion):
    i=len(conjunto)
    conjunto+=[[]]
    conjunto2=[]
    k=0
    j=0
    for reg in vector:
        k=k+1
        if k<len(vector):

            for reg1 in vector[k:]:
                diferencia=0
                aux=[[],[]]
                aux[0]=deepcopy(reg)
                aux[1]=deepcopy(reg1)
                if type(aux[0])==list:
                    if(aux[0][len(aux[0])-2])==(aux[1][len(aux[1])-2]):
                        if(aux[0][len(aux[0])-1]!=aux[1][len(aux[1])-1]):
                            aux[0]+=[[]]
                            aux[0][len(aux[0])-1]=aux[1][len(aux[1])-1]
                            diferencia=1
                    if diferencia==1:
                        conjunto2+=[[]]
                        conjunto2[j]+=aux[0]
                        j=j+1

                if iteracion==2:
                    conjunto2+=[[]]
                    conjunto2[j]+=aux
                    j=j+1
    m=0
    for reg2 in conjunto2:
        bandera=subset(reg2,conjunto[i-1])
        if bandera==0:
            conjunto[i]+=[[]]
            conjunto[i][m]=reg2
            m=m+1
    return conjunto

def subset(vector,conjunto):
    bandera=0
    auxi=[]
    var=vector
    if len(vector)==2:
        for reg in vector:
            auxi=[[]]
            auxi[0]=reg
            if (auxi[0]) not in conjunto:
                bandera=1
    else:
        for i in range(0,len(vector)):
            pos=0
            auxi=[]
            for j in range(0,len(vector)):
                if i!=j:
                    auxi+=[[]]
                    auxi[pos]=vector[j]
                    pos=pos+1
            if auxi not in conjunto:
                bandera=1
    return bandera

def plot(vector):
    for i in range(0,len(vector)):
        print("Candidatos de longitud: ",i+1)
        print(vector[i])

def A_priori(entrada):
    FK=[[]]
    CK=[[]]
    C1=int_pass(entrada)
    i=0
    z=0
    CK[z]=C1
    j=0
    k=2
    for reg3 in CK[z]:
        if support(reg3,entrada)>=0.3:
            FK[j]+=[[]]
            FK[j][i]=reg3
            i=i+1
    while (not FK[j])==False and k>=2:
        z=z+1
        CK=candidato_gen(FK[j],CK,k)
        j=j+1
        FK+=[[]]
        k=k+1
        i=0
        for reg3 in CK[z]:
            if support(reg3,entrada)>=0.3:
                FK[j]+=[[]]
                FK[j][i]=reg3
                i=i+1
    FK.pop(len(FK)-1)
    plot(FK)
