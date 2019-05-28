from Desicion import desicion as Ds
from Arbol import arbol as Ab
from Read import read as Rd
from Write import write as Wr
salida=[['intento','longitud','aciertos','fallos']]
resultado=[0,0,0,[],[]]
for i in range(1,101):
    salida+=[[[],[],[],[],[]]]
    nodo = Ab.Nodo()
    archivo= Rd.read_ar('Pruebacsv.csv',80)
    #print(archivo[1])
    #print(archivo[3])
    #print(salida)
    salida[i][0]=len(archivo[3])
    nivel = 0
    nodo = Ds.decision_tree(archivo[1], archivo[0], nodo, nivel,0)
    #Ds.principal(''datos_continuo.csv'',nodo)
    cont_true=0
    cont_false=0
    for reg in archivo[3]:
        if reg[2]== nodo.clasepunto(reg[0],reg[1]):
            cont_true+=1
        else:
            cont_false+=1
    salida[i][1]=cont_true
    salida[i][3]=round((cont_true/len(archivo[3]))*100,2)
    resultado[0]=i
    resultado[1]+=salida[i][3]
    salida[i][2]=cont_false
    salida[i][4] = round((cont_false / len(archivo[3]))*100,2)
    resultado[2]+=salida[i][4]
Wr.write_ar(salida,'resultados_prueba.csv')
resultado[3]=resultado[1]/resultado[0]
resultado[4]=resultado[2]/resultado[0]
print(resultado)