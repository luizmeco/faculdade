string = input("Informe Qualquer coisa ")

espaco = string.find(" ")
if espaco != -1 :
    print("Contém espaço")
else :
    print("Não contém espaços")

eNumero = string.isnumeric()
if eNumero :
    print("é um número")
else :
    print("Não é um número")

caracteresAlfabeticos = string.isalpha()
if caracteresAlfabeticos :
    print("é alfabético")
else :
    print("não é alfabético")

caracteresAlfanumericos = string.isalnum()
if caracteresAlfanumericos :
    print("é alfanumérico")
else :
    print("não é alfanumérico")

maiusculo = string.isupper()
if maiusculo :
    print("está em maiúsculo")
else :
    print("não está em maiúsculo")

minusculo = string.islower()
if minusculo :
    print("está em minúsculo")
else :
    print("não está em minúsculo")

capitalizada = string.istitle()
if capitalizada :
    print("está capitalizada")
else :
    print("não está capitalizada")




