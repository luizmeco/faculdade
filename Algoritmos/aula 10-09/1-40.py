r = 6
positivos = 0
while r>0 :
    r-=1
    num = int(input("Informe um número "))
    if num > 0 :
        positivos += 1
print(f"{positivos} valores positivos")
