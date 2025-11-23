"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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


def pregunta_03():

    datos = leer_datos()
    suma_por_letra = {}

    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])

        if letra not in suma_por_letra:
            suma_por_letra[letra] = 0

        suma_por_letra[letra] += valor

    resultado = sorted(suma_por_letra.items())
    return resultado


if __name__ == "__main__":
    print(pregunta_03())
