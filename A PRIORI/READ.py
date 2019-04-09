#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class
import os, sys
import csv, operator

def read_ar(arg):
    archivo=[]
    pos=0
    with open(arg) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            archivo+=[[]]
            archivo[pos]=reg
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
