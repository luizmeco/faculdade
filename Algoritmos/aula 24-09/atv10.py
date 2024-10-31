lista1 = [1, 6, 7, 4, 5, 6, 7, 10, 9, 10,11,12,13,14,15,16,17,18,19,20]
lista2 = [1, 6, 7,]
ambas = []

for num in lista1:
    if num in lista2:
        ambas.append(num)

print(ambas)
