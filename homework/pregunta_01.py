"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne la suma de la segunda columna.

    Rta/
    214

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


def pregunta_01():

    datos = leer_datos()
    total = 0

    for fila in datos:
        valor = int(fila[1])  
        total += valor

    return total


if __name__ == "__main__":
    print(pregunta_01())









    
