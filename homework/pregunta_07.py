"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

def leer_datos():
    ruta = r"C:\Especializacion-Analitica\Descriptiva\LAB-01-programacion-basica-en-python-laugrei1821\files\input\data.csv"
    datos = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()              
            partes = linea.split("\t")         
            datos.append(partes)               
    return datos


def pregunta_07():

    datos = leer_datos()
    asociaciones = {}

    for fila in datos:
        letra = fila[0]           # Columna 0
        numero = int(fila[1])     # Columna 1 (entero)

        if numero not in asociaciones:
            asociaciones[numero] = []

        asociaciones[numero].append(letra)

    salida = []
    for numero in sorted(asociaciones.keys()):
        salida.append((numero, asociaciones[numero]))

    return salida


if __name__ == "__main__":
    print(pregunta_07())
