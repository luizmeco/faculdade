from datetime import date
data_atual = date.today()
def mostrar_data():
    print(f'{data_atual.day}/{data_atual.month}/{data_atual.year}')

mostrar_data()