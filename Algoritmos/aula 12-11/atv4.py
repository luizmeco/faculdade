vetor = []

for i in range(15):
    numero = int(input("digite um número: "))
    vetor.append(numero)


for i in range(len(vetor)):
    if vetor[i] >= 10:
        print(vetor[i])