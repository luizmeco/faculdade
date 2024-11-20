import random

vetor = [random.randint(1,10)for _ in range(5)]

sair = False

while sair == False:
    print('Se deseja sair do programa digite 0')
    print('Se deseja visualizar o vetor digite 1')
    print('Se deseja visualizar o vetor ao contrario digite 2')
    valor_usuario = int(input(''))
    if valor_usuario == 1:
        print(vetor)
    if valor_usuario == 2:
        vetor.reverse()
        print(vetor)
        vetor.reverse()
    if valor_usuario == 0:
        print('Programa Finalizou!')
        sair = True
