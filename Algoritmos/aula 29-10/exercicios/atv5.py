alunos ={
    'luiz': [7,8,9,6],
    'joao': [7,6,4,8],
    'carol': [7,5,9,7],
    'fredi': [4,6,9,9],
}

for name, nota in alunos.items():
    print(name, '=', sum(nota)/4)