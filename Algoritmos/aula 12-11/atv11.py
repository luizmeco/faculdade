import random

vetor = [random.randint(1, 100) for _ in range(30)]

soma = 0

print('numeros pares: ')
for i in vetor:
    soma += i
    if i % 2 == 0:
        print(i, end=', ')
print('')


media = soma/(len(vetor)+1)



print(f"maior valor: {max(vetor)}")
print(f"menor valor: {min(vetor)}")
print('maiores que a média: ')

for i in vetor:
    if i > media:
        print(i, end=', ')


