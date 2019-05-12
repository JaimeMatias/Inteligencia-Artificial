import threading

def contar(num_hilo, **datos):
    contador = datos['inicio']
    incremento = datos['incremento']
    limite = datos['limite']
    while contador<=limite:
        print('hilo:', num_hilo, 'contador:', contador)
        contador+=incremento

for num_hilo in range(3):
    hilo = threading.Thread(target=contar,
                            args=(num_hilo,),
                            kwargs={'inicio':0,
                                    'incremento':1,
                                    'limite':10})
    hilo.start()