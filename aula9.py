alunos =["Lucas", "Marcos", "Pedro", "anna"]
novo_aluno1 =input("Digite o nome do novo aluno: ")
novo_aluno2 = input("Digite o nome de outro aluno: ")
remv_aluno = input("Digite o nome do aluno pra ser removido: ")
alunos.append(novo_aluno1)
alunos.append(novo_aluno2)
alunos.remove(remv_aluno)

if "Roque" not in alunos:
    alunos.append("Roque")

alunos.sort()
print("os alunos são ", alunos)
print("a quantidade de pessoas na sala são", len(alunos))
