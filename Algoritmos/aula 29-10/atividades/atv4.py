def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contagem_vogais = 0
    for caractere in texto:
        if caractere in vogais:
            contagem_vogais += 1
    return contagem_vogais

print(contar_vogais('Olaaa'))