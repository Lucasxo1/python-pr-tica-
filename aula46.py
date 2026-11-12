#30
papelaria = [
    {"item": "caderno", "preco": 25.0},
    {"item": "caneta", "preco": 5.0},
    {"item": "mochila", "preco": 120.0}
]
papelaria[0]["preco"]=papelaria[0]["preco"]*1.20
papelaria.append({"item": "estojo", "preco": 15.0})
esgotado=papelaria.pop(1)
soma=papelaria[0]["preco"]+papelaria[1]["preco"]
print(esgotado)
print(soma)
print(papelaria)
print(len(papelaria))
