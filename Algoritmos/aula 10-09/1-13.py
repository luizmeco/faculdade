num1 = input("Informe um número ")
num2 = input("Informe um número ")
num3 = input("Informe um número ")

if num1 > num2 and num1 > num3 :
    print(f"o maior número eh o: {num1}")
if num2 > num1 and num2 > num3 :
    print(f"o maior número eh o: {num2}")
if num3 > num1 and num3 > num2:
    print(f"o maior número eh o: {num3}")
else:
    print(f"o maior número eh o: {num3}")