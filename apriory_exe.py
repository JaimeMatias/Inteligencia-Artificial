#-*- coding: latin-1 -*-
from Arbol import *
from ENTROPY import*
from copy import deepcopy
from READ import *
from GAIN import*
def Apriory(archivo,atributos,arbol=None,i=0):
    entropiac=entropiaclase(archivo)
    #print(entropiac)
    #print(len(archivo))
    if entropiac==0:
        #print(archivo)
        nombre=clase(archivo)#funcion de ENTROPY
        nod1=Nodo(nombre,i)
        #print(arbol.cedula)
        #print('antes hoja')
        #arbol.listar()
        #arbol.agregarele(nod1)
        #print('despues hoja')
        #arbol.listar()
        print('entra hoja')
        arbol=nod1
        #print('hoja:',nod1.nombre)
        #print('datos hoja: ',archivo)
        #print('nodo hoja: ',nod1)
        return(arbol)
    else:
        var4=['si','NO']
        posicion=[0,0,0]
        corte=0
        valor=0
        atributo=0
        control=False
        while control==False:
            var1=genintervalo(archivo,corte,atributo,var4)
            var2=gain(var1,atributo)
            if var2>valor:
                valor=var2
                posicion[1]=corte
            corte=genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True
        atributo=1
        corte=0
        control=False
        while control==False:
            var1=genintervalo(archivo,corte,atributo,var4)
            var2=gain(var1,atributo)
            if var2>valor:
                valor=var2
                posicion[0]=1
                posicion[1]=corte

            corte=genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True
        posicion[2]=archivo[posicion[1]][posicion[0]]
        #print('VAlor y Posicion:',valor,posicion)
        conjunto1=deepcopy(archivo[0:posicion[1]])
        conjunto2=deepcopy(archivo[posicion[1]:])
        #print('conjunto 1:',conjunto1)
        #print('conjunto 2:',conjunto2)
        nombre=atributos[posicion[0]]
        #print(nombre)
        nod2=Nodo(nombre,i)
        arbol.genelemento(nod2)
        #arbol.listar()
        #print('nodo 1:' ,nod1.nombre)
        if valor>0:
            #arbol.listar()
            #print('funciona')
            #print('nodo 1:' ,nod1.nombre)
            #print('nodo1: ',i,nod1.nombre,nod1)

            if conjunto1!=None:
                nod1=Nodo(nombre,i)
                print('entra conjunto izquierdo')
                print(conjunto1)
                nod1=Apriory(conjunto1,atributos,nod1,i+1)
                arbol.agregarizq(nod1)
                print('nod1 izquierda: ')
                nod1.listar()
                #print('nodo1 izquierda: ',i,nod1.nombre)
            if conjunto2!=None:
                nod1=Nodo(nombre,i)
                print(conjunto2)
                print('entra conjunto derecho')
                nod1=Apriory(conjunto2,atributos,nod1,i)
                arbol.agregarder(nod1)
                print('nodo1 derecha: ',i,nod1.nombre,nod1)
                nod1.listar()
        print('arbol: ',arbol)
        print('llego abajo')
        arbol.listar()
        #print(type(var1.der),'arbol.izq.der.nombre')
        return(arbol)


"""PRUEBA """
import READ
Archivo=READ.read_ar('datos_continuo.csv')
#print(Archivo)
nodo=Nodo()
nodo=Apriory(Archivo[1],Archivo[0],nodo)
print('LISTA')
#nodo.listar()
print('')
Prueba2=aBinarios()
Prueba2.agregar(nodo)
plot(Prueba2,'opcionrecursiva.png')
