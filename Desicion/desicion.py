# -*- coding: latin-1 -*-
from Read import read as rd
from Grafica import grafica as gf
from Gain import GAIN as gn
from Arbol import arbol as ab
from Entropy import ENTROPY as en
from copy import deepcopy


def decision_tree(archivo, atributos, arbol=None, nivel=0,ganancia=0):
    """
    la implementaci�n del algoritmo c4.5
    :param archivo: un arreglo con todos los datos
    :param atributos: los nombre de los atributos
    :param arbol: el nodo actual
    :param nivel: la profundidad en el arbol

    :return: un arbol de decisi�n
    """
    entropiac = en.entropiaclase(archivo)
    if entropiac == 0:
        nombre = en.clase(archivo)  # funcion de ENTROPY
        nod1 = ab.Nodo(nombre, 0, nivel, len(archivo), 1, 'si')
        arbol = nod1
        return arbol
    else:
        var4 = ['conjunto 1', 'conjunto 2']
        posicion = [0, 0, 0]
        valor = 0
        for i in range(0, 2):
            corte = 0
            atributo = i
            control = False
            archivo = rd.ordenar(archivo, atributo)

            while not control:
                var1 = rd.genintervalo(archivo, corte, atributo, var4)
                var2 = gn.gain(var1, atributo)
                if var2 > valor:
                    valor = var2
                    if i == 0:
                        posicion[1] = corte
                    else:
                        posicion[0] = 1
                        posicion[1] = corte
                corte = rd.genproxcorte(archivo, corte, atributo)
                if corte == -1:
                    control = True
        archivo = rd.ordenar(archivo, posicion[0])
        #print('archivo ordenado:',archivo)
        posicion[2] = rd.valorcorte(archivo, posicion[1], posicion[0])

        conjunto1 = deepcopy(archivo[0:posicion[1]])
        conjunto2 = deepcopy(archivo[posicion[1]:])
        #print(conjunto1)
        #print(conjunto2)
        nombre = atributos[posicion[0]]
        corte = posicion[2]
        diferencia=valor-ganancia

        ganancia=valor
        if valor >0:
            nod2 = ab.Nodo(nombre, corte, nivel, len(archivo))
            arbol.genelemento(nod2)
            if conjunto1 is not None:
                #print(len(conjunto1),conjunto1)
                #print()
                nod1 = ab.Nodo(nombre, None, None)
                nod1 = decision_tree(conjunto1, atributos, nod1, nivel + 1,ganancia)
                arbol.agregarizq(nod1)
            if conjunto2 is not None:
                #print(len(conjunto2),conjunto2)
                #print()
                nod1 = ab.Nodo(nombre, None, None)
                nod1 = decision_tree(conjunto2, atributos, nod1, nivel + 1,ganancia)

                arbol.agregarder(nod1)
        else:
            clase1 = en.clase(archivo)
            #print('nodo hoja: ', clase1)
            confianza = float(round(en.confianzaclase(archivo, clase1), 2))
            nod2 = ab.Nodo(clase1, 0, nivel, len(archivo), confianza, 'si')
            arbol = nod2
        return arbol


def principal(archivo,nodo):
    """
    Es la funci�n mas amplia y que engloba el programa
    :param archivo: la direccion del archivo
    :return: nada
    """

    archivo = rd.read_ar(archivo) # Transforma el archivo csv a una estructura en memoria
    nivel = 0  # Genera la profundidad inicial
    nodo = decision_tree(archivo[1], archivo[0], nodo, nivel)  # Llama al algoritmo de Decisi�n

    nombre = 'Arbol_Decision.png'
    ab.plot(nodo, nombre) # Plotea otro grafico
    gf.plotear(archivo[2], archivo[1], nodo, 'grafica_desintegracion.png') #Plotea un grafio
    return nodo
#nodo=ab.Nodo()
#print('Creo Nodo')
#principal('datos3.csv',nodo)
#nodo.clasepunto(1,1.5)