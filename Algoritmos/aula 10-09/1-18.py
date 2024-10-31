num = int(input("Informe um número: "))

if num < 0 or num > 1000000 :
    num = int(input("Informe um número maior do que 0 e menor que 1000000 "))

if num > 0:
    print(f"{int(num/100)} nota(s) de R$ 100,00")
    num = num%100

if num > 0:
    print(f"{int(num/50)} nota(s) de R$ 50,00")
    num = num%50

if num > 0:
    print(f"{int(num/20)} nota(s) de R$ 20,00")
    num = num%20

if num > 0:
    print(f"{int(num/10)} nota(s) de R$ 10,00")
    num = num%10

if num > 0:
    print(f"{int(num/5)} nota(s) de R$ 5,00")
    num = num%5

if num > 0:
    print(f"{int(num/2)} nota(s) de R$ 2,00")
    num = num%2

if num > 0:
    print(f"{int(num/1)} nota(s) de R$ 1,00")
    num = num%1

