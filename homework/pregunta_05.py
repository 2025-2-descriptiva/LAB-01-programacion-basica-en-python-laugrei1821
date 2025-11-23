"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

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

def pregunta_05():

    datos = leer_datos()
    resultados = {}

    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])


        if letra not in resultados:
            resultados[letra] = [valor, valor]
        else:
            
            if valor > resultados[letra][0]:
                resultados[letra][0] = valor

            
            if valor < resultados[letra][1]:
                resultados[letra][1] = valor


    salida = []
    for letra in sorted(resultados.keys()):
        maximo, minimo = resultados[letra]
        salida.append((letra, maximo, minimo))

    return salida


if __name__ == "__main__":
    print(pregunta_05())

