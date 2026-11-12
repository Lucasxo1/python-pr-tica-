#16
produtos=[{"nome": "mouse", "preco": 50.0 },
{"nome": "teclado", "preco": 120.0 },
{"nome": "monitor", "preco": 800.0}
]
produtos[0]["preco"] =produtos[0]["preco"] *1.10
produtos.append({"nome": "fone", "preco": 90.0})
removido=produtos.pop(1)
soma =produtos[0]["preco"] + produtos[-1]["preco"]

print(removido)
print(soma)
print(produtos[0]["preco"])
print(len(produtos))
