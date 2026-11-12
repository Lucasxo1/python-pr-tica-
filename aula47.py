#1
mercado = [
{"item": "arroz", "preco": 20.0},
{"item": "feijão", "preco": 8.0},
{"item": "leite", "preco": 5.0}
]
for i in mercado:
    i["preco"]=i["preco"]*1.10
    print(f"o item {i['item']}, agora custa {i['preco']}")
