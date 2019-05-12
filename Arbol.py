#-*- coding: latin-1 -*-
import pygraphviz as pgv
import copy as cp

class Nodo:
    """docstring for Nodo."""

    def __init__(self,nombre=None,corte=None,nivel=0,soporte=0,confianza=0,hoja=None,izq=None,der=None):
        self.nombre=nombre
        self.soporte=soporte
        self.nivel=nivel
        self.corte=corte
        self.confianza=confianza
        self.hoja=hoja
        self.izq=izq
        self.der=der
        #self.menor=menor
        #self.mayor=mayor

    def __str__(self):
        return"%s %s" %(self.nombre,self.soporte)

    def listar(self):
        if self!=None:
            menor=('< '+str(cp.deepcopy(self.corte)))
            mayor=('> '+str(cp.deepcopy(self.corte)))
            print('lista: ',self.nombre,menor,mayor,self.soporte)
            if self.izq!=None:
                #print(self.nombre,self.hoja,self.izq)
                var1=self.izq
                var1.listar()
            if self.der!=None:
                #print(self.izq)
                var2=self.der
                var2.listar()


    def genelemento(self,elemento):
        self.nombre=elemento.nombre
        self.nivel=elemento.nivel
        self.soporte=elemento.soporte
        self.corte=elemento.corte
    def agregarizq(self,elemento):
        if self.nombre==None:
            self.nombre=elemento.nombre
            self.nivel=elemento.nivel
            self.soporte=elemento.soporte
            if elemento.izq!=None:
                self.izq=elemento.izq
            if elemento.der!=None:
                self.der=elemento.der
        else:
            self.izq=elemento

    def agregarder(self,elemento):
        if self.nombre==None:
            self.nombre=elemento.nombre
            self.nivel=elemento.nivel
            self.soporte=elemento.soporte
            if elemento.izq!=None:
                self.izq=elemento.izq
            if elemento.der!=None:
                self.der=elemento.der
        else:
            self.der=elemento

    def plot_recusivo(self,arbol):
        #print(self.nombre,self)
        if self!=None and self.izq!=None:
            var1=self.izq
            menor=('< '+str(self.corte))
            mayor=('> '+str(self.corte))
            if var1.hoja=='si':
                arbol.add_edge((self.nombre,self.nivel,self.soporte),(var1.nombre,var1.nivel,var1.soporte,var1.confianza),label=menor,color='red')
                #print(self.nombre,var1.nombre,'entra condicion izq')
            else:
                arbol.add_edge((self.nombre,self.nivel,self.soporte,),(var1.nombre,var1.nivel,var1.soporte),label=menor,)
                #print(self.nombre,var1.nombre,'no entra condicion izq')
            var1.plot_recusivo(arbol)

        if self!=None and self.der!=None:
            var2=self.der
            if var2.hoja=='si':
                arbol.add_edge((self.nombre,self.nivel,self.soporte),(var2.nombre,var2.nivel,var2.soporte,var2.confianza),label=mayor)
                #print(self.nombre,var2.nombre,'entra condicion')
            else:
                arbol.add_edge((self.nombre,self.nivel,self.soporte),(var2.nombre,var2.nivel,var2.soporte),label=mayor)
                #print(self.nombre,var2.nombre,'no entra condicion')
            var2.plot_recusivo(arbol)
        return(arbol)

    def plot(self,nombre):
        arbol = pgv.AGraph(directed=True,label='Arbol Desicion, RESOLVER CON PROFUNDIDAD')
        self.plot_recusivo(arbol)
        arbol.layout(prog='dot')
        arbol.draw(nombre)
        return arbol


"""PRUEBA """
#nodo=Nodo()
#nodo=prueba(9,nodo)
#Prueba2=aBinarios()
#Prueba2.agregar(nodo)
#plot(Prueba2,'opcionrecursiva.png')
