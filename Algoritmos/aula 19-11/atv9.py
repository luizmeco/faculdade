comprimentoVetor =  int(input("Insira o comprimento do vetor: "))

while comprimentoVetor > 10 or comprimentoVetor < 0:
    print('A dimensão deve ser igual ou inferior a 10')
    comprimentoVetor =  int(input("Insira o comprimento do vetor: "))

vetor = [0]*comprimentoVetor

for i in range(len(vetor)):
    numero = int(input("Insira um número inteiro no vetor: "))
    vetor[i] = numero

print(vetor)
