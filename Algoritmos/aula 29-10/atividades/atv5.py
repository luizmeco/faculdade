def eh_palindromo(texto):
    contagem_retroativa = len(texto)
    texto_contrario = ''

    for i in range(len(texto)):

        contagem_retroativa -= 1
        texto_contrario += texto[contagem_retroativa]
    
    if texto_contrario == texto:
        return True
    
    return False


print(eh_palindromo('tenet'))