lista = [1, 6, 7, 4, 5, 6, 7, 10, 9, 10,11,12,13,14,15,16,17,18,19,20]
cont_par = []
cont_impar = []

for num in lista:
    while lista.count(num) > 1:
            lista.remove(num)

print(lista)