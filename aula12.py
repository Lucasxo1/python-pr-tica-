aluno = {"nome": "Trindade", "idade": 19,}
aluno["nota"] = float(input("Digite a nota: "))
if aluno["nota"] >= 7.0:
    aluno ["status"] = "Aprovado"
else: 
    aluno["status"] = "Reprovado"

print("STATUS DO ALUNO", aluno["status"])
print("A nota do aluno", aluno["nota"])
print("FICHA COMPLETA", aluno)
