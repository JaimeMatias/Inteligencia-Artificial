#-*- coding: latin-1 -*-
 #!/usr/bin/python
import decimal
from decimal import Decimal


def support(vector,archivo):
    n=0
    count=0
    if type(vector)==str:
        for reg in archivo:
            n=n+1
            bandera=0
            if (vector in reg)!=True:
                bandera=1
            if bandera==0:
                count=count+1
        total=Decimal(count)/Decimal(n)
        return total
    else:
        for reg2 in archivo:
            n=n+1
            bandera=0
            for reg3  in vector:
                if (reg3 in reg2)!=True:
                    bandera=1
            if bandera==0:
                count=count+1
        total=Decimal(count)/Decimal(n)
        return total
