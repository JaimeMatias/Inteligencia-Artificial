from Desicion import desicion as Ds
from Arbol import arbol as Ab
from Read import read as Rd
from Write import write as Wr
import matplotlib.pyplot as plt  # importando matplotlib

analisis_Positivo_desvio = [['intento', 'probabilidad', 'media', 'min', 'max', 'Varianza', 'Desvio Estandar']]
analisis_Positivo_media = [['intento', 'probabilidad', 'media', 'min', 'max', 'Varianza', 'Desvio Estandar']]
analisis_Negativo = [['intento', 'probabilidad', 'media', 'min', 'max', 'Varianza', 'Desvio Estandar']]
resultado = [0, 0, 0, [], []]
prueb=1
for prob in range(30,101):
    salida = [['longitud','Cantidad Acierto', 'Cantidad Fallo', 'Porcentja aciertos', 'Porcentaje fallos']]
    subindicie=1
    control=0
    print('la prob es: ',prob)
    for i in range(1, 50):

        nodo = Ab.Nodo()
        archivo = Rd.read_ar('datos3.csv', prob)


        nivel = 0
        nodo = Ds.decision_tree(archivo[1], archivo[0], nodo, nivel, 0)
        cont_true = 0
        cont_false = 0
        for reg in archivo[3]:
            if reg[2] == nodo.clasepunto(reg[0], reg[1]):
                cont_true += 1
            else:
                cont_false += 1

        #print(len(archivo[3])!=0)
        if len(archivo[3])!=0:
            salida += [[[], [], [], [], []]]
            salida[subindicie][0] = len(archivo[3])
            salida[subindicie][1] = cont_true
            salida[subindicie][2] = cont_false
            salida[subindicie][3] = round((cont_true / len(archivo[3])) * 100, 2)
            salida[subindicie][4] = round((cont_false / len(archivo[3])) * 100, 2)

            subindicie += 1
          #  if control !=0:
         #       print('detecta error: ',salida)

        else:
            if control==0:
                salida += [[[], [], [], [], []]]
                control=1
                salida[subindicie][0] = len(archivo[3])
                salida[subindicie][1] = cont_true
                salida[subindicie][2] = cont_false
                salida[subindicie][3]=100
                salida[subindicie][4] = 100
                subindicie+=1
            #print(salida)
        #print(salida)
    if prob== 60:
        Wr.write_ar(salida, 'resultados_prueba60.csv')
    if prob== 99:
        Wr.write_ar(salida, 'resultados_prueba99.csv')
    Wr.write_ar(salida, 'resultados_prueba.csv')
    import pandas as pd

    df = pd.read_csv('resultados_prueba.csv', index_col=0)
    #print(df[['Porcentja aciertos']])
    #print()
    media = round(df[['Porcentja aciertos']].get_values().mean(), 2)
    mini = round(df[['Porcentja aciertos']].get_values().min(), 2)
    maxi = round(df[['Porcentja aciertos']].get_values().max(), 2)
    var = round(df[['Porcentja aciertos']].get_values().var(), 2)
    desvi = round(df[['Porcentja aciertos']].get_values().std(), 2)
    analisis_Positivo_desvio += [[prueb, prob,
                                  media, mini,
                                  maxi, var, desvi]]
    prueb+=1
Wr.write_ar(analisis_Positivo_desvio, 'Analisi_resultados_prueba.csv')
df=pd.read_csv('Analisi_resultados_prueba.csv',index_col=0)
#print(df)
#df2=pd.read_csv('resultados_prueba.csv',index_col=0)
#print(df2[['Porcentja aciertos']].get_values().mean())
prob=df[['probabilidad']].get_values()
desvi = df[['media']].get_values()
plt.scatter(prob,desvi)
plt.savefig('Analisis media Datos3.png')
plt.xlabel('Porcentaje de Datos Entrenamiento')
plt.ylabel(' Porcentaje de la Media de Acierto')
plt.show()
#prob=df[['probabilidad']].get_values()
#desvi = df[['media']].get_values()
#plt.scatter(prob,desvi)
#plt.savefig('Analisis Media Positivo.png')
#plt.xlabel('Porcentaje de Datos Entrenamiento')
#plt.ylabel('Media de Acierto')

plt.show()
