#28
livraria = [
    {"titulo": "ficcao", "preco": 45.0},
    {"titulo": "historia", "preco": 60.0},
    {"titulo": "poesia", "preco": 30.0}
]
livraria[0]["preco"]=livraria[0]["preco"]*1.10
livraria.append({"titulo": "quadrinhos", "preco": 25.0})
esgotado=livraria.pop(1)
dif=livraria[-1]["preco"]-livraria[1]["preco"]
print(esgotado)
print(dif)
print(livraria)
print(len(livraria))
