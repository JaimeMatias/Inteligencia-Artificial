# -*- coding: latin-1 -*-
import pygraphviz as pgv

import copy as cp


class Nodo:
    """docstring for Nodo."""

    def __init__(self, nombre=None, corte=None, nivel=0, soporte=0, confianza=0, hoja=None, izq=None, der=None):
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
        self.izq = izq  # Nodo hijo izquierdo todo a la izquierda del corte
        self.der = der  # Nodo hijo derecho todo a la derecha del corte

    # Funcion que recibe otro nodo, y sobre escribe los valor del nodo actual
    def genelemento(self, elemento):
        """
        actualiza la información del nodo
        :param elemento: nodo con la información
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
        if self is not None and self.izq is not None:  # Pregunto  si es el nodo existe y si tiene hijo
            var1 = self.izq
            menor = ('< ' + str(self.corte))  # Genero las etiquetas de los arcos
            if var1.hoja == 'si':  # Genero los 2 nodos origen destino, teniendo al nodo destino como hoja
                arbol.add_edge((self.nombre, self.nivel, self.soporte),
                               (var1.nombre, 'IZQ', var1.nivel, var1.soporte, var1.confianza), label=menor,
                               color='blue')
            else:  # Genero los 2 nodos origen destino, teniendo al nodo destino como nodo de decisiï¿½n
                arbol.add_edge((self.nombre, self.nivel, self.soporte,), (var1.nombre, var1.nivel, var1.soporte),
                               label=menor, )
            var1.plot_recusivo(arbol)
        # Lo mismo que el anterior
        if self is not None and self.der is not None:
            var2 = self.der
            mayor = ('> ' + str(self.corte))
            if var2.hoja == 'si':
                arbol.add_edge((self.nombre, self.nivel, self.soporte),
                               (var2.nombre, 'DER', var2.nivel, var2.soporte, var2.confianza), label=mayor)
            else:
                arbol.add_edge((self.nombre, self.nivel, self.soporte), (var2.nombre, var2.nivel, var2.soporte),
                               label=mayor)
            var2.plot_recusivo(arbol)
        return arbol


# recibe el nodo raiz y un nombre
# Genera el arbol de Desiciï¿½n
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
