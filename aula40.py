#24
feira=[
{"fruta": "maca", "preco": 4.0},
{"fruta": "banana", "preco": 6.0},
{"fruta": "uva", "preco": 10.0}
]
feira[0]["preco"]=feira[0]["preco"]*1.30
feira.append({"fruta": "manga", "preco": 5.0})
esgotado=feira.pop(1)
dif=feira[1]["preco"]-feira[-1]["preco"]
print(esgotado)
print(dif)
print(feira)
print(len(feira))
