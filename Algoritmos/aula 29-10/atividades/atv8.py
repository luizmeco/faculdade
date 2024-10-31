import random

def rolar_dados():
    numero_aleatorio_1 = random.randint(1,6)
    numero_aleatorio_2 = random.randint(1,6)

    return numero_aleatorio_1 + numero_aleatorio_2

print(rolar_dados())