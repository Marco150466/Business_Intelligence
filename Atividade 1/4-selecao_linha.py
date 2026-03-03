import numpy as np

# 1. Criando um array com 4 linhas e 5 colunas
# Usamos np.arange(20).reshape(4, 5) para gerar dados sequenciais de 0 a 19
matriz = np.arange(20).reshape(4, 5)

print("Matriz Completa (4x5):")
print(matriz)

# 2. Imprimindo os elementos da terceira linha
terceira_linha = matriz[2]

print("\n--- Resultado Estratégico ---")
print(f"Elementos da 3ª linha: {terceira_linha}")