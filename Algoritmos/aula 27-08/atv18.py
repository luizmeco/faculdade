peso = int(input("Informe seu peso "))
altura = float(input("Informe sua altura "))

imc = peso/(altura*altura)

if imc <= 18.4 :
    print("abaixo do peso")
if imc >= 18.5 and imc <= 24.9:
    print("peso normal")
if imc >= 25 and imc <= 29.9:
    print("acima do peso")
if imc >= 30:
    print("obesidade")

print(f"{imc}")