alunos = ["Joao", "Carolina", "Nicole", "Nicole", "Nicole", "Nicole"]
alunos2 = ["Luiz", "Guto", "Duda"]

alunos.extend(alunos2)

print(alunos)

for aluno2 in alunos2:
    alunos.remove(aluno2)
    print(alunos)

while "Nicole" in alunos:
    alunos.remove("Nicole")
    print(alunos)

