# -*- coding: latin-1 -*-
from Read import read as rd
from Grafica import grafica as gf
from Gain import GAIN as gn
from Arbol import arbol as ab
from Entropy import entropy as en
from copy import deepcopy


def decision_tree(archivo, atributos, arbol=None, nivel=0, ganancia=0):
    """
    la implementaci�n del algoritmo c4.5
    :param archivo: un arreglo con todos los datos
    :param atributos: los nombre de los atributos
    :param arbol: el nodo actual
    :param nivel: la profundidad en el arbol

    :return: un arbol de decisi�n
    """
    entropiac = en.entropiaclase(archivo)  # Calculo la entropia del archivo
    if entropiac == 0:  # Condici�n de parada, el conjunto de datos es puro
        nombre = en.clase(archivo)  # determino la clase del conjunto
        nuevo_nodo = ab.Nodo(nombre=nombre, corte=0, nivel=nivel, soporte=len(archivo), confianza=1,
                             hoja='si')  # Genero el Nodo
        arbol = nuevo_nodo  # Lo asigno al arbol
        return arbol  # Devuelvo el nodo
    else:  # Trato a los datos continuos oomo conjuntos de datos
        nombre_conjunto = ['conjunto 1', 'conjunto 2']  # Defino los 2 conjuntos
        posicion = [0, 0]  # Primer posici�n, que eje, Segunda posicion desplazamiento dentro del conjunto de datos
        ganancia_inf = 0  # Ganancia de Informaci�n
        for i in range(0, 2):
            valor_corte = 0  # Valor de corte es decir el promedio de los 2 puntos
            atributo_pos = i  # la poscici�n del atributo
            archivo = rd.ordenar(archivo, atributo_pos)  # Ordeno el archivo por el atributo
            control = False  # Seteo Variable Corntro
            while not control:
                sub_intervalo = rd.genintervalo(archivo, valor_corte, atributo_pos,
                                                nombre_conjunto)  # Genero el sib intervalo
                ganancia_sub_intervalo = gn.gain(sub_intervalo,
                                                 atributo_pos)  # Generola ganancia del intervalo anterior
                if ganancia_sub_intervalo > ganancia_inf:  # Pregunto si el nuevo corte, mejora la ganancia de informaci�n
                    ganancia_inf = ganancia_sub_intervalo  # Actualizao la ganancia
                    if i == 0:  # Estamos en el primer bucle
                        posicion[1] = valor_corte  # Actualizo la poscion del corte, desplazamientos
                    else:
                        posicion[0] = 1  # Actualizo la poscion del corte, atributo
                        posicion[1] = valor_corte  # Actualizo la posicion del corte, desplazamiento
                valor_corte = rd.genproxcorte(archivo, valor_corte,
                                              atributo_pos)  # Genero la proxima posicion del corte
                if valor_corte == -1:  # Overflow, no hay mas posiciones
                    control = True
        archivo = rd.ordenar(archivo, posicion[
            0])  # ordeno el archivo por el atributo que me genera la mayor ganancia de informcion
        valor_corte = rd.valorcorte(archivo, posicion[1],
                                    posicion[0])  # Obtengo el valor del corte que me genera la mayor ganancia
        subconjunto_izq = deepcopy(
            archivo[0:posicion[1]])  # Genero el primer subconjunto, todo lo que est� a la izquierda
        subconjunto_der = deepcopy(
            archivo[posicion[1]:])  # Genero el segundo subconjunto, todo lo que est� a la izquierda
        nombre = atributos[posicion[0]]  # nombre del eje
        ganancia = ganancia_inf

        if ganancia_inf > 0:
            nod2 = ab.Nodo(nombre, valor_corte, nivel, len(archivo))  # Genero el nodo raiz para esta iteracion
            arbol.genelemento(nod2)  # Lo agrego al arbol
            if subconjunto_izq is not None:  # Pregunto si el subconjunto no est� vacio
                nuevo_nodo_izq = ab.Nodo()  # Creo el nodo
                nuevo_nodo_izq = decision_tree(archivo=subconjunto_izq, atributos=atributos, arbol=nuevo_nodo_izq,
                                               nivel=nivel + 1, ganancia=ganancia)  # llamo a la funcion recursiva
                arbol.agregarizq(nuevo_nodo_izq)  # Lo agrego al arbol
            if subconjunto_der is not None:
                nuevo_nodo_der = ab.Nodo()
                nuevo_nodo_der = decision_tree(archivo=subconjunto_der, atributos=atributos, arbol=nuevo_nodo_der,
                                               nivel=nivel + 1, ganancia=ganancia)
                arbol.agregarder(nuevo_nodo_der)
        else:  # Nodos impuros
            clase1 = en.clase(archivo)  # Busco la clase mas probable
            confianza = float(round(en.confianzaclase(archivo, clase1), 2))  # Calculo su confianza
            nod2 = ab.Nodo(nombre=clase1, corte=0, nivel=nivel, soporte=len(archivo), confianza=confianza,
                           hoja='si')  # Genero el nodo impuro
            arbol = nod2
        return arbol


def principal(archivo, nodo):
    """
    Es la funci�n mas amplia y que engloba el programa
    :param archivo: archivo con el conjunto de entrenamiento y conjunto de prueba
    :return: nada
    """

    nivel = 0  # Genera la profundidad inicial
    nodo = decision_tree(archivo[1], archivo[0], nodo, nivel,0)  # Llama al algoritmo de Decisi�n

    nombre = 'Arbol_Decision.png'
    gf.graficar_arbol(nodo, nombre)  # Plotea otro grafico
    gf.graficar_diagrama_cortes(archivo[2], archivo[1], nodo, 'grafica_desintegracion.png')  # Plotea un grafio
    return nodo


#nodo = ab.Nodo()
#print('Creo Nodo')
#archivo=rd.read_ar('datos2.csv',80)
#principal(archivo, nodo)
#nodo.clasepunto(1, 1.5)
