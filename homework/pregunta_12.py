"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

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


def pregunta_12():

    datos = leer_datos()
    resultado = {}

    for fila in datos:
        letra = fila[0]           
        dicc_str = fila[4]          

        pares = dicc_str.split(",")  

        suma_valores = 0
        for p in pares:
            clave, valor = p.split(":")
            suma_valores += int(valor)

        if letra not in resultado:
            resultado[letra] = 0

        resultado[letra] += suma_valores

    return dict(sorted(resultado.items()))


if __name__ == "__main__":
    print(pregunta_12())
