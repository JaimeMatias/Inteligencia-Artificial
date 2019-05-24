# -*- coding: latin-1 -*-
import pygraphviz as pgv

import copy as cp


class Nodo:
    """docstring for Nodo."""

    def __init__(self, nombre=None, corte=None, nivel=0, soporte=0, confianza=0, hoja=None, tipo=None, izq=None,
                 der=None):
        """
        Constructor
        :param nombre: nombre del nodo
        :param corte: valor del corte
        :param nivel: profundidad dentro del arbol
        :param soporte: soporte del nodo
        :param confianza: confianza del nodo
        :param hoja: si es hoja o no
        :param izq: nodo hijo izquiero
        :param der: nodo hijo derecho
        """
        self.nombre = nombre
        self.corte = corte
        self.nivel = nivel
        self.soporte = soporte
        self.confianza = confianza
        self.hoja = hoja
        self.tipo = tipo
        self.izq = izq  # Nodo hijo izquierdo todo a la izquierda del corte
        self.der = der  # Nodo hijo derecho todo a la derecha del corte

    # Funcion que recibe otro nodo, y sobre escribe los valor del nodo actual
    def genelemento(self, elemento):
        """
        actualiza la informaci�n del nodo
        :param elemento: nodo con la informaci�n
        :return:
        """
        self.nombre = elemento.nombre
        self.nivel = elemento.nivel
        self.soporte = elemento.soporte
        self.corte = elemento.corte

    def agregarizq(self, elemento):
        """
        genera un hijo del lado izquierdo
        :param elemento: nodo
        :return:
        """
        self.izq = elemento

    def agregarder(self, elemento):
        """
         genera un hijo del lado derecho
        :param elemento: nodo
        :return:
        """
        self.der = elemento

    # Funcion recursiva que se recibe a si mismo y al grafico
    # genera todos los nodos y los arcos del grafico
    def plot_recusivo(self, arbol):
        # print(self.nombre,self)
        id = (str(self.nombre) + str(self.corte) + str(self.nivel))
        if self is not None and self.izq is not None:  # Pregunto  si es el nodo existe y si tiene hijo
            var1 = self.izq
            menor = ('< ' + str(self.corte))  # Genero las etiquetas de los arcos
            id_local = (str(var1.nombre) + str(var1.corte) + str(var1.nivel))
            if var1.hoja == 'si':  # Genero los 2 nodos origen destino, teniendo al nodo destino como hoja
                id_local = (str(var1.nombre) + str(self.corte) + str(var1.nivel))
                arbol.add_edge((id, self.soporte),
                               (id_local, var1.soporte, var1.confianza), label=menor)
            else:  # Genero los 2 nodos origen destino, teniendo al nodo destino como nodo de decisi�n
                arbol.add_edge((id, self.soporte,), (id_local, var1.soporte),
                               label=menor, )
            var1.plot_recusivo(arbol)
        # Lo mismo que el anterior
        if self is not None and self.der is not None:
            var2 = self.der
            mayor = ('> ' + str(self.corte))
            id_local = (str(var2.nombre) + str(var2.corte) + str(var2.nivel))
            if var2.hoja == 'si':
                id_local = (str(var2.nombre) + str(self.corte) + str(var2.nivel))
                arbol.add_edge((id, self.soporte),
                               (id_local, var2.soporte, var2.confianza), label=mayor)
            else:
                arbol.add_edge((id, self.soporte), (id_local, var2.soporte),
                               label=mayor)
            var2.plot_recusivo(arbol)
        return arbol

    def clasepunto(self, valorx=float, valory=float):
        var = self
        while var is not None:
            if var.hoja == "si":
                return print('Es de la clase: ', var.nombre)
            if var.nombre == "Eje y":
                if valory < var.corte:
                    var = var.izq
                else:
                    var = var.der
            if var.nombre == "Eje x":
                if valorx < var.corte:
                    var = var.izq
                else:
                    var = var.der


# recibe el nodo raiz y un nombre
# Genera el arbol de Desici�n
def plot(nodo, nombre):
    arbol = pgv.AGraph(directed=True, label='Arbol Desicion')
    nodo.plot_recusivo(arbol)
    arbol.layout(prog='dot')
    arbol.draw(nombre)
    # arbol.plot()

    # plt.show()


"""PRUEBA """
# nodo=Nodo()
# nodo=prueba(9,nodo)
# Prueba2=aBinarios()
# Prueba2.agregar(nodo)
# plot(Prueba2,'opcionrecursiva.png')
