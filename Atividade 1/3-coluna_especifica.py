import numpy as np

# 1. Criando um array com 3 linhas e 2 colunas
# Usaremos valores diferentes para cada coluna para facilitar a identificação
matriz = np.array([
    [10, 100], 
    [20, 200], 
    [30, 300]
])

# 2. Imprimindo a 2ª coluna
# Sintaxe: matriz[todas_as_linhas , coluna_indice_1]
# O ':' indica que queremos todas as linhas.
segunda_coluna = matriz[:, 1]

print("Matriz Completa:")
print(matriz)

print("\nExtração da 2ª Coluna (Índice 1):")
print(segunda_coluna)