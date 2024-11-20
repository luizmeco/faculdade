import random

vetor = [random.randint(1,100)for _ in range(1000000)]
vetorDosPrimos = []


def verificarPrimo(num):
    ehPrimo = True
    if num >= 1:
        for numero in range(2, num):
            if num % numero == 0:
                ehPrimo = False
    return ehPrimo


for i in vetor:
    if verificarPrimo(i) == True:
        vetorDosPrimos.append(i)

print(vetorDosPrimos)

