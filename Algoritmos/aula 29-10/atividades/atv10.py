def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    if imc < 18.5:
        return 'Abaixo do peso'
    if imc >= 18.5 and imc < 25:
        return 'Peso normal'
    else:
        return 'Acima do peso'
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

print(calcular_imc(peso,altura))