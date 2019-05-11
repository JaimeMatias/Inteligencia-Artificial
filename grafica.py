 #-*- coding: latin-1 -*-
import matplotlib.pyplot as plt
from read import *
import decimal as dc

def puntos(entrada,clase):
    ejex=[]
    ejey=[]
    for registro in entrada:
        if registro[len(registro)-1]==clase:
            plt.scatter(float(registro[0]),float(registro[1]),c='red',marker="^")
        else:
            plt.scatter(float(registro[0]),float(registro[1]),c='blue')

def cortes(arbol,limitex,limitey,restrix=[0,0],restriy=[0,0]):
    #arbol.listar()
    #print(arbol.nombre,arbol.izq,arbol.der)
    ancho=float(limitex[1])-float(limitex[0])
    alto=float(limitey[1])-float(limitey[0])
    if arbol.nombre=="'Eje y'":
        limi=0
        lims=1
        if restrix[0]!=0 :
            var=round((dc.Decimal(restrix[0]-float(limitex[0]))),2)
            limi=round(dc.Decimal(var)/dc.Decimal(ancho),2)
        if restrix[1]!=0:
            var=round((dc.Decimal(restrix[1]-float(limitex[0]))),2)
            lims=round(dc.Decimal(var)/dc.Decimal(ancho),2)
        plt.axhline(float(arbol.corte),limi,lims,color='r')
        if arbol.izq!=None:
            restriyn=[restriy[0],arbol.corte]
            cortes(arbol.izq,limitex,limitey,restrix,restriyn)
        if arbol.der!=None:
            restriyn=[arbol.corte,limitey[1]]
            cortes(arbol.der,limitex,limitey,restrix,restriyn)

    if arbol.nombre=="'Eje x'":
        limi=0
        lims=1
        if restriy[0]!=0:
            limi=((dc.Decimal(restriy[0]-float(limitey[0]))/dc.Decimal(alto)))
        if restriy[1]!=0:
            lims=((dc.Decimal(restriy[1]-float(limitey[0]))/dc.Decimal(alto)))
        plt.axvline(float(arbol.corte),limi,lims,color='g')
        if arbol.izq!=None:
            restrixn=[restrix[0],arbol.corte]
            cortes(arbol.izq,limitex,limitey,restrixn,restriy)
        if arbol.der!=None:
            restrixn=[arbol.corte,limitex[1]]
            cortes(arbol.der,limitex,limitey,restrixn,restriy)
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
