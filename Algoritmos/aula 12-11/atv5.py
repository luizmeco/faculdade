vetor = []

for i in range(6):
    numero = int(input("digite um número: "))
    vetor.append(numero)

contador = len(vetor)
novo_vetor = []

for i in range(contador):
    contador -= 1
    novo_vetor.append(vetor[contador])

print(novo_vetor)
    