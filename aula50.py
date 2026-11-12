#5
papelaria=[
{"item": "caderno", "preco": 20.0},
{"item": "caneta", "preco": 4.0},
{"item": "lapis", "preco": 2.0}
]
for i in papelaria:
    i["preco"]=i["preco"]*1.10
    print(f"o item {i['item']} tem o preco de {i['preco']}")

print(papelaria)
