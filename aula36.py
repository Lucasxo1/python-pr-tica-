#20
alunos =[
{"nome": "carlos", "nota": 6.0},
{"nome": "mariana", "nota": 8.0},
{"nome": "pedro", "nota": 5.0}
]
alunos[0]["nota"]=alunos[0]["nota"]*1.25
alunos.append({"nome": "sofia", "nota": 9.0})
transferido=alunos.pop(2)
md=(alunos[0]["nota"]+alunos[-1]["nota"])/2
print(transferido)
print(md)
print(alunos[0]["nota"])
print(alunos)
print(len(alunos))
