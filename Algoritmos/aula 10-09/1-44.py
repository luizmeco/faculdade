r = 5

pares = 0
impares = 0
positivos = 0
negativos = 0



while r>0 :
    r-=1
    num = int(input("Informe um número "))
    if num > 0 :
        positivos += 1
    if num < 0 :
        negativos += 1
    if num % 2 == 0 :
        pares += 1
    if num % 2 != 0 :
        impares += 1

print(f"{pares} valores pares")
print(f"{impares} valores impares")
print(f"{positivos} valores positivos")
print(f"{negativos} valores negativos")


