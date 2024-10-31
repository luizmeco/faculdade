texto = "Ola esse texto repete algumas palavras luiz luiz luiz"
palavras = texto.lower().split()
print(palavras)
contador = 0

palavras_nao_repetidas = []

for palavra in palavras:
    if palavra in palavras_nao_repetidas:
        print("Nada")
    else:
        palavras_nao_repetidas.append(palavra)

print(palavras_nao_repetidas)


for palavra in palavras_nao_repetidas:
    print(f"Contém {palavras.count(palavra)} {palavra}")

