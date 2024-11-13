import random

vetor = [random.randint(1, 10) for _ in range(4)]

print(f'As notas são: {vetor}')
print(f'A maior nota é: {max(vetor)}')
print(f'A menor nota é: {min(vetor)}')
soma = 0

for i in vetor:
    soma += i
    

media = soma/(len(vetor)+1)

print(f'A media é: {media}')
