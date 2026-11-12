#3
roupas = [
{"item": "camiseta", "preco": 40.0},
{"item": "calca", "preco": 100.0},
{"item": "casaco", "preco": 200.0}
]
for i in roupas:
    i["preco"]=i["preco"]*0.90
    print(f"o tem do {i['item']} agora é do valor {i['preco']}")
