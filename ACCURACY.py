#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal


def accuracy(entrada):
    total=0
    count=0
    for reg in entrada:
        indice=int(len(reg)-1)
        last=reg[indice]
        total=total+1
        if last=="yes":
            count=count+1
    c=Decimal(count)/Decimal(total)
    return(c)
