alunos= ["Gabriel", "Julia", "Julio", "Lucas", "Pedro"]
novo_aluno =input("Digite o nome de um novo aluno: ")
alunos.append(novo_aluno)
if "Pedro" in alunos:
    alunos.remove("Pedro")

alunos.sort()
print("os alunos são: ", len (alunos))
print("O aluno do dia é o ", alunos[0])
print("a ordem dos alunos", alunos)
