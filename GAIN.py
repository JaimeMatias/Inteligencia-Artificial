#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal
import ENTROPY

def gain(entrada,indice=0):
    data=ENTROPY.entropy(entrada)
    alternativa=ENTROPY.entropy(entrada,indice)
    ganancia=float(data)-float(alternativa)
    return ganancia
