
import READ
from READ import read_ar
from A_priori import A_priori
from decimal import Decimal

def convertir(numero):
    numero=Decimal(numero*0.01)
    numero=round(numero,2)
    return numero

support=int(raw_input("ingrese el soporte(0 a 100): "))
support=convertir(support)
Data=read_ar('compra.csv')
A_priori(Data,support)
confidence=int(raw_input("ingrese la confinaza(0 a 100): "))
confidence=convertir(confidence)
