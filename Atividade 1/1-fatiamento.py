import numpy as np

# 1. Criação do array de 10 elementos (0 a 9)
# Usamos arange para eficiência, mas poderia ser np.array([list])
array = np.arange(10)
print(f"Array original: {array}")

# 2. Alteração dos valores com índices de 5 até 8 para 0
# Importante: O fatiamento [5:9] inclui o índice 5 e vai ATÉ o 8 (o 9 é exclusivo)
array[5:9] = 0

# 3. Exibição do resultado para validação
print(f"Array modificado: {array}")