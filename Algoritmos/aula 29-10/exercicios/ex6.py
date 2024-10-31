def operacoes(a,b):
    soma = a+b
    subtracao = a-b
    multiplicacao = a*b
    divisao = a/b
    return [soma, subtracao, multiplicacao, divisao]

som,sub,mult,div = operacoes(5,5)

print(som)
print(sub)
print(mult)
print(div)