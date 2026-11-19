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

- **Variable respuesta:** Número de unidades vendidas por semana del producto estrella en cada tienda de RetailAndina S.A. Esta variable es cuantitativa discreta y permitirá comparar las ventas promedio semanales entre el grupo experimental y el grupo de control.

- **Período de medición:** Cuatro semanas consecutivas. Se registrarán las ventas del producto estrella al finalizar cada semana en las 10 tiendas participantes. Se obtendrán 40 registros semanales (10 tiendas × 4 semanas), correspondientes a 10 unidades experimentales.

- **Quién registra y cómo (¿ciego?):** Las ventas serán registradas mediante el sistema de punto de venta (POS) de cada tienda. Al finalizar cada semana, el equipo de Business Intelligence recopilará los datos y verificará que correspondan al mismo producto y período de medición.

No será posible aplicar un cegamiento completo, porque el personal de las tiendas podrá observar la ubicación del producto. Sin embargo, se utilizarán registros automáticos de ventas para reducir posibles sesgos de medición. Siempre que sea posible, el análisis inicial se realizará con los grupos identificados mediante códigos, sin revelar cuál corresponde al tratamiento.

Cada registro incluirá el código de la tienda, la semana, la ubicación asignada y las unidades vendidas del producto estrella.



## 7. Factores a controlar (mínimo 4)

Para que las diferencias en las ventas puedan atribuirse con mayor confianza a la ubicación del producto estrella, se identificarán y controlarán otros factores que podrían influir en los resultados.

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Precio del producto | Se mantendrá el mismo precio de venta del producto estrella en las 10 tiendas durante las cuatro semanas. Cualquier cambio excepcional se registrará para considerarlo en el análisis. |
| 2. Promociones y descuentos | Se evitarán promociones exclusivas del producto durante el experimento. Si existe una promoción general que no pueda suspenderse, se registrarán la tienda, la semana y el tipo de promoción. |
| 3. Disponibilidad de inventario | Se verificará diariamente que cada tienda disponga de existencias suficientes. Se registrarán los días con agotamiento de stock, ya que podrían reducir las ventas independientemente de la ubicación. |
| 4. Afluencia de clientes | Se registrará el número de clientes o transacciones por tienda y semana mediante los sistemas disponibles. Esto permitirá evaluar si las diferencias de ventas están relacionadas con el flujo de compradores. |
| 5. Temporada y días especiales | Ambos grupos serán observados durante las mismas cuatro semanas. Se registrarán feriados, eventos comerciales y fechas especiales que puedan modificar la demanda. |
| 6. Características de las tiendas | Se registrarán la ciudad, el tamaño y el volumen histórico de ventas de cada tienda. Estas características se revisarán antes de la asignación para identificar posibles desequilibrios entre los grupos. |

**Justificación:**

El control de estos factores permitirá reducir la influencia de variables externas sobre las ventas del producto estrella. La asignación aleatoria ayudará a distribuir las características de las tiendas entre los grupos, mientras que el registro de precios, promociones, inventario y afluencia permitirá identificar posibles factores de confusión.

Aunque estos controles no eliminan completamente todos los sesgos, contribuyen a que la comparación entre el grupo experimental y el grupo de control sea más confiable.



## 8. Limitaciones del diseño

El experimento presenta algunas limitaciones que deben considerarse para interpretar correctamente sus resultados.

1. **Tamaño de la muestra:** Se trabajará con 10 tiendas distribuidas en dos grupos de 5. Este número permite realizar un estudio piloto, pero podría ser insuficiente para detectar diferencias pequeñas en las ventas o generalizar los resultados a todas las tiendas de RetailAndina S.A.

2. **Diferencias entre tiendas:** Las tiendas pueden presentar distintas características, como ubicación geográfica, tamaño, afluencia de clientes y hábitos de consumo. Aunque la asignación aleatoria reduce el sesgo de selección, no garantiza que ambos grupos sean completamente equivalentes.

3. **Promociones y disponibilidad del producto:** Las promociones imprevistas, los cambios de precio o la falta de inventario podrían modificar las ventas independientemente de la ubicación del producto. Si estos factores no se controlan o registran adecuadamente, podrían afectar la validez de la comparación.

4. **Duración del experimento:** El período de cuatro semanas podría ser insuficiente para identificar efectos a largo plazo, variaciones estacionales o cambios permanentes en el comportamiento de los consumidores.

5. **Ausencia de cegamiento completo:** El personal de las tiendas podrá observar la ubicación del producto y conocer la intervención, lo que podría modificar involuntariamente su comportamiento, por ejemplo, al recomendarlo con mayor frecuencia.

6. **Limitaciones de la interpretación:** Los resultados permitirán estimar el efecto de la ubicación del producto en las tiendas participantes durante el período estudiado, siempre que se respete la asignación y se controlen adecuadamente los factores externos. Sin embargo, no permitirán asegurar que el mismo efecto ocurra en todas las tiendas, en otros períodos o con productos diferentes.

**Conclusión:**

El diseño propuesto permite evaluar de manera controlada la relación causal entre la ubicación del producto estrella y sus ventas. No obstante, la interpretación dependerá del cumplimiento del protocolo, la calidad de los registros y el control de los factores externos. Por ello, cualquier resultado deberá analizarse considerando las limitaciones señaladas.


## 9. Comparación en código (Python/R)

Se utilizó Python y la biblioteca pandas para analizar los datos de ejemplo contenidos en `plantillas/registro_experimento.csv`. El programa se encuentra en `scripts/comparacion_experimento.py` y permite calcular las ventas promedio por ubicación y contar los registros de cada grupo.

**Resultados de la ejecución:**

```text
Promedio de ventas por ubicación:
ubicacion
habitual             1040.0
pasillo_principal    1335.0
Name: ventas_producto, dtype: float64

Número de registros por grupo:
ubicacion
pasillo_principal    2
habitual             2
Name: count, dtype: int64
```

**¿Qué grupo muestra mayor venta promedio en la plantilla?**

El grupo del pasillo principal presenta un promedio de 1335 unidades vendidas, mientras que el grupo de ubicación habitual registra 1040 unidades. La diferencia descriptiva es de 295 unidades a favor del pasillo principal.

**¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?**

La plantilla contiene solamente cuatro registros, dos por grupo. Esta cantidad es insuficiente para evaluar adecuadamente la variabilidad de las ventas y distinguir un posible efecto del tratamiento de fluctuaciones aleatorias u otros factores externos. Además, los datos de ejemplo no constituyen resultados de un experimento controlado.

**Si el experimento se ejecutara con nuestro protocolo, ¿qué le faltaría a este análisis para ser justo?**

Se necesitarían los registros de las 10 tiendas asignadas aleatoriamente durante cuatro semanas, así como información sobre precios, promociones, inventario y afluencia de clientes. También sería necesario considerar que las cuatro mediciones de cada tienda no son independientes y utilizar un análisis estadístico adecuado para evaluar el efecto de la ubicación y su incertidumbre.

**Conclusión:**

Aunque el pasillo principal presenta mayores ventas promedio en los datos de ejemplo, estos resultados no permiten afirmar que cambiar la ubicación del producto aumente sus ventas. El análisis demuestra únicamente cómo se compararían los grupos. Para obtener conclusiones fundamentadas sería necesario ejecutar el protocolo experimental diseñado.
```

