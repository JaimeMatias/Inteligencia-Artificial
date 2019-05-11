#-*- coding: latin-1 -*-
import matplotlib.pyplot as plt
import READ as rd
import grafica as gf
import GAIN as gn
import Arbol as ab
import ENTROPY as en

from copy import deepcopy


#from Decimal import Decimal
def Apriory(archivo,atributos,arbol=None,i=0):
    entropiac=en.entropiaclase(archivo)
    if entropiac==0:
        nombre=en.clase(archivo)#funcion de ENTROPY
        nod1=ab.Nodo(nombre,None,len(archivo),1,'si')
        arbol=nod1
        return(arbol)
    else:
        var4=['si','NO']
        posicion=[0,0,0]
        corte=0
        valor=0
        atributo=0
        control=False
        archivo=rd.ordenar(archivo,atributo)
        while control==False:
            var1=rd.genintervalo(archivo,corte,atributo,var4)
            var2=gn.gain(var1,atributo)
            if var2>valor:
                valor=var2
                posicion[1]=corte
            corte=rd.genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True
        atributo=1
        corte=0
        control=False
        archivo=rd.ordenar(archivo,atributo)
        while control==False:
            var1=rd.genintervalo(archivo,corte,atributo,var4)
            var2=gn.gain(var1,atributo)
            if var2>valor:
                valor=var2
                posicion[0]=1
                posicion[1]=corte

            corte=rd.genproxcorte(archivo,corte,atributo)
            if corte==-1:
                control=True
        archivo=rd.ordenar(archivo,posicion[0])
        posicion[2]=rd.valorcorte(archivo,posicion[1],posicion[0])
        conjunto1=deepcopy(archivo[0:posicion[1]])
        conjunto2=deepcopy(archivo[posicion[1]:])
        nombre=atributos[posicion[0]]
        corte=posicion[2]
        #print('entropia: ',entropiac)
        #print('valor: ',valor)
        if valor>0:
            nod2=ab.Nodo(nombre,corte,len(archivo))
            arbol.genelemento(nod2)
            if conjunto1!=None:
                nod1=ab.Nodo(nombre,None,None)
                nod1=Apriory(conjunto1,atributos,nod1)
                arbol.agregarizq(nod1)
            if conjunto2!=None:
                nod1=ab.Nodo(nombre,None,None)
                nod1=Apriory(conjunto2,atributos,nod1)
                arbol.agregarder(nod1)
        else:
            clase1=en.clase(archivo)
            confianza=float(round(en.confianzaclase(archivo,clase1),2))
            nod2=ab.Nodo(clase1,None,len(archivo),confianza,'si')
            arbol=nod2
        return(arbol)


"""PRUEBA """
Archivo=rd.read_ar('Pruebacsv.csv')
#print(Archivo)
nodo=ab.Nodo()
nodo=Apriory(Archivo[1],Archivo[0],nodo)
#nodo.listar()
print('LISTA')
nodo.plot('prueba.png')
gf.plotear(Archivo[1],nodo)
