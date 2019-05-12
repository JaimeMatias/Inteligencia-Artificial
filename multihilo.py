import threading

def contar( valor=0,nombre=None,**datos):
    print(valor)
    print(nombre)
    '''Contar hasta cien'''
    contador = 0
    if valor!=0:
        num=valor
    else:
        print(datos['limite'])
        num=datos['limite']
    while contador<num:
        contador+=1
        print('Hilo:',
              threading.current_thread().getName(),
              'con identificador:',
              threading.current_thread().ident,
              'Contador:', contador)

hilo1 = threading.Thread(target=contar,args=[100,'nombre'])
hilo2 = threading.Thread(target=contar,kwargs={'limite':10})
hilo1.start()
hilo2.start()