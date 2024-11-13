import random

vetor = [random.randint(1, 100) for _ in range(10)]

maior_valor = max(vetor)
menor_valor = min(vetor)

print(vetor)

print(f'posição do maior: {vetor.index(maior_valor)}')
print(f'posição do menor: {vetor.index(menor_valor)}')