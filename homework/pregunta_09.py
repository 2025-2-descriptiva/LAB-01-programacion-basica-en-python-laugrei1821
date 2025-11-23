"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

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


def pregunta_09():

    datos = leer_datos()
    conteo_claves = {}

    for fila in datos:
        columna5 = fila[4]              
        pares = columna5.split(",")     

        for par in pares:
            clave, valor = par.split(":")   
            
            if clave not in conteo_claves:
                conteo_claves[clave] = 0

            conteo_claves[clave] += 1       
    return dict(sorted(conteo_claves.items()))


if __name__ == "__main__":
    print(pregunta_09())
