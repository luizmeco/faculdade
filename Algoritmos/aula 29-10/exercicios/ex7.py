def eh_par(n):
    return n%2 == 0

numero = int(input('insira um número'))

if eh_par(numero):
    print('é par')
else:
    print('é impar')