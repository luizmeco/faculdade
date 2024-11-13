import random

vetor = [random.randint(1, 100) for _ in range(5)]

print(vetor)

num_usuario = int(input("Informe um número: "))
resposta = []

for i in range(len(vetor)):
    if vetor[i] < num_usuario:
        resposta.append(vetor[i])

print(resposta)