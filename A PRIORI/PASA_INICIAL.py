#-*- coding: latin-1 -*-
 #!/usr/bin/python
import os, sys
import csv, operator

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
