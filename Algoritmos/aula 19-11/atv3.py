vetor = [0]*10



for i in range(len(vetor)):
    numero = int(input('Insira um número: '))
    vetor[i] = numero

print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))