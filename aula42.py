#26
eletronica=[
{"item": "fone", "preco": 80.0},
{"item": "carregador", "preco": 40.0},
{"item": "mousepad", "preco": 30.0}
]
eletronica[0]["preco"]=eletronica[0]["preco"]*1.20
eletronica.append({"item": "cabo usb", "preco": 30.0})
esgotado=eletronica.pop(1)
soma=eletronica[0]["preco"]+eletronica[-1]["preco"]
print(esgotado)
print(soma)
print(eletronica)
print(len(eletronica))
