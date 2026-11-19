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

- **Unidad:** Cada tienda de RetailAndina S.A. constituye una unidad experimental, porque es el establecimiento al que se asigna una de las dos condiciones de ubicación del producto estrella.

- **Número de unidades y justificación:** Se seleccionarán 10 tiendas de RetailAndina S.A., distribuidas aleatoriamente en dos grupos de 5 tiendas cada uno. El grupo experimental ubicará el producto estrella en el pasillo principal, mientras que el grupo de control mantendrá su ubicación habitual.

Las 10 tiendas participarán durante cuatro semanas consecutivas, manteniendo la ubicación asignada durante todo el período. Se registrarán las ventas semanales del producto en cada establecimiento, obteniendo 40 registros de ventas.

Este tamaño se propone como un estudio piloto que permite evaluar la viabilidad del protocolo y comparar ambos grupos. Sin embargo, no garantiza suficiente potencia estadística para detectar diferencias pequeñas, por lo que sería necesario realizar un cálculo formal del tamaño muestral antes de implementar un experimento definitivo.


## 3. Factor, niveles y tratamiento

- **Factor (variable manipulada):** La ubicación del producto estrella dentro de las tiendas de RetailAndina S.A. Esta variable será manipulada por el equipo investigador para evaluar su efecto sobre las ventas promedio semanales.

- **Niveles (valores del factor):**
  1. Ubicación habitual: el producto permanece en el lugar donde normalmente se comercializa.
  2. Pasillo principal: el producto se traslada al pasillo principal de la tienda.

- **Tratamiento (combinación asignada):**
  - Grupo experimental: 5 tiendas recibirán la intervención, que consiste en trasladar el producto estrella al pasillo principal durante cuatro semanas consecutivas.
  - Grupo de control: 5 tiendas mantendrán el producto en su ubicación habitual durante el mismo período, sin recibir la intervención.

La asignación de las tiendas a los grupos se realizará aleatoriamente antes del inicio del experimento. Ambos grupos mantendrán su condición durante las cuatro semanas para permitir una comparación de las ventas promedio semanales.


## 4. Grupo de control

El grupo de control estará conformado por 5 tiendas de RetailAndina S.A., seleccionadas mediante asignación aleatoria, que mantendrán el producto estrella en su ubicación habitual durante las cuatro semanas del experimento.

Estas tiendas no recibirán la intervención de trasladar el producto al pasillo principal. Sin embargo, se registrarán sus ventas semanales utilizando el mismo procedimiento aplicado al grupo experimental.

**Función del grupo de control:**

Servir como referencia para comparar las ventas del producto estrella entre las tiendas que mantienen su ubicación habitual y aquellas que reciben el tratamiento.

Esta comparación permitirá estimar si existen diferencias en las ventas promedio semanales asociadas al cambio de ubicación. La asignación aleatoria y el control de otros factores ayudarán a reducir posibles sesgos y explicaciones alternativas.

Ambos grupos tendrán el mismo período de observación y las mismas condiciones comerciales, excepto por la ubicación del producto estrella.


## 5. Aleatorización

Las 10 tiendas participantes serán asignadas aleatoriamente a dos grupos de igual tamaño: 5 tiendas al grupo experimental (pasillo principal) y 5 tiendas al grupo de control (ubicación habitual).

La asignación se realizará mediante un sorteo computacional en Python, utilizando una semilla fija que permitirá reproducir los resultados.

**Código de asignación aleatoria (Python):**

```python
import numpy as np

tiendas = [f"T{i:02d}" for i in range(1, 11)]
rng = np.random.default_rng(1234597)

tiendas_aleatorias = rng.permutation(tiendas)

experimental = tiendas_aleatorias[:5]
control = tiendas_aleatorias[5:]

print("Grupo experimental:", experimental.tolist())
print("Grupo de control:", control.tolist())
```

**Resultado de la ejecución:**


Grupo experimental (pasillo principal):
['T01', 'T07', 'T08', 'T06', 'T09']

Grupo de control (ubicación habitual):
['T10', 'T05', 'T03', 'T02', 'T04']


**Justificación:**

La aleatorización permite que todas las tiendas tengan la misma probabilidad de ser asignadas a cualquiera de los dos grupos. Esto ayuda a distribuir los factores conocidos y desconocidos que podrían influir en las ventas, como diferencias de clientes, ubicación geográfica o afluencia.
La asignación aleatoria no garantiza que ambos grupos sean idénticos, especialmente con solo 10 tiendas, pero reduce el sesgo de selección.
Cada tienda conservará su ubicación asignada durante las cuatro semanas del experimento.


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
