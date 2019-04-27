from copy import deepcopy
class Nodo:
    """docstring for Nodo."""

    def __init__(self,nombre=None,cedula=0,izq=None,der=None):
        self.nombre=nombre
        self.cedula=cedula
        self.izq=izq
        self.der=der

    def __str__(self):
        return"%s %s" %(self.nombre,self.cedula)

    def listar(self):
        if self!=None:

            print('lista: ',self.nombre,self.cedula)
            if self.izq!=None:
                var1=self.izq
                var1.listar()
            if self.der!=None:
                var2=self.der
                var2.listar()


    def agregar2(self,elemento):
        #print('en agregar 2 el tipo es :',type(elemento))

        if self.cedula==0:
            #print('Condicion: ',self.cedula==0)
            self.nombre=elemento.nombre
            self.cedula=elemento.cedula
            if elemento.izq!=None:
                self.izq=elemento.izq

            if elemento.der!=None:
                self.der=elemento.der        

        else:
        #print(int(self.cedula))
            if int(elemento.cedula) >= int(self.cedula):
                self.der=elemento
            else:
                self.izq= elemento


class aBinarios: #Al ser un arbol, conoce todas sus hojas
    """docstring for aBinarios."""

    def __init__(self):
        self.raiz = None

    def agregar(self, elemento):
        if self.raiz==None:
            self.raiz=elemento
            #print('Prueba ',elemento)
            #print('prueba: ',elemento.izq)
        else:
            aux=self.raiz
            padre=None


            #if int(elemento.cedula) >= int(aux.cedula):
            #    aux.der=elemento
            #else:
            #    aux.izq= elemento
            while (aux.der!=None) and (aux.izq!=None):
                padre=aux
                if int(elemento.cedula) > int(aux.cedula):
                    aux=aux.der
                else:
                    aux=aux.izq
            if int(elemento.cedula) >= int(aux.cedula):
                aux.der=elemento
            else:
                aux.izq=elemento


    def preorder(self,elemento,num=0,i=0):
        arreglo=[[]]
        #print(elemento)
        if elemento!=None:
            des="L"
            desplazamiento=""
            for j in range(0,i):
                if j==(i-1):
                    desplazamiento+=des
                desplazamiento+=" "
            desplazamiento+="_"
            if num==0:
                print(i,'izquierda',desplazamiento,elemento.cedula)
            else:
                print(i,'derecha',desplazamiento,elemento.cedula)

            arreglo[0]=[i,elemento.cedula]
            arreglo+=self.preorder(elemento.izq,0,i+1)
            arreglo+=self.preorder(elemento.der,1,i+1)
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

def prueba(numero,arbol,i=0):
    if numero==0:
        nombre=i
        print('nodo: ',i)
        cedula=numero
        nod=Nodo(nombre,cedula)
        nod.listar()
        #print("Es 0:",nod.nombre,nod.cedula,i)
        #print(type(nod))
        #print('prueba')
        arbol.agregar2(nod)
        return(arbol)
    else:
        var1=numero-1
        nombre=i
        cedula=numero
        nod1=Nodo(nombre,cedula)
        print('nodo pre prueba: ',i)
        nod1.listar()
        print('numero prueba: ',i+1)
        prueba(var1,nod1,i+1)
        print('nodo post prueba: ',i+1)
        nod1.listar()
        print('valor nodo: ',nod1.nombre,nod1.cedula)
        print('valor arbol: ',arbol.nombre, arbol.cedula)
        arbol.agregar2(nod1)
        print('hola')
        arbol.listar()

        print('arbol: ',i)
        #arbol.agregar2(nod1)
        #arbol.listar()        #prin('nodo:')

        #print('primero recursividad: ',nombre,cedula)
        #print(type(prueba(var1,nodo,i+1)))
        return(arbol)


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

Prueba=aBinarios()
print('FUnciona')
from random import randrange
nod2=Nodo(1,40)
print(nod2)
nod3=Nodo(2,35)
#nod3.agregar2(Nodo(4,45))
#nod3.agregar2(Nodo(4,25))

nod4=Nodo(3,60)
nod2.agregar2(nod3)
nod3.agregar2(nod4)
nod2.listar()
#nod2.agregar2(Nodo(3,35))
#print('nodo: ',nod2)
#nod3=Nodo(2,30)
#print('nombre: ',nod2.derecha.nombre)
Prueba.agregar(nod2)
#Prueba.agregar(nod3)
#Prueba.agregar(nod4)
"""for i in range(0,10):
    print(i)
    val=randrange(2,100)

    nod=Nodo(i,val)
    Prueba.agregar(nod)"""
nodo=Nodo()
nodo=prueba(9,nodo)
print('prueba')
#varx.listar()
print('ho')
nodo.listar()
#nodo.agregar2(var3[0])
#nodo.agregar2(prueba(4,nodo))
#print(type(nodo))
#print(nodo.izq !=None)
#print('valor: ',nodo.nombre,nodo.cedula)
#print('valor: ',nodo.izq.nombre,nodo.izq.cedula)
#print('valor: ',nodo.der.nombre,nodo.der.cedula)
#print('valor: ',nodo.der.der.nombre,nodo.der.der.cedula)

#print('nodo Recursivo: ',nodo)
Prueba2=aBinarios()
Prueba2.agregar(nodo)

#print('raiz: ',Prueba2.getRaiz())
#Prueba2.preorder(Prueba2.getRaiz())
#print(type(Prueba))
#Prueba.preorder(Prueba.getRaiz())
#print(Prueba.getRaiz().derecha)
arreglo=Prueba.preorder(Prueba.getRaiz())
arreglo=limpiar(arreglo)
#print(arreglo)
plot(arreglo,'opcion.png')
arreglo=Prueba2.preorder(Prueba2.getRaiz())
arreglo=limpiar(arreglo)
#print(arreglo)
plot(arreglo,'opcionrecursiva.png')
