 #-*- coding: latin-1 -*-
import matplotlib.pyplot as plt
from Read import read as rd


 #recibe un conjunto de datos y el valor de una clase
#a todos los regitros cuya clase coincida con la clase ingresada van a tener un tipo de representaci�n en el grafico
#al resto de registros van a tener otra representaci�n
def puntos(entrada,clase):
    ejex=[]
    ejey=[]
    for registro in entrada:
        if registro[len(registro)-1]==clase:
            plt.scatter(float(registro[0]),float(registro[1]),c='red',marker="^")
        else:
            plt.scatter(float(registro[0]),float(registro[1]),c='blue')
#Funcion recursiva que recibe un nodo, los limtes del grafico tanto en x como en y, y las restricciones tanto en x como en y
#y genera las lineas de cortes
def cortes(arbol,limitex,limitey,restrix=[0,0],restriy=[0,0]):
    ancho=float(limitex[1])-float(limitex[0]) #Establece el ancho de la grafica
    alto=float(limitey[1])-float(limitey[0])#Establece el alto de la grafica
    if arbol.nombre=="'Eje y'":#Pregunta si el corte es sobre el eje Y
        limi=0#establece el limite inferior en 0
        lims=1#establece el limite superior en 1
        #Si tiene alguna restricci�n distinta de 0 hay que actualizar los limites
        if restrix[0]!=0 :#
            limi=(float(restrix[0])-float(limitex[0]))/ancho
        if restrix[1]!=0:
            lims = (float(restrix[1]) - float(limitex[0])) / ancho

        plt.axhline(float(arbol.corte),limi,lims,color='r')#Funcion que plotea, recibe el valor del eje y en terminos relativos, donde comienza
        #y donde termina la linea, los valores van de 0 a 1
        #Actualiza los valores y se llama recursivamente
        if arbol.izq!=None:
            restriyn=[restriy[0],arbol.corte]
            cortes(arbol.izq,limitex,limitey,restrix,restriyn)
        if arbol.der!=None:
            restriyn=[arbol.corte,limitey[1]]
            cortes(arbol.der,limitex,limitey,restrix,restriyn)
    #Lo mismo para el eje X
    if arbol.nombre=="'Eje x'":
        limi=0
        lims=1
        if restriy[0]!=0:
            limi=(float(restriy[0])-float(limitey[0]))/alto
        if restriy[1]!=0:
            lims=(float(restriy[1])-float(limitey[0]))/alto
        plt.axvline(float(arbol.corte),limi,lims,color='g')
        if arbol.izq!=None:
            restrixn=[restrix[0],arbol.corte]
            cortes(arbol.izq,limitex,limitey,restrixn,restriy)
        if arbol.der!=None:
            restrixn=[arbol.corte,limitex[1]]
            cortes(arbol.der,limitex,limitey,restrixn,restriy)

#Funci�n que recibe los valores de las clases, el conjunto de datos del archivo, el nodo raiz y el nombre del archivo
#Genera el grafico de 2D con los cortes
def plotear(clase,archivo,arbol,nombre):
    puntos(archivo,clase[0])#plotea los puntos
    limitex= rd.extremos(archivo,0)#Establece los limites del grafico
    limitey=rd.extremos(archivo,1)
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
    cortes(arbol,limitex,limitey,restrix,restriy) #Llama a la funcion Cortes
    plt.savefig(nombre)#Guada el archivo
    #plt.savefig("grafica_desintegracion.png")
    #plt.show()#Lo muestra

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
