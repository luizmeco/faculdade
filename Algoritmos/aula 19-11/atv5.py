import random

matriz = [[random.randint(1,10)for _ in range(3)]for _ in range(3)]

somaLinha = []

for i in range(len(matriz)):
    somaLinha.append(sum(matriz[i]))
    print(matriz[i])

print(max(somaLinha))