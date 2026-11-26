import time
import functools
from servicios.logs import logger

#Decorador para medir el tiempo de ejecucion
def medir_tiempo(funcion):
    @functools.wraps(funcion)  # conserva nombre y docstring de la funcion original
    def envoltura(*args, **kwargs):
        inicio = time.time()

        # Ejecutamos la funcion original; si falla, se registra ERROR
        try:
            resultado = funcion(*args, **kwargs)
        except ValueError:
            # Un ValueError es una validacion rechazada: ya quedo registrada
            # como WARNING en validaciones.py, asi que aqui solo la reenviamos
            # (un dato invalido NO es una falla del programa)
            raise
        except Exception as error:
            # Cualquier otro fallo (por ejemplo, no poder leer o escribir un
            # archivo) si se registra como ERROR
            logger.error(f"La funcion {funcion.__name__} falló: {error}")
            raise
        
        fin = time.time()
        tiempo_total = fin - inicio
        
        # redondeamos a 4 decimales usando round() (para que sea mas facil de entender)
        tiempo_redondeado = round(tiempo_total, 4)
        
        # guardamos en el log de forma sencilla
        mensaje = "La funcion " + funcion.__name__ + " tardo " + str(tiempo_redondeado) + " segundos."
        logger.info(mensaje)
        
        return resultado
    return envoltura