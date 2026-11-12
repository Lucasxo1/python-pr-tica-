#29 
padaria = [
    {"item": "pao frances", "preco": 10.0},
    {"item": "queijo", "preco": 20.0},
    {"item": "presunto", "preco": 18.0}
]
padaria[0]["preco"]=padaria[0]["preco"]*1.10
padaria.append({"item": "manteiga", "preco": 12.0})
esgotado=padaria.pop(1)
soma=padaria[0]["preco"]+padaria[-1]["preco"]
print(esgotado)
print(soma)
print(padaria)
print(len(padaria))
