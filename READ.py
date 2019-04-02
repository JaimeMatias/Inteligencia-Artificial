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
