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



def decisionTree(Data,A=None,T=None):
    if ACCURACY.accuracy(Data)==1:
        print("funciona")
    #elif A=None:
    #    print("Entra en el elif")
    else:
        pruebatotal=ENTROPY.entropy(Data)
        print(pruebatotal)
        print(Data)
        archivo= Data
        longitud=archivo[0]
        contador=len(longitud)
        maximo=[0,0]
        for i in range(1,contador):
            print(i)
            incremento=GAIN.gain(Data,i)
            if incremento>maximo[1]:
                maximo[0]=i
                maximo[1]=incremento
        #if
        
        return maximo
