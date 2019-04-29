#-*- coding: latin-1 -*-
from Arbol import *
from ENTROPY import*
from copy import deepcopy
from READ import *
from GAIN import*
def Apriory(archivo,arbol=None,i=0):
    entropiac=entropiaclase(archivo)
    #print(entropiac)
    #print(len(archivo))
    if entropiac==0:
        nombre=clase(archivo)
        nod1=Nodo(nombre,i)
        arbol.agregar2(nod1)
        return(arbol)
    else:
        var4=['si','NO']
        posicion=[0,0]
        corte=0
        valor=0
        atributo=0
        control=False
        while control==False:
            var1=genintervalo(archivo,corte,atributo,var4)
            var2=gain(var1,atributo)
            if var2>=valor:
                valor=var2
                posicion[1]=corte
            #print('Posicion corte: ',i)
            #print(var1)
            #print(var2)
            corte=genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True
        #print('valor corte: ',corte)
        #for i in range(0,(len(archivo))+1):
        atributo=1
        corte=0
        control=False
        while control==False:
            var1=genintervalo(archivo,corte,atributo,var4)
            var2=gain(var1,atributo)
            #print(var1)
            #print(var2)
            if var2>=valor:
                valor=var2
                posicion[0]=1
                posicion[1]=corte
            #print('Posicion corte: ',i)
            #print(var1)
            #print(var2)
            corte=genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True

        print(valor,posicion)


        #print(var2)

"""PRUEBA """
import READ
Archivo=READ.read_ar('datos_continuo.csv')
print(Archivo)
nodo=Nodo()
Apriory(Archivo[1],nodo)
#print(nodo)
