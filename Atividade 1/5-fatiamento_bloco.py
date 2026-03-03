import numpy as np

# 1. Criando o array de 4 linhas e 5 colunas
# Usamos arange(1, 21) para que os números fiquem de 1 a 20 (mais fácil de ler)
matriz = np.arange(1, 21).reshape(4, 5)

print("Matriz Original (4x5):")
print(matriz)

# 2. Extraindo o bloco específico:
# Linhas: 1ª e 2ª (índices 0 e 1) -> Slicing [0:2]
# Colunas: 2ª e 3ª (índices 1 e 2) -> Slicing [1:3]
recorte = matriz[0:2, 1:3]

print("\n--- Recorte Estratégico ---")
print("Elementos da 1ª e 2ª linhas (apenas 2ª e 3ª colunas):")
print(recorte)