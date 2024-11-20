matriz = [[0]*5 for _ in range(5)]

for i in matriz:
    print(i)


for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][i]=1

for i in matriz:
    print(i)