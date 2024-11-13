import random
t = 8

vetor_a = [random.randint(1, 100) for _ in range(t)]

vetor_b = [0]*t


for i in range(len(vetor_b)):
    vetor_b[i] = vetor_a[i]*3

print(vetor_a)
print(vetor_b)