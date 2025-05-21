"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    # Cargar el archivo tbl1.csv
    df = pd.read_csv('tbl1.csv')

    # Obtener los valores únicos de la columna c4, convertir a mayúsculas y ordenar alfabéticamente
    unique_values = sorted(df['c4'].str.upper().unique())

    return unique_values

print(pregunta_06())