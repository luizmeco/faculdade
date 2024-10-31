usuario = {
    'name': 'Luiz',
    'last-name':'Valandro',
    'date':'18/05/2005',
}

for atr in usuario.values():
    print(atr)



for chave, valor in usuario.items():
    print(chave, '=', valor)