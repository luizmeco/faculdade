lista = [1, 0, 7, 4, 5, 0, 7, 0, 9]


for num in lista:
    if num == 0:
        lista.remove(0)
        lista.append(0)

print(lista)