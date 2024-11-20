import random


vetor = [random.randint(-10,10)for _ in range(10)]

negativos = 0
soma = 0

for i in vetor:
    if i<0:
        negativos+=1
    else:
        soma+=i

print(vetor)
print(negativos)
print(soma)