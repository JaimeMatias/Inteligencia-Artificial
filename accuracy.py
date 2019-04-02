#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal


def accuracy(arg):
    total=0
    count=0
    with open(arg) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        elementos=[]
        Valor=[]
        for reg in entrada:
            indice=int(len(reg)-1)
            last=reg[indice]
            total=total+1
            if last=="yes":
                count=count+1
    c=Decimal(count)/Decimal(total)
    return(c)
