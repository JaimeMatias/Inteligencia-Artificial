from Desicion import desicion as Ds
from Arbol import arbol as Ab
from Read import read as Rd
from Write import write as Wr
import matplotlib.pyplot as plt  # importando matplotlib

Analisis = [['intento','probabilidad','media', 'min', 'max', 'Varianza', 'Desvio Estandar']]
resultado = [0, 0, 0, [], []]
prueb=1
for prob in range(60,90):
    salida = [['intento', 'longitud', 'aciertos', 'fallos']]

    for i in range(1, 40):
        salida += [[[], [], [], [], []]]
        nodo = Ab.Nodo()
        archivo = Rd.read_ar('Pruebacsv.csv', prob)
        salida[i][0] = len(archivo[3])
        nivel = 0
        nodo = Ds.decision_tree(archivo[1], archivo[0], nodo, nivel, 0)
        cont_true = 0
        cont_false = 0
        for reg in archivo[3]:
            if reg[2] == nodo.clasepunto(reg[0], reg[1]):
                cont_true += 1
            else:
                cont_false += 1
        salida[i][1] = cont_true
        salida[i][2] = cont_false
        if len(archivo[3])!=0:
            salida[i][3] = round((cont_true / len(archivo[3])) * 100, 2)
            salida[i][4] = round((cont_false / len(archivo[3])) * 100, 2)
        else:
            salida[i][3]=0
            salida[i][4] = 0

    Wr.write_ar(salida, 'resultados_prueba.csv')
    import pandas as pd

    df = pd.read_csv('resultados_prueba.csv', index_col=0)
    # df.mean()

    media = round(df[['aciertos']].get_values().mean(), 2)
    mini = round(df[['aciertos']].get_values().min(), 2)
    maxi = round(df[['aciertos']].get_values().max(), 2)
    var = round(df[['aciertos']].get_values().var(), 2)
    desvi = round(df[['aciertos']].get_values().std(), 2)
    Analisis += [[prueb,prob,
        media, mini,
        maxi, var, desvi]]
    prueb+=1
Wr.write_ar(Analisis, 'Analisi_resultados_prueba.csv')
df=pd.read_csv('Analisi_resultados_prueba.csv',index_col=0)
print(df)
df.get
prob=df[['probabilidad']].get_values()
desvi = df[['Desvio Estandar']].get_values()
plt.scatter(prob,desvi)
plt.savefig('Disperción.png')
plt.xlabel('Porcentaje de Datos Entrenamiento')
plt.ylabel('Desvio EStandar')
plt.show()
