def calcular_media(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma/len(lista)

print(calcular_media([5,5,5,6]))