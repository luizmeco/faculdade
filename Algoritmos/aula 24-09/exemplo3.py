alunos = ["Joao", "Carolina"]

novo_aluno = "Nicole"


if novo_aluno in alunos:
    print("O estudante " + novo_aluno + " ja está na lista")
else:
    alunos.append(novo_aluno)
    print(f"O nome {novo_aluno} foi adicionado")
