lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
cont_par = []
cont_impar = []

for num in lista:
    if num%2 == 0:
        cont_par.append(num)
    else:
        cont_impar.append(num)

print(cont_par)
print(cont_impar)