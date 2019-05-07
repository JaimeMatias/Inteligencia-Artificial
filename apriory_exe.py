#-*- coding: latin-1 -*-
from Arbol import *
from ENTROPY import*
from copy import deepcopy
from READ import *
from GAIN import*
from grafica import*
#from Decimal import Decimal
def Apriory(archivo,atributos,arbol=None,i=0):
    entropiac=entropiaclase(archivo)
    if entropiac==0:
        print(len(archivo))
        nombre=clase(archivo)#funcion de ENTROPY
        nod1=Nodo(nombre,None,len(archivo),1,'si')

        arbol=nod1
        print(type(arbol))
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
            print('posici{on: }', posicion)
            print('ganancia eje x: ',var2)
            print('valor: ',valor)
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
            print('posici{on: }', posicion)
            print('ganancia eje y: ',var2)
            print('valor: ',valor)
            if var2>valor:
                valor=var2
                posicion[0]=1
                posicion[1]=corte

            corte=genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True
        #print(archivo[posicion[1]][posicion[0]])
        #print(archivo[posicion[1]+1][posicion[0]])
        posicion[2]=valorcorte(archivo,posicion[1],posicion[0])
        print(posicion[2])
        conjunto1=deepcopy(archivo[0:posicion[1]])
        conjunto2=deepcopy(archivo[posicion[1]:])
        nombre=atributos[posicion[0]]
        corte=posicion[2]
        #menor=('< '+str(posicion[2]))
        #mayor=('> '+str(posicion[2]))
        #print(menor)
        #print(posicion)

        if valor>0:
            nod2=Nodo(nombre,corte,len(archivo))
            arbol.genelemento(nod2)
            if conjunto1!=None:
                nod1=Nodo(nombre,None,None)
                nod1=Apriory(conjunto1,atributos,nod1)
                #print(nod1.nombre,nod1.cedula)
                print(type(nod1))
                arbol.agregarizq(nod1)
            if conjunto2!=None:
                nod1=Nodo(nombre,None,None)
                nod1=Apriory(conjunto2,atributos,nod1)
                arbol.agregarder(nod1)
                print(type(nod1))
        else:
            clase1=clase(archivo)
            confianza=float(round(confianzaclase(archivo,clase1),2))
            print('la confianza es: ',confianza)
            nod2=Nodo(clase1,None,len(archivo),confianza,'si')
            print('nodo del problema: ',nod2.nombre,nod2.corte,nod2.cedula)
            #arbol.genelemento(nod2)
            arbol=nod2
            print(type(nod2.izq))

        return(arbol)


"""PRUEBA """
import READ
Archivo=READ.read_ar('datos_continuo.csv')
#print(Archivo)
nodo=Nodo()
nodo=Apriory(Archivo[1],Archivo[0],nodo)
print('LISTA')
nodo.listar()
nodo.plot('prueba.png')
print('')
Prueba2=aBinarios()
Prueba2.agregar(nodo)
plot(Prueba2,'opcionrecursiva.png')
plotear(Archivo[1],nodo)
