numero = int(input("Informe os números em ordem crescente: "))

vetor = [numero]


while len(vetor) < 7:
    numero = int(input("Informe outro número: "))
    if numero > len(vetor)-1:
        vetor.append(numero)
    else:
        print("Você digitou um número inferior ao anterior. Tente novamente.")
        
print(vetor)