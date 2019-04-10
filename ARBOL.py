#!/usr/bin/python3.6
class Nodo:
    """docstring for Nodo."""

    def __init__(self,nombre=None,cedula=0,izq=None,der=None):
        self.nombre=nombre
        self.cedula=cedula
        self.izq=izq
        self.der=der

    def __str__(self):
        return"%s %s" %(self.nombre,self.cedula)

class aBinarios: #Al ser un arbol, conoce todas sus hojas
    """docstring for aBinarios."""

    def __init__(self):
        self.raiz = None

    def agregar(self, elemento):
        if self.raiz==None:
            self.raiz=elemento
        else:
            aux=self.raiz
            padre=None

            while aux!=None:
                padre=aux
                if int(elemento.cedula) >= int(aux.cedula):
                    aux=aux.der
                else:
                    aux=aux.izq
            if int(elemento.cedula) >= int(padre.cedula):
                padre.der=elemento
            else:
                padre.izq=elemento


    def preorder(self,elemento,i=0):
        arreglo=[[]]
        if elemento!=None:
            des="L"
            desplazamiento=""
            for j in range(0,i):
                if j==(i-1):
                    desplazamiento+=des
                desplazamiento+=" "
            desplazamiento+="_"
            arreglo[0]=[i,elemento.cedula]
            arreglo+=self.preorder(elemento.izq,i+1)
            arreglo+=self.preorder(elemento.der,i+1)
        return(arreglo)



    def getRaiz(self):
        return self.raiz

from random import randrange

def limpiar(arreglo):
    arr=[]
    for reg in arreglo:
        if not reg:
            pass
        else:
            arr+=[reg]
    return arr

def plot(arreglo,nombre):
    import pygraphviz as pgv
    arbol = pgv.AGraph(directed=True,center=True,ordering="in")

    for i in range(0,len(arreglo)):
        cont=2
        for j in range(i+1,len(arreglo)):
            if cont!=0:
                if arreglo[i][0]==arreglo[j][0]:
                    cont=0
                if (arreglo[i][0]+1)==arreglo[j][0]:
                    arbol.add_edge((arreglo[i][0],arreglo[i][1]),(arreglo[j][0],arreglo[j][1]),label=arreglo[j][0])
    arbol.layout()
    arbol.draw(nombre)
    return arbol
