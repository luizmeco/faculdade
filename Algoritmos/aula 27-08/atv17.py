quilometros = int(input("Infome quantos km rodou com o carro "))
dias = int(input("Infome quantos dias ficou com o carro "))

gastosTotais = (dias*140)+(quilometros*0.25)

print("A conta rica R$ " + f"{gastosTotais:,.2f}".replace(",","x").replace(".",",").replace("x","."))