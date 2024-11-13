vetor = []

for i in range(20):
    numero = int(input("digite um número: "))
    vetor.append(numero)

soma = 0

for i in range(10):
    soma += vetor[i]

print(soma)