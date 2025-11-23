"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

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


def pregunta_04():

    datos = leer_datos()
    conteo_meses = {}

    for fila in datos:
        fecha = fila[2]          
        partes = fecha.split("-")  
        mes = partes[1]        

        if mes not in conteo_meses:
            conteo_meses[mes] = 0

        conteo_meses[mes] += 1

    resultado = sorted(conteo_meses.items())
    return resultado


if __name__ == "__main__":
    print(pregunta_04())
