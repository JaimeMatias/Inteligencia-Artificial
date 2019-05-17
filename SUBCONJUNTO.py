#!/usr/bin/python
 #-*- coding: latin-1 -*-
import os, sys
import copy as cp
import read as rd

#Recibe un archivo y devuelve un arreglo, donde para cada elemento de la clase, indica la cantidad de ocurrencias que tiene
#dentro del archivo
#El orden va a coincider con el orden en que aparecen en los datos.
def subconjuntoclase(datos):
    Valor=[]
    elementos=[]
    for reg in datos:
        elem=reg[len(reg)-1] #Posicion de la clase
        if elem not in elementos:
            elementos=elementos+[elem]
            Valor.extend([1])
        else:
            i=0
            for pos in elementos:
                if pos==elem:
                    Valor[i]=Valor[i]+1
                i=i+1
    return(elementos,Valor)


#Recibe un archivo y la posición del atributo
# y devuelve un arreglo, donde para cada valor del atributo, indica la cantidad de ocurrencias de cada
#clase que posee
def subconjuntoatributo(datos,atributo):
    Valor=[]
    elementos=[]
    clases=subconjuntoclase(datos)
    clasesdist=[]
    for i in range(0,len(clases[1])):
        clasesdist.extend([0])  #  sirve para determinar cuantas clases distintas hay
    for reg in datos:
        elem=reg[atributo]
        if elem not in elementos:
            elementos=elementos+[elem]
            Valor.extend([cp.deepcopy(clasesdist)])
        j=0
        for pos in elementos:# bucle para encontrar la coincidencia entre el valor del atributo, y la poscion que ocupa
            if pos==elem:
                i=0
                for reg2 in clases[0]: #bucle para encontrar la coincidencia entre el valor de la clase de ese atributo y la poscion que ocupa
                    if reg[len(reg)-1]==reg2:
                        Valor[j][i]=Valor[j][i]+1
                    i=i+1
            j=j+1

    return(elementos,Valor)


"""PRUEBA """

"NECESARIO PARA TODAS LAS FUNCIONES"
#Archivo=rd.read_ar('datos_continuo.csv')

"PRUEBA FUNCION SUBCONJUNTOCLASE"
#subconjunto=subconjuntoclase(Archivo[1])
#print(subconjunto)

"PRUEBA FUNCION SUBCONJUNTOATRIBUTO"
#atributo=subconjuntoatributo(Archivo[1],0)
#print(atributo)
