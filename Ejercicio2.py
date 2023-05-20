import numpy as np

def calcularCostoMinimo():
  costos = {
    (1, 2): 8,
    (1, 3): 5,
    (1, 4): 7,
    (2, 5): 9,
    (3, 5): 6,
    (3, 6): 6,
    (3, 7): 16,
    (3, 8): 10,
    (4, 6): 5,
    (4, 8): 11,
    (5, 9): 4,
    (5, 10): 4,
    (6, 9): 4,
    (7, 9): 8,
    (7, 11): 8,
    (8, 10): 1,
    (8, 11): 5,
    (9, 12): 8,
    (10, 12): 7,
    (11, 12): 3
  }

  n = 12  # Número total de nodos en el grafo
  inf = float('inf')
  dp = np.full((n + 1), inf)  # Inicializar el arreglo con infinito
  dp[1] = 0  # El costo para llegar al nodo inicial es 0

  # Calcular el costo mínimo para llegar a cada nodo
  for i in range(1, n):
    for j in range(i + 1, n + 1):
      if (i, j) in costos:
        dp[j] = min(dp[j], dp[i] + costos[(i, j)])

  return dp[n]  # El costo mínimo para llegar al nodo final

# Llamar a la función para obtener el costo mínimo
costoMinimo = calcularCostoMinimo()

# Imprimir el costo mínimo
print("El costo mínimo de la ruta óptima es:", costoMinimo)
