
import numpy as np

tiendas = [f"T{i:02d}" for i in range(1, 11)]

rng = np.random.default_rng(1234597)

tiendas_aleatorias = rng.permutation(tiendas)
experimental = tiendas_aleatorias[:5]
control = tiendas_aleatorias[5:]

print("Grupo experimental (pasillo principal):")
print(experimental.tolist())

print("\nGrupo de control (ubicación habitual):")
print(control.tolist())
