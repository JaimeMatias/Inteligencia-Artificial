#!/usr/bin/python3.6
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class

import os, sys
import csv, operator
import math
import decimal
from decimal import Decimal
import ENTROPY
from ENTROPY import entropy
def gain(entrada,indice=0):
    data=entropy(entrada)
    alternativa=entropy(entrada,indice)
    ganancia=float(data)-float(alternativa)
    return ganancia
