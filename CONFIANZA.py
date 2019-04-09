#-*- coding: latin-1 -*-
 #!/usr/bin/python
import decimal
from decimal import Decimal

def confidence(vector1,vector2,archivo):
    n=0
    count1=0
    count2=0
    for reg in archivo:
        bandera1=0
        bandera2=0
        for reg1 in vector1:
            if (reg1 in reg)!=True:
                bandera1=1
            if bandera1==0:
                count1=count1+1
        for reg2 in vector2:
            if (reg2 in reg)!=True:
                bandera2=1
            if bandera2==0:
                count2=count2+1
    total=Decimal(count1)/Decimal(count2)
    return total
