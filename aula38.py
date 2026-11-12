#22
remedio=[
{"nome": "dipirona", "preco": 10.0},
{"nome": "paracetomal", "preco": 15.0},
{"nome": "vitamina c", "preco": 20.0}
]
remedio[0]["preco"]=remedio[0]["preco"]*1.20
remedio.append({"nome": "anti-alergico", "preco": 25.0})
remv=remedio.pop(1)
dif=remedio[-1]["preco"]-remedio[0]["preco"]
print(remv)
print(dif)
print(remedio)
print(len(remedio))
