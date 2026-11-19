# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** ___ · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.


## 1. Pregunta e hipótesis

**Pregunta de investigación:**

¿La ubicación del producto estrella de RetailAndina S.A. en el pasillo principal incrementa sus ventas promedio semanales en comparación con su ubicación habitual durante un período de cuatro semanas?

**Hipótesis nula (H0):**

Las ventas promedio semanales del producto estrella son iguales en las tiendas que mantienen su ubicación habitual y en las tiendas que lo colocan en el pasillo principal.

H0: μprincipal = μhabitual

**Hipótesis alternativa (H1):**

Las ventas promedio semanales del producto estrella son mayores en las tiendas que lo colocan en el pasillo principal que en aquellas que mantienen su ubicación habitual.

H1: μprincipal > μhabitual

**Justificación:**

Se plantea una comparación entre dos grupos de tiendas para determinar si cambiar la ubicación del producto estrella influye en sus ventas. La hipótesis es medible porque utiliza como variable de respuesta las unidades vendidas por semana, permitiendo comparar los promedios de ambos grupos durante cuatro semanas.


## 2. Unidad experimental

*¿Qué recibe el tratamiento? ¿Cuántas unidades se incluyen?*

- Unidad:
- Número de unidades y justificación:

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada):
- **Niveles** (valores del factor):
- **Tratamiento** (combinación asignada):

## 4. Grupo de control

*¿Cuál es la referencia sin tratamiento y qué rol cumple?*

## 5. Aleatorización

*¿Cómo se asignan las unidades a los grupos? ¿Por qué es necesaria?*

- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- Variable respuesta:
- Período de medición:
- Quién registra y cómo (¿ciego?):

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
