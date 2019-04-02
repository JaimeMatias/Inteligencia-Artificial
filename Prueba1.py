#!/usr/bin/python
 #-*- coding: latin-1 -*-
import os, sys
import csv, operator
a=0
lista=[]
with open('transac.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        a=a+1
        for reg1 in reg:
            aux1=0
            palabra=''
            print("reg1: ",reg1,len(reg1))
            for reg2 in reg1:
                aux=0
                print(reg2)
                if reg2!=",":
                    palabra=palabra+reg2
                else:
                    palabra=palabra.strip()
                    print(palabra)
                    for cand1 in lista:
                        print("la lista: ",lista)
                        print(cand1,(palabra==cand1))
                        if palabra==cand1:
                            aux=1
                            print("repetido: ",palabra)
                    if aux==0:
                        lista.append(palabra)
                    palabra=''
        print(a,reg,len(reg))  # Cada línea se muestra como una lista de campos
        print(lista)
        raw_input("ingrese enter para continuar")

final = raw_input("ingrese enter para continuar")
