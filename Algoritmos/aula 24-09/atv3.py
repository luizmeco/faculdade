lista = [-1, 2, 3, -4, 5, 6, 7, 8, -9, -1]

for num in lista:
    if num < 0:
        lista.remove(num)

print(lista)