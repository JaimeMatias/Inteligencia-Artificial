# -*- coding: latin-1 -*-

import copy as cp


class Nodo:
    """docstring for Nodo."""

    def __init__(self, nombre=None, corte=None, nivel=0, soporte=0, confianza=0, hoja=None,izq=None,
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


    def clasepunto(self, valorx=float, valory=float):
        var = self
        while var is not None:
            if var.hoja == "si":
                return var.nombre
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

    # arbol.plot()

    # plt.show()


"""PRUEBA """
# nodo=Nodo()
# nodo=prueba(9,nodo)
# Prueba2=aBinarios()
# Prueba2.agregar(nodo)
# plot(Prueba2,'opcionrecursiva.png')
