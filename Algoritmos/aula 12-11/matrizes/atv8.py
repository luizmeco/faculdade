import random


matriz = [[random.randint(1,10)for _ in range(3)] for _ in range(2)]
m2 = [[random.randint(1,10)for _ in range(3)] for _ in range(3)]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        m2[j][i]=matriz[i][j]


print(matriz)
print(m2)


