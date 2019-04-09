#-*- coding: latin-1 -*-
 #!/usr/bin/python
import os, sys
import copy
from copy import deepcopy
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
