import random

matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

menor_valor = min(min(linha)for linha in matriz)

print(matriz)
print(menor_valor)