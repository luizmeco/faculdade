lista = [-1, 2, 3, -4, 5, 6, 7, 8, -9, -1]
cont_par = 0
cont_impar = 0

for num in lista:
    if num%2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(cont_par)
print(cont_impar)