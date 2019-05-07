from copy import deepcopy
class Nodo:
    """docstring for Nodo."""

    def __init__(self,nombre=None,corte=None,cedula=0,confianza=0,hoja=None,izq=None,der=None):
        self.nombre=nombre
        self.cedula=cedula
        self.confianza=confianza
        self.corte=corte
        self.hoja=hoja
        self.izq=izq
        self.der=der
        #self.menor=menor
        #self.mayor=mayor

    def __str__(self):
        return"%s %s" %(self.nombre,self.cedula)

    def listar(self):
        if self!=None:
            menor=('< '+str(deepcopy(self.corte)))
            mayor=('> '+str(deepcopy(self.corte)))
            print('lista: ',self.nombre,menor,mayor,self.cedula)
            if self.izq!=None:
                print(self.nombre,self.hoja,self.izq)
                var1=self.izq
                var1.listar()
            if self.der!=None:
                print(self.izq)
                var2=self.der
                var2.listar()


    def genelemento(self,elemento):
        self.nombre=elemento.nombre
        self.cedula=elemento.cedula
        self.corte=elemento.corte
    def agregarizq(self,elemento):
        if self.nombre==None:
            self.nombre=elemento.nombre
            self.cedula=elemento.cedula
            if elemento.izq!=None:
                self.izq=elemento.izq
            if elemento.der!=None:
                self.der=elemento.der
        else:
            self.izq=elemento

    def agregarder(self,elemento):
        if self.nombre==None:
            self.nombre=elemento.nombre
            self.cedula=elemento.cedula
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
                arbol.add_edge((self.nombre,self.cedula),(var1.nombre,var1.cedula,var1.confianza),label=menor)
                print(self.nombre,var1.nombre,'entra condicion izq')
            else:
                arbol.add_edge((self.nombre,self.cedula),(var1.nombre,var1.cedula),label=menor)
                print(self.nombre,var1.nombre,'no entra condicion izq')
            var1.plot_recusivo(arbol)

        if self!=None and self.der!=None:
            var2=self.der
            if var2.hoja=='si':
                arbol.add_edge((self.nombre,self.cedula),(var2.nombre,var2.cedula,var2.confianza),label=mayor)
                print(self.nombre,var2.nombre,'entra condicion')
            else:
                arbol.add_edge((self.nombre,self.cedula),(var2.nombre,var2.cedula),label=mayor)
                print(self.nombre,var2.nombre,'no entra condicion')
            var2.plot_recusivo(arbol)
        return(arbol)

    def plot(self,nombre):
        import pygraphviz as pgv
        arbol = pgv.AGraph(directed=True,center=True,ordering="in")
        self.plot_recusivo(arbol)
        arbol.layout()
        arbol.draw(nombre)
        return arbol


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

            arreglo[0]=[i,elemento.nombre,elemento.cedula]
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
        cedula=numero
        nod=Nodo(nombre,cedula)
        arbol.agregarder(nod)
        return(arbol)
    else:
        var1=numero-1
        nombre=i
        cedula=numero
        nod1=Nodo(nombre,cedula)
        prueba(var1,nod1,i+1)
        arbol.agregarder(nod1)
        return(arbol)


def plot(Prueba2,nombre):

    arreglo=Prueba2.preorder(Prueba2.getRaiz())
    arreglo=limpiar(arreglo)
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
"""PRUEBA """
#nodo=Nodo()
#nodo=prueba(9,nodo)
#Prueba2=aBinarios()
#Prueba2.agregar(nodo)
#plot(Prueba2,'opcionrecursiva.png')
