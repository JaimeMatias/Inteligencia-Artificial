#-*- coding: latin-1 -*-
 #!/usr/bin/python
import os, sys
import csv, operator
import READ
import math
import decimal
import decimal
from decimal import Decimal
import SOPORTE
from SOPORTE import support
import CONFIANZA
from CONFIANZA import confidence
import PASA_INICIAL
from PASA_INICIAL import int_pass
from CANDIDATO import candidato_gen
from CANDIDATO import subset

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
