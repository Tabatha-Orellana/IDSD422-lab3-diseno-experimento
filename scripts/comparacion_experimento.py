
# comparacion_experimento.py — Comparación de grupos (Python)
# Ejecutar desde la raíz del repositorio:
# python scripts/comparacion_experimento.py

import pandas as pd

# TODO 1: Cargar el archivo CSV
df = pd.read_csv("plantillas/registro_experimento.csv")

# TODO 2: Calcular el promedio de ventas por ubicación
print("Promedio de ventas por ubicación:")
print(df.groupby("ubicacion")["ventas_producto"].mean())

# TODO 3: Mostrar el número de registros por grupo
print("\nNúmero de registros por grupo:")
print(df["ubicacion"].value_counts())

# TODO 4: Interpretación de resultados
print("\nInterpretación:")
print("Los resultados muestran diferencias en los promedios de ventas.")
print("Sin embargo, con solo cuatro registros no podemos concluir que")
print("el cambio de ubicación del producto aumente las ventas.")
print("Se necesitan más observaciones y un experimento controlado.")
