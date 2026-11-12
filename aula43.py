#27
roupas=[
{"peça": "camisa", "preco": 50.0},
{"peça": "calça", "preco": 100.0},
{"peça": "casaco", "preco": 150.0}
]
roupas[0]["preco"]=roupas[0]["preco"]*1.10
roupas.append({"peça": "meia", "preco": 15.0})
esgotado=roupas.pop(1)
dif=roupas[1]["preco"]-roupas[-1]["preco"]
print(esgotado)
print(dif)
print(roupas)
print(len(roupas))
