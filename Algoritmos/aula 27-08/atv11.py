nota1 = int(input("Informe a primeira nota "))
peso1 = int(input("Informe o peso da primeira nota "))
nota2 = int(input("Informe a primeira nota "))
peso2 = int(input("Informe o peso da segunda nota "))
nota3 = int(input("Informe a primeira nota "))
peso3 = int(input("Informe o peso da terceira nota "))

mediaPonderada = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/(peso1 + peso2 +peso3)

print(f"A média ponderada das notas é {mediaPonderada}")