#25
oficina=[
{"servico": "troca de oleo", "valor": 100},
{"servico": "alinhamento", "valor": 80.0},
{"servico": "balenceamento", "valor": 60.0}
]
oficina[0]["valor"]=oficina[0]["valor"]*1.15
oficina.append({"servico": "lavegem", "valor": 40.0})
cancelado=oficina.pop(1)
soma= oficina[0]["valor"] + oficina[-1]["valor"]
print(cancelado) 
print(soma)
print(oficina)
print(len(oficina))
