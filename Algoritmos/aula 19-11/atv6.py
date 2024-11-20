import random

matriz = [[random.randint(1,10)for _ in range(5)]for _ in range(5)]

valor = int(input('Insira um número'))
contagem = 0

for i in matriz:
    print(i)
    contagem += i.count(valor)

print(contagem)