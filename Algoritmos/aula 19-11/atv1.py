import random


vetor = [random.randint(1,10)for _ in range(10)]

pares = 0

for i in vetor:
    if i%2 == 0:
        pares+=1

print(vetor)
print(pares)