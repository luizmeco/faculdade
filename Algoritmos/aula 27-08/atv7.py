real = float(input("Informe um valor em Real "))
cota = 5.51
dolar = real * cota

print("Valor em Dólares $ " + f"{dolar:,.2f}".replace(",","x").replace(".",",").replace("x","."))