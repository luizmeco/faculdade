colunas = int(input("Insira o número de colunas "))
if colunas < 1 or colunas > 20 :
    colunas = int(input("Insira o número de linhas entre 1 e 20 "))
numero = int(input("Insira um número"))
if numero < colunas or numero > 1000000 :
    linhas = int(input("Insira o número maior do que linhas"))
contador = 0

while contador < numero :
    for column in range(colunas):
        contador+=1
        print(contador," ", end="")      
    print(" ")

