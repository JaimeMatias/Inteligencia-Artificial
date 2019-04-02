#!/usr/bin/python
 #-*- coding: latin-1 -*-
import os, sys
import csv, operator
def suma(sumando1,sumando2):
    return sumando1+sumando2

def factorial(numero):
    if numero==0 or numero==1:
        return numero
    else:
        return(numero+factorial(numero-1))
    pass
