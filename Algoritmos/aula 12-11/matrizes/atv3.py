import random

matriz = [[random.randint(1, 10) for _ in range(2)] for _ in range(2)]
contador = 0
soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        soma += matriz[i][j]
        contador += 1
        media = soma/contador

print(matriz)
print(soma)
print(contador)
print(media)

