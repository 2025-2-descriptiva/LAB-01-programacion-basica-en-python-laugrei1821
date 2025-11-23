"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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


def pregunta_06():

    datos = leer_datos()
    valores = {}

    for fila in datos:
        columna_5 = fila[4]             
        pares = columna_5.split(",")     

        for par in pares:
            clave, numero = par.split(":")
            numero = int(numero)

            if clave not in valores:
                valores[clave] = [numero, numero]  
            else:
                if numero < valores[clave][0]:
                    valores[clave][0] = numero
                if numero > valores[clave][1]:
                    valores[clave][1] = numero

    salida = []
    for clave in sorted(valores.keys()):
        minimo, maximo = valores[clave]
        salida.append((clave, minimo, maximo))

    return salida


if __name__ == "__main__":
    print(pregunta_06())
