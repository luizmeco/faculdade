import random

matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
print(matriz)
for i in matriz:
    print('soma de cada linha: ')
    print(sum(i))