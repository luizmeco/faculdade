date=input("Informe a data de hoje: ")
name_user=input("Informe a data de hoje: ")
last_name_user=input("Informe a data de hoje: ")
def hello(name, last_name, datestring=''):
    msg = f'Hello {name} {last_name}'
    if datestring:
        msg += f', hoje é dia {datestring}'
    print(msg)

hello(datestring="22/10/2024", name="Luiz", last_name="Valandro")