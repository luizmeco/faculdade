alunos = ["Joao", "Carolina"]

novo_aluno = "Nicole"


if novo_aluno in alunos:
    print("O estudante " + novo_aluno + " ja está na lista")
else:
    alunos.insert(0, novo_aluno)
    print(alunos)

alunos[1] = "Luiz"
print(alunos)