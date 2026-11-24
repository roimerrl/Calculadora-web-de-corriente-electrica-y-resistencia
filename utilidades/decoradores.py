import time
from servicios.logs import logger

#Decorador para medir el tiempo de ejecucion
def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        
        # Ejecutamos la funcion original
        resultado = funcion(*args, **kwargs)
        
        fin = time.time()
        tiempo_total = fin - inicio
        
        # redondeamos a 4 decimales usando round() (para que sea mas facil de entender)
        tiempo_redondeado = round(tiempo_total, 4)
        
        # guardamos en el log de forma sencilla
        mensaje = "La funcion " + funcion.__name__ + " tardo " + str(tiempo_redondeado) + " segundos."
        logger.info(mensaje)
        
        return resultado
    return envoltura