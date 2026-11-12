aluno ={"nome": "Gabriel", "falta": 3}
aluno["novas_falta"] = int(input("Digite a quantidade de novas falta: "))
aluno["falta"] += aluno["novas_falta"]
if aluno["falta"] >=5:
    aluno["situação"] = "Limite atingindo"
    print(aluno["situação"])
else:
    aluno["situação"] ="regular"
    print(aluno["situação"])
