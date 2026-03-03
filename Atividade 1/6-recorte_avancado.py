import numpy as np

# 1. Criando a matriz de 4 linhas e 5 colunas
# Usaremos números de 1 a 20 para facilitar o rastreio visual
matriz = np.arange(1, 21).reshape(4, 5)

print("Matriz Completa (4x5):")
print(matriz)

# 2. Extraindo o recorte solicitado:
# Linhas: 2ª e 3ª (índices 1 e 2) -> Slicing [1:3]
# Colunas: 1ª à 3ª (índices 0, 1 e 2) -> Slicing [0:3]
recorte_final = matriz[1:3, 0:3]

print("\n--- Resultado do Recorte Avançado ---")
print("Elementos da 2ª e 3ª linhas (Colunas 1 a 3):")
print(recorte_final)