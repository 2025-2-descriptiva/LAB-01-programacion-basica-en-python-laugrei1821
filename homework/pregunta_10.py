"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

def leer_datos():
    ruta = "files/input/data.csv"
    datos = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            partes = linea.split("\t")
            datos.append(partes)
    return datos


def pregunta_10():

    datos = leer_datos()
    salida = []

    for fila in datos:
        letra = fila[0]                    
        col4 = fila[3].split(",")          
        col5 = fila[4].split(",")          

        num_col4 = len(col4)               
        num_col5 = len(col5)

        salida.append((letra, num_col4, num_col5))

    return salida

if __name__ == "__main__":
    print(pregunta_10())
