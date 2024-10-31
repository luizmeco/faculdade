name = input("Informe seu nome:")
last_name = input("Informe seu sobrenome:")
date = input("Informe a data do seu aniversário:")

def pessoa(name, last_name, date):
    print(f'Olá {name} {last_name}')
    if date:
        print(f'Você faz aniversário em {date}')

pessoa(name, last_name, date)