"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


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


def pregunta_11():

    datos = leer_datos()
    resultado = {}

    for fila in datos:
        valor_col2 = int(fila[1])          
        letras_col4 = fila[3].split(",")   

        for letra in letras_col4:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += valor_col2

    return dict(sorted(resultado.items()))


if __name__ == "__main__":
    print(pregunta_11())
