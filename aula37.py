#21
menu=[
{"item": "café", "preco": 5.0},
{"item": "suco", "preco": 8.0},
{"item": "bolo", "preco": 12.0}
]
menu[0]["preco"]=menu[0]["preco"]*1.10
menu.append({"item": "pao", "preco": 6.0})
remv=menu.pop(1)
total=menu[0]["preco"]+menu[-1]["preco"]
print(remv)
print(total)
print(menu)
print(len(menu))
