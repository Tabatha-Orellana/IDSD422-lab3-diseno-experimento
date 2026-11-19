
# comparacion_experimento.R — Comparación de grupos (R)
# Ejecutar desde la raíz del repositorio:
# Rscript scripts/comparacion_experimento.R

# TODO 1: Cargar el archivo CSV
df <- read.csv("plantillas/registro_experimento.csv")

# TODO 2: Calcular el promedio de ventas por ubicación
cat("Promedio de ventas por ubicación:\n")
print(aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean))

# TODO 3: Mostrar el número de registros por grupo
cat("\nNúmero de registros por grupo:\n")
print(table(df$ubicacion))

# TODO 4: Interpretación de resultados
cat("\nInterpretación:\n")
cat("Los resultados muestran diferencias en los promedios de ventas.\n")
cat("Sin embargo, con solo cuatro registros no podemos concluir que\n")
cat("el cambio de ubicación del producto aumente las ventas.\n")
cat("Se necesitan más observaciones y un experimento controlado.\n")
