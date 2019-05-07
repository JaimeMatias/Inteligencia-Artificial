 #-*- coding: latin-1 -*-
import matplotlib.pyplot as plt
def puntos(entrada,clase):
    ejex=[]
    ejey=[]
    for registro in entrada:
        #pass
        print(float(registro[0]),float(registro[1]))
        if registro[len(registro)-1]==clase:
            print('entra')
            plt.scatter(float(registro[0]),float(registro[1]),c='red',marker="^")
        else:
            plt.scatter(float(registro[0]),float(registro[1]),c='blue')
            #ejex=ejex+[float(registro[0])]
            #ejey=ejey+[float(registro[1])]
    #return(ejex,ejey)
def cortes(arbol,min=0,max=0):
    print(arbol.nombre)
    print(type(arbol.corte))
    print(min)
    print(max)
    #plt.axhline(1.35, color = 'g')  # Dibujamos una línea vertical verde centrada en x = -0.5

    if arbol.nombre=="'Eje y'":
        print('entra')
        print('Valor Corte: ',arbol.corte)

        plt.axhline(float(arbol.corte),color='r')
    if arbol.nombre=="'Eje x'":
        print('entra')
        print('Valor Corte: ',arbol.corte)
        plt.axvline(arbol.corte,color='g')
    if arbol.izq!=None:
        cortes(arbol.izq,0,arbol.corte)
    if arbol.der!=None:
        cortes(arbol.der,arbol.corte,0)

def plotear(archivo,arbol):
    print(archivo)
    puntos(archivo,'yes')
    #puntosno=puntos(archivo,'no')
    #print(puntosyes)
    #plt.scatter(puntosyes[0],puntosyes[1],'*r')
    plt.xlim(-1,3.1)
    plt.ylim(-1,3.1)
    cortes(arbol)
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
