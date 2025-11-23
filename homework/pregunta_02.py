"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

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


def pregunta_02():

    datos = leer_datos()
    conteo = {}

    for fila in datos:
        letra = fila[0]
        if letra not in conteo:
            conteo[letra] = 0
        conteo[letra] += 1

    resultado = sorted(conteo.items())
    return resultado


if __name__ == "__main__":
    print(pregunta_02())