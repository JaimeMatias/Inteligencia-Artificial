#-*- coding: latin-1 -*-
from Read import read as rd
from Grafica import grafica as gf
from Gain import GAIN as gn
from Arbol import arbol as ab
from Entropy import ENTROPY as en
from copy import deepcopy


#from Decimal import Decimal
#Recibe el archivo, los atributos, la raiz y el nivel
#Genera el arbol aplicando el algoritmo aprendido en clase
def Apriory(archivo,atributos,arbol=None,nivel=0):
    entropiac=en.entropiaclase(archivo)
    if entropiac==0:
        nombre=en.clase(archivo)#funcion de ENTROPY
        nod1=ab.Nodo(nombre,None,nivel,len(archivo),1,'si')
        arbol=nod1
        return(arbol)
    else:
        var4=['conjunto 1','conjunto 2']
        posicion=[0,0,0]
        valor=0
        for i in range(0,2):
            corte=0
            atributo = i
            control = False
            archivo = rd.ordenar(archivo, atributo)

            while control == False:
                var1 = rd.genintervalo(archivo, corte, atributo, var4)
                var2 = gn.gain(var1, atributo)
                if var2 > valor:
                    valor = var2
                    if i==0:
                        posicion[1] = corte
                    else:
                        posicion[0] = 1
                        posicion[1] = corte
                corte = rd.genproxcorte(archivo, corte, atributo)
                if corte == -1:
                    control = True

        archivo=rd.ordenar(archivo,posicion[0])
        posicion[2]=rd.valorcorte(archivo,posicion[1],posicion[0])
        conjunto1=deepcopy(archivo[0:posicion[1]])
        conjunto2=deepcopy(archivo[posicion[1]:])
        nombre=atributos[posicion[0]]
        corte=posicion[2]
        if valor>0:
            nod2=ab.Nodo(nombre,corte,nivel,len(archivo))
            arbol.genelemento(nod2)
            if conjunto1!=None:
                nod1=ab.Nodo(nombre,None,None)
                nod1=Apriory(conjunto1,atributos,nod1,nivel+1)
                arbol.agregarizq(nod1)
            if conjunto2!=None:
                nod1=ab.Nodo(nombre,None,None)
                nod1=Apriory(conjunto2,atributos,nod1,nivel+1)
                arbol.agregarder(nod1)
        else:
            clase1=en.clase(archivo)
            confianza=float(round(en.confianzaclase(archivo,clase1),2))
            nod2=ab.Nodo(clase1,None,nivel,len(archivo),confianza,'si')
            arbol=nod2
        return(arbol)

def principal(archivo):
    Archivo = rd.read_ar(archivo)
    nodo = ab.Nodo()
    nivel = 0
    print('comienza')
    nodo = Apriory(Archivo[1], Archivo[0], nodo, nivel)
    print('LISTA')
    #hilo1 = th.Thread(target=gf.plotear, args=[Archivo[2], Archivo[1], nodo, 'grafica_desintegracion.png'])
    gf.plotear(Archivo[2], Archivo[1], nodo, 'grafica_desintegracion.png')
    nombre = 'Arbol_Decision.png'
    #hilo2 = th.Thread(target=ab.plot, args=[nodo, nombre])
    ab.plot(nodo, nombre)
    #hilo1.start()
    #hilo2.start()

principal('Pruebacsv.csv')
