import numpy as np

# 1. Criando um array (matriz) com 3 linhas e 2 colunas
# Usaremos valores sequenciais para facilitar a visualização da estrutura
matriz = np.array([[10, 20], [30, 40], [50, 60]])

# 2. Imprimindo o 'shape' (formato) da matriz
# O shape é uma tupla (linhas, colunas) - Essencial para validar cargas de dados
print(f"Shape da matriz: {matriz.shape}")

# 3. Imprimindo a 2ª linha da matriz 

segunda_linha = matriz[1]

print(f"A 2ª linha é: {segunda_linha}")