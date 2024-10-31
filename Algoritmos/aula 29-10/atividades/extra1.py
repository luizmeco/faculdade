import json

def converter_para_json(dicionario):
    return json.dumps(dicionario, indent=4)

meu_dicionario = {
    'nome': 'Luiz',
    'sobrenome': 'Valandro',
    'data_aniversario': '18/05/2005',
}

print(converter_para_json(meu_dicionario))