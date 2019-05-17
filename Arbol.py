#-*- coding: latin-1 -*-
import pygraphviz as pgv
#import networkx as nw

import copy as cp

class Nodo:
    """docstring for Nodo."""
    #Constructor
    def __init__(self,nombre=None,corte=None,nivel=0,soporte=0,confianza=0,hoja=None,izq=None,der=None):
        self.nombre=nombre#nombre del nodo
        self.corte = corte #Valor del corte
        self.nivel = nivel#profundidad dentro del arbol
        self.soporte=soporte #Soport del nodo
        self.confianza=confianza#Confianza del nodo
        self.hoja=hoja#si es hoja o no
        self.izq=izq #Nodo hijo izquierdo todo a la izquierda del corte
        self.der=der#Nodo hijo derecho todo a la derecha del corte

    def __str__(self):
        return"%s %s" %(self.nombre,self.soporte)

    def listar(self):
        if self!=None:
            menor=('< '+str(cp.deepcopy(self.corte)))
            mayor=('> '+str(cp.deepcopy(self.corte)))
            print('lista: ',self.nombre,menor,mayor,self.soporte)
            if self.izq!=None:
                var1=self.izq
                var1.listar()
            if self.der!=None:
                var2=self.der
                var2.listar()

    #Funcion que recibe otro nodo, y sobre escribe los valor del nodo actual
    def genelemento(self,elemento):
        self.nombre=elemento.nombre
        self.nivel=elemento.nivel
        self.soporte=elemento.soporte
        self.corte=elemento.corte

    #agrega un nodo como hijo del lado izquierdo
    def agregarizq(self,elemento):
        self.izq=elemento

    #Agrega un nodo como hijo del lado derecho
    def agregarder(self,elemento):
        self.der=elemento

    #Funcion recursiva que se recibe a si mismo y al grafico
    #genera todos los nodos y los arcos del grafico
    def plot_recusivo(self,arbol):
        #print(self.nombre,self)
        if self!=None and self.izq!=None:#Pregunto  si es el nodo existe y si tiene hijo
            var1=self.izq
            menor=('< '+str(self.corte))#Genero las etiquetas de los arcos
            mayor=('> '+str(self.corte))
            if var1.hoja=='si': #Genero los 2 nodos origen destino, teniendo al nodo destino como hoja
                arbol.add_edge((self.nombre,self.nivel,self.soporte),(var1.nombre,var1.nivel,var1.soporte,var1.confianza),label=menor,color='red')
            else:#Genero los 2 nodos origen destino, teniendo al nodo destino como nodo de decisi�n
                arbol.add_edge((self.nombre,self.nivel,self.soporte,),(var1.nombre,var1.nivel,var1.soporte),label=menor,)
            var1.plot_recusivo(arbol)
        #Lo mismo que el anterior
        if self!=None and self.der!=None:
            var2=self.der
            if var2.hoja=='si':
                arbol.add_edge((self.nombre,self.nivel,self.soporte),(var2.nombre,var2.nivel,var2.soporte,var2.confianza),label=mayor)
            else:
                arbol.add_edge((self.nombre,self.nivel,self.soporte),(var2.nombre,var2.nivel,var2.soporte),label=mayor)
            var2.plot_recusivo(arbol)
        return(arbol)

#recibe el nodo raiz y un nombre
#Genera el arbol de Desici�n
def plot(nodo,nombre):
    arbol = pgv.AGraph(directed=True,label='Arbol Desicion')
    nodo.plot_recusivo(arbol)
    arbol.layout(prog='dot')
    arbol.draw(nombre)
    #arbol.plot()


    #plt.show()


"""PRUEBA """
#nodo=Nodo()
#nodo=prueba(9,nodo)
#Prueba2=aBinarios()
#Prueba2.agregar(nodo)
#plot(Prueba2,'opcionrecursiva.png')
