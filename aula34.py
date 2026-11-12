#18
frota =[
{"modelo": "gol", "km": 40000.0},
{"modelo": "onix", "km": 25000.0},
{"modelo": "civic", "km": 60000.0}
]
frota[0]["km"]=frota[0]["km"]*1.20
frota.append({"modelo": "corolla", "km": 10000.0})
vendido=frota.pop(1)
soma=frota[0]["km"]+frota[-1]["km"]
print(vendido)
print(soma)
print(frota)
print(len(frota))
