#2
eletronicos=[
{"item": "fone", "preco": 100.0},
{"item": "mouse", "preco": 50.0},
{"item": "teclado", "preco": 150.0}
]
for i in eletronicos:
    i["preco"]=i["preco"]*1.20
    print(f"o item: {i['item']} tem o preço agora de {i['preco']}")
