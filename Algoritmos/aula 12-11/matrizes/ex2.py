matriz = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(i, j)
        matriz[i][j]= int(input("digite: "))

print(matriz)