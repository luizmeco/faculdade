def contar_caracteres(texto):
    contagem = {}
    for caractere in range(len(texto)):
        contagem[texto[caractere]] = caractere+1
        
    print(contagem)

contar_caracteres('Olá')