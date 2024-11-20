import random


matriz = [[random.randint(1,10)for _ in range(4)] for _ in range(4)]
soma = 0
for i in range(len(matriz)):
    soma += matriz[i][i]
        


for i in matriz:
    print(i)

print('soma da diagonal principal: ')
print(soma)