num1= input("Informe Um número: ")
num2= input("Informe Um número: ")

def comparar(num1_user, num2_user):
    #realiza a comparação entre dois numeros para ver se são iguais maiores ou menores
    if num1_user == num2_user:
        print('Os números são iguais')
    elif num1_user > num2_user:
        print(f'O {num1_user} é maior que {num2_user}')
    else:
        print(f'O {num1_user} é menor que {num2_user}')

comparar(num1_user=int(num1), num2_user=int(num2))