num = input('Insira um número ')
inicio_user = input('Insira o mínimo do intervalo ')
fim_user = input('Insira o maximo do intervalo')

def imprimir_tabuada(n, inicio=1, fim=10):
    #mostra a tabuada de um número informado pelo usuário em um intervalo específico
    for i in range(inicio, fim+1):
        print(f'{i}x{n}={i*n}')

imprimir_tabuada(n=int(num), inicio=int(inicio_user), fim=int(fim_user))