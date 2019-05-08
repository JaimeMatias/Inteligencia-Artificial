 #-*- coding: latin-1 -*-
import matplotlib.pyplot as plt
from READ import *
from decimal import Decimal
def puntos(entrada,clase):
    ejex=[]
    ejey=[]
    for registro in entrada:
        #pass
        #print(float(registro[0]),float(registro[1]))
        if registro[len(registro)-1]==clase:
            #print('entra')
            plt.scatter(float(registro[0]),float(registro[1]),c='red',marker="^")
        else:
            plt.scatter(float(registro[0]),float(registro[1]),c='blue')
            #ejex=ejex+[float(registro[0])]
            #ejey=ejey+[float(registro[1])]
    #return(ejex,ejey)
def cortes(arbol,limitex,limitey,restrix=[0,0],restriy=[0,0]):
    #print('limite que ingresa:',limitex)
    ancho=float(limitex[1])-float(limitex[0])
    alto=float(limitey[1])-float(limitey[0])
    if arbol.nombre=="'Eje y'":
        print(arbol.nombre,restrix,restriy,ancho)
        limi=0
        lims=1
        if restrix[0]!=0 :
            var=round((Decimal(restrix[0]-float(limitex[0]))),2)
            limi=Decimal(var)/Decimal(alto)
        if restrix[1]!=0:
            print(round((Decimal(restrix[1]-float(limitex[0]))),2))
            lims=((Decimal(restrix[1]-float(limitex[0]))/Decimal(alto)))
        #print(alto)
        print('limite inferior y: ',limi)
        print('limite Superior c: ',lims)
        plt.axhline(float(arbol.corte),limi,lims,color='r')
        if arbol.izq!=None:
            restriy=[0,arbol.corte]
            #print('restry izq',restriy)
            cortes(arbol.izq,limitex,limitey,restrix,restriy)
        if arbol.der!=None:
            restriy=[arbol.corte,limitey[1]]
            #print('restry der',restriy)
            cortes(arbol.der,limitex,limitey,restrix,restriy)

    if arbol.nombre=="'Eje x'":
        print(arbol.nombre,restrix,restriy)
        limi=0
        lims=1
        if restriy[0]!=0:
            limi=((Decimal(restriy[0]-float(limitey[0]))/Decimal(alto)))
        if restriy[1]!=0:
            lims=((Decimal(restriy[1]-float(limitey[0]))/Decimal(alto)))
        print('limite inferior x: ',limi)
        print('limite Superior x: ',lims)
        plt.axvline(float(arbol.corte),limi,lims,color='g')
        if arbol.izq!=None:
            restrix=[0,arbol.corte]
            #print('restry izq',restriy)
            cortes(arbol.izq,limitex,limitey,restrix,restriy)
        if arbol.der!=None:
            restrix=[arbol.corte,limitex[1]]

            #print('restry der',restriy)
            cortes(arbol.der,limitex,limitey,restrix,restriy)





        if arbol.izq!=None:
            cortes(arbol.izq,limitex,limitey,restrix,restriy)
        if arbol.der!=None:
            cortes(arbol.der,limitex,limitey,restrix,restriy)

def plotear(archivo,arbol):
    #print(archivo)
    puntos(archivo,'yes')
    limitex= extremos(archivo,0)
    limitey=extremos(archivo,1)
    #print('limite: ',limitex,type(limitex[0]),type(limitex[0]))
    minx=float(limitex[0])-0.5
    maxx=float(limitex[1])+0.5
    limitex=[minx,maxx]
    #print('maximo y minimo',maxx,minx)
    miny=float(limitey[0])-0.5
    maxy=float(limitey[1])+0.5
    limitey=[miny,maxy]
    #puntosno=puntos(archivo,'no')
    #print(puntosyes)
    #plt.scatter(puntosyes[0],puntosyes[1],'*r')
    plt.xlim(minx,maxx)
    plt.ylim(miny,maxy)
    restrix=[0,0]
    print(restrix)
    restriy=[0,0]
    cortes(arbol,limitex,limitey,restrix,restriy)
    #print('puntos')
    plt.savefig("grafica_desintegracion.png")
    plt.show()

"""PRUEBA"""
#from READ import *
#Archivo=read_ar('datos_continuo.csv')
#axvline(3,color='r')
#plt.scatter(1.5,4.5)  # Dibujamos un scatterplot de valores aleatorios
#plt.scatter(3,5)
#plt.show()
#plt.savefig("grafica_desintegracion.png")

#axhline(3,color='g')
#cortes(2)
#cortes(2)
#var2=conjuntos(Archivo[1],'no')
#print(var2)
#plot(var2[0],var2[1],'*')
#plot(var1[0],var1[1],'s')
