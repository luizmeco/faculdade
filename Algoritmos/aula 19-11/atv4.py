vetor = [0]*6



for i in range(len(vetor)):
    numero = int(input('Insira um número: '))
    if numero%2 == 0:
        vetor[i] = numero

vetor.reverse()
print(vetor)