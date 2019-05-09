 #-*- coding: latin-1 -*-
import matplotlib.pyplot as plt
from READ import *
from decimal import Decimal
def puntos(entrada,clase):
    ejex=[]
    ejey=[]
    for registro in entrada:
        if registro[len(registro)-1]==clase:
            plt.scatter(float(registro[0]),float(registro[1]),c='red',marker="^")
        else:
            plt.scatter(float(registro[0]),float(registro[1]),c='blue')

def cortes(arbol,limitex,limitey,restrix=[0,0],restriy=[0,0]):
    arbol.listar()
    print(arbol.nombre,arbol.izq,arbol.der)
    ancho=float(limitex[1])-float(limitex[0])
    alto=float(limitey[1])-float(limitey[0])
    if arbol.nombre=="'Eje y'":
        limi=0
        lims=1
        if restrix[0]!=0 :
            var=round((Decimal(restrix[0]-float(limitex[0]))),2)
            limi=round(Decimal(var)/Decimal(ancho),2)
        if restrix[1]!=0:
            var=round((Decimal(restrix[1]-float(limitex[0]))),2)
            lims=round(Decimal(var)/Decimal(ancho),2)
        plt.axhline(float(arbol.corte),limi,lims,color='r')
        if arbol.izq!=None:
            restriy=[0,arbol.corte]
            cortes(arbol.izq,limitex,limitey,restrix,restriy)
        if arbol.der!=None:
            restriy=[arbol.corte,limitey[1]]
            cortes(arbol.der,limitex,limitey,restrix,restriy)

    if arbol.nombre=="'Eje x'":
        limi=0
        lims=1
        if restriy[0]!=0:
            limi=((Decimal(restriy[0]-float(limitey[0]))/Decimal(alto)))
        if restriy[1]!=0:
            lims=((Decimal(restriy[1]-float(limitey[0]))/Decimal(alto)))
        plt.axvline(float(arbol.corte),limi,lims,color='g')
        if arbol.izq!=None:
            restrix=[0,arbol.corte]
            cortes(arbol.izq,limitex,limitey,restrix,restriy)
        if arbol.der!=None:
            restrix=[arbol.corte,limitex[1]]
            cortes(arbol.der,limitex,limitey,restrix,restriy)
def plotear(archivo,arbol):
    #arbol.listar()
    puntos(archivo,'yes')
    limitex= extremos(archivo,0)
    limitey=extremos(archivo,1)
    minx=float(limitex[0])-0.5
    maxx=float(limitex[1])+0.5
    limitex=[minx,maxx]
    miny=float(limitey[0])-0.5
    maxy=float(limitey[1])+0.5
    limitey=[miny,maxy]
    plt.xlim(minx,maxx)
    plt.ylim(miny,maxy)
    restrix=[0,0]
    restriy=[0,0]
    plt.xlabel('Eje X')        # Etiqueta del eje OX
    plt.ylabel('Eje Y')        # Etiqueta del eje OY
    plt.title('Grafico de Corte')    # Título del gráfico
    cortes(arbol,limitex,limitey,restrix,restriy)
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
