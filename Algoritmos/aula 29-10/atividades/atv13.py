def validar_cpf(texto):

    if len(texto) != 11:
        return False
    if texto.isdigit() == False:
        return False
    
    return True


cpf = '12345678910'

print(validar_cpf(cpf))